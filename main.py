from fastapi import FastAPI,HTTPException
from mockData import products

app = FastAPI()


@app.get("/")
def home():
    return "Everything is Good!.."

# @app.get("/products")
# def getProducts():
#     return products

@app.get("/products/{id}")
def getProductById(id:int):
    if id<1 or id>len(products):
        raise HTTPException(status_code=404,details="products not found")
    return products[id-1]

@app.get("/products")
def getProductByQuery(category:str=None):
    if category!=None:
        res = [n for n in products if n["category"]==category]
        return res
    else:
        return products
