# Configurations related to the scraper
SCRAPER_URL = 'https://www.kvb.co.in/nri/products/deposits/fcnr-deposits/#fcnr-interest-rate'
REQUEST_TIMEOUT = 30  # Time in seconds
RETRY_COUNT = 3  # Number of retries before failing

# Example: Database connection string if using external DB instead of SQLite
DATABASE_URL = 'sqlite:///db.sqlite3'
