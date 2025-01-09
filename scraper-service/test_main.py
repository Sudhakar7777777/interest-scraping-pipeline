from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

# Test Health Check
def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Mocking the scrape function for tests
@patch("main.scrape_interest_rates_optimized")
def test_scrape_success(mock_scrape):
    """Test scraping success for a known bank (kvb) with mocked scraper"""
    # Mock the return value of the scraper
    mock_scrape.return_value = [
        {"Tenure": "Years >= 1 < 2", "USD_Interest_Rate": "6.00"},
        {"Tenure": "Years >= 2 < 3", "USD_Interest_Rate": "4.49"},
    ]
    
    response = client.get("/scrape/kvb")
    # print(f"printing...response.....{response}")
    assert response.status_code == 200
    json_data = response.json()
    # print(f"printing...{json_data}.....")
    
    # Validate structure and content of the response
    assert "bank_name" in json_data
    assert json_data["bank_name"] == "kvb"
    assert "data" in json_data
    assert len(json_data["data"]) > 0
    
    # Check if the mock data is used
    assert json_data["data"][0]["Tenure"] == "Years >= 1 < 2"
    assert json_data["data"][0]["USD_Interest_Rate"] == "6.00"

# Test Scraping with an Invalid Bank Name
def test_scrape_invalid_bank():
    """Test scraping failure for an invalid bank name"""
    response = client.get("/scrape/invalidbank")
    # print(f"printing...response.....{response}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Bank not found"}
