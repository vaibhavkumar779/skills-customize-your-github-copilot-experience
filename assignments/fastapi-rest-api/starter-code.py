from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items")
def read_items():
    # Return a sample list of items
    return [{"name": "Sample Item", "price": 9.99}]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # Return the item ID and optional query parameter
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item):
    # Return the created item data
    return item
