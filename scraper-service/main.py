from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import json
import time
from playwright.async_api import async_playwright
from typing import List
import logging

# Set logging configuration
logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="Bank Interest Rate Scraper", description="An API for scraping bank interest rates", version="1.0.0")

# Bank Data Model for API response
class InterestRateData(BaseModel):
    Tenure: str
    USD_Interest_Rate: str

class BankScraperResponse(BaseModel):
    bank_name: str
    data: List[InterestRateData]

# Async function to scrape interest rates using Playwright
async def scrape_interest_rates_optimized(bank_url: str) -> List[InterestRateData]:
    start_time = time.time()
    logging.debug(f"Launching the browser for {bank_url}...")
    
    # Launch Playwright browser (using Chromium in headless mode)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        logging.debug(f"Navigating to URL: {bank_url}")
        await page.goto(bank_url, wait_until='networkidle')

        logging.debug("Waiting for table to load...")
        try:
            await page.wait_for_selector('#fcnr-interest-rate table', timeout=30000)  # Timeout of 30 seconds
        except Exception as e:
            logging.error(f"Error waiting for table: {e}")
            await browser.close()
            raise HTTPException(status_code=500, detail="Error loading table data")

        # Extract table data
        table_data = await page.evaluate('''() => {
            const rows = document.querySelectorAll('#fcnr-interest-rate table tbody tr');
            let data = [];
            rows.forEach(row => {
                const cols = row.querySelectorAll('td');
                if (cols.length > 1) {
                    let rowData = {
                        'Tenure': cols[0].innerText.trim(),
                        'USD_Interest_Rate': cols[1].innerText.trim(),
                    };
                    data.push(rowData);
                }
            });
            return data;
        }''')

        await browser.close()
        end_time = time.time()
        logging.debug(f"Scraped data: {table_data} in {end_time - start_time:.2f} seconds")
    
    return table_data

# Bank URL configuration (For demonstration, add more URLs as needed)
bank_urls = {
    "kvb": "https://www.kvb.co.in/nri/products/deposits/fcnr-deposits/#fcnr-interest-rate",
    # You can add more banks here.
}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Scrape interest rates for a given bank
@app.get("/scrape/{bank_name}", response_model=BankScraperResponse)
async def scrape_interest_rates(bank_name: str):
    """Scrape the interest rates for a given bank name"""
    
    # Check if the bank is in the predefined list
    if bank_name.lower() not in bank_urls:
        raise HTTPException(status_code=404, detail="Bank not found")
    
    # Get the URL for the bank
    bank_url = bank_urls[bank_name.lower()]
    
    # Scrape the data using the asynchronous scraping function
    rates = await scrape_interest_rates_optimized(bank_url)
    
    # Return the scraped data in the response model format
    return {"bank_name": bank_name, "data": rates}

