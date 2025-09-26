import sys
import os
from main import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Stock Market API"


def test_get_stock_price_valid():
    response = client.get("/stock/AAPL")
    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
    assert abs(response.json()["price"] - 150.75) < 1e-6


def test_get_stock_price_invalid():
    response = client.get("/stock/INVALID")
    assert response.status_code == 404
    assert "Symbol not found" in response.json()["detail"]
