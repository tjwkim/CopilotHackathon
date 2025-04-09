from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Optional
import json
import os
from product import Product  # src. 제거
from cart import Cart  # src. 제거

app = FastAPI()
cart = Cart()
templates = Jinja2Templates(directory="templates")  # src/ 제거

# 절대 경로로 수정
file_path = os.path.join(os.path.dirname(__file__), 'automobileParts.json')
with open(file_path) as f:
    products = json.load(f)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "products": products, "cart_items": cart.items, "cart_total": cart.calculate_total()})

@app.get("/products", response_model=List[Product])
def get_products(offset: int = 0, limit: int = 10):
    return products[offset:offset+limit]

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/search", response_class=HTMLResponse)
def search_products(
    request: Request,
    name: Optional[str] = Query(None),
    description: Optional[str] = Query(None),
    manufacturer: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None)
):
    result = products
    if name:
        result = [product for product in result if name.lower() in product["name"].lower()]
    if description:
        result = [product for product in result if description.lower() in product["description"].lower()]
    if manufacturer:
        result = [product for product in result if manufacturer.lower() in product["manufacturer"].lower()]
    if min_price is not None:
        result = [product for product in result if product["price"] >= min_price]
    if max_price is not None:
        result = [product for product in result if product["price"] <= max_price]
    return templates.TemplateResponse("index.html", {"request": request, "products": result, "cart_items": cart.items, "cart_total": cart.calculate_total()})

@app.post("/cart/add/{product_id}")
def add_to_cart(product_id: int):
    for product in products:
        if product["id"] == product_id:
            cart.add_product(Product(**product))
            return {"message": "Product added to cart"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/cart/remove/{product_id}")
def remove_from_cart(product_id: int):
    cart.remove_product(product_id)
    return {"message": "Product removed from cart"}

@app.get("/cart/total")
def get_cart_total():
    return {"total": cart.calculate_total()}

@app.get("/cart/items", response_model=List[Product])
def get_cart_items():
    return cart.items