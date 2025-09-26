from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
import uvicorn

# Define the data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Create a new FastAPI instance
app = FastAPI()

# In-memory storage for items
items = {}

# CREATE - Post method
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

# READ - Get method
@app.get("/items/", response_model=List[Item])
async def read_items():
    return list(items.values())

@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]

# UPDATE - Put method
@app.put("/items/{item_name}", response_model=Item)
async def update_item(item_name: str, item: Item):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_name] = item
    return item

# DELETE - Delete method
@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_name]
    return {"message": "Item deleted successfully"}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)