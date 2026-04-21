from fastapi import FastAPI,HTTPException,Request
from mockData import products
from dtos import Product
app = FastAPI()


@app.get("/")
def home():
    return "Everything is Good!.."


@app.get("/products/{id}")
def getProductById(id:int):
    if id<1 or id>len(products):
        raise HTTPException(status_code=404,details="products not found")
    return products[id-1]

@app.get("/products")
def getProductByQuery(request:Request):
     
    return products

@app.post("/create")
def createProduct(data:Product):
    id = len(products)+1
    product = {
        "id":id,
        **data.model_dump()
    }
    products.append(product)
    return products
