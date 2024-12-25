from prometheus_client import generate_latest, CollectorRegistry
from scraper import app

def test_scraper_metrics():
    registry = CollectorRegistry()
    metrics = generate_latest(registry)
    assert "scraper_runtime_seconds" in str(metrics), "Scraper runtime metric not found"
