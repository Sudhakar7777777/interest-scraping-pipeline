import asyncio
import json
import time
from pyppeteer import launch
from datetime import datetime
import logging

# Set logging configuration
logging.basicConfig(level=logging.DEBUG)

async def scrape_interest_rates_optimized():
    start_time = time.time()
    logging.debug("Launching the browser...")
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    url = 'https://www.kvb.co.in/nri/products/deposits/fcnr-deposits/#fcnr-interest-rate'
    logging.debug(f"Navigating to URL: {url}")
    await page.goto(url, {'waitUntil': 'networkidle2'})
    
    logging.debug("Waiting for table to load...")
    await page.waitForSelector('#fcnr-interest-rate table', {'timeout': 30000})
    
    table_data = await page.evaluate('''() => {
        const rows = document.querySelectorAll('#fcnr-interest-rate table tbody tr');
        let data = [];
        rows.forEach(row => {
            const cols = row.querySelectorAll('td');
            if (cols.length > 1) {
                let rowData = {
                    'Tenure': cols[0].innerText.trim(),
                    'USD Interest Rate': cols[1].innerText.trim(),
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
