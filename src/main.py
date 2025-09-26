from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Stock Market API"}


@app.get("/stock/{symbol}")
def get_stock_price(symbol: str):
    if symbol == "AAPL":
        return {"symbol": "AAPL", "price": 150.75, "currency": "USD"}
    else:
        raise HTTPException(status_code=404, detail="Symbol not found")
