import json
import re
import time
from playwright.async_api import async_playwright
from datetime import datetime

# Function to process the tenure text (Python-heavy approach)
def format_tenure(tenure_text):
    # Regex to convert text like "1 Year and above but less than 2 Years" to "Years >= 1 < 2"
    match = re.match(r"(\d+)\s+Year(?:s)?\s+and\s+above\s+but\s+less\s+than\s+(\d+)\s*Year(?:s)?", tenure_text)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        return f"Years >= {start} < {end}"
    
    # If it matches "X Years only", convert to "Years = X"
    match_only = re.match(r"(\d+)\s+Years?\s+only", tenure_text)
    if match_only:
        years = int(match_only.group(1))
        return f"Years = {years}"
    
    return tenure_text.strip()

async def scrape_interest_rates_optimized():
    start_time = time.time()  # Start the timer for the optimized solution

    # Launch the browser using Playwright
    print("Launching the browser...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Go to the target URL directly to the FCNR Interest Rate section
        url = 'https://www.kvb.co.in/nri/products/deposits/fcnr-deposits/#fcnr-interest-rate'
        print(f"Navigating to URL: {url}")
        await page.goto(url, wait_until='networkidle')

        # Wait for the table to appear (simplified selector)
        print("Waiting for the table to appear...")
        try:
            await page.wait_for_selector('#fcnr-interest-rate table', timeout=30000)  # 30s timeout
            print("Table is now loaded.")
        except Exception as e:
            print(f"Error waiting for table: {e}")
            await browser.close()
            return

        # Extract the table data with raw structure (minimal JS code)
        print("Extracting raw table data...")
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

        # Process the raw data in Python (formatting the tenure text)
        print("Processing the table data...")
        processed_data = []
        for entry in table_data:
            formatted_entry = {
                'Tenure': format_tenure(entry['Tenure']),
                'USD Interest Rate': entry['USD Interest Rate']
            }
            processed_data.append(formatted_entry)

        # Create a timestamped filename to avoid overwriting
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'fcnr_interest_rates_optimized_{timestamp}.json'

        # Save the processed data to a JSON file
        print(f"Saving the data to '{filename}'...")
        with open(filename, 'w') as json_file:
            json.dump(processed_data, json_file, indent=4)

        print(f"Data saved to '{filename}'.")

        # Close the browser
        await browser.close()
        print("Browser closed.")

        # Calculate and print the time taken
        end_time = time.time()
        print(f"Optimized solution took {end_time - start_time:.2f} seconds.")

# Run the asyncio event loop to execute the scraping function
import asyncio
asyncio.run(scrape_interest_rates_optimized())
