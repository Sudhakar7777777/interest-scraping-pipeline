import pytest
from scraper.scraper import scrape_interest_rates_optimized


@pytest.mark.asyncio
async def test_scrape_interest_rates_basic():
    data = await scrape_interest_rates_optimized()
    assert data is not None, "Scraper returned no result"


@pytest.mark.asyncio
async def test_scrape_interest_rates():
    data = await scrape_interest_rates_optimized()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'Tenure' in data[0]
    assert 'USD Interest Rate' in data[0]
