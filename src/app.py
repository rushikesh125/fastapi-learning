from fastapi import FastAPI,HTTPException
import json
from pathlib import Path 

app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR/ "posts.json"


def load_posts():
    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)
@app.get("/")
def app_get():
    return {"message":"Hello, Everything is good!."}

@app.get("/posts")
def get_all_posts():
    posts = load_posts()
    return posts

@app.get("/posts/{id}")
def get_post(id:int):
    data = load_posts()
    posts = data["posts"]
    if(id>len(posts)):
        raise HTTPException(status_code=404,detail="Post Not Found")
    return posts[id-1]