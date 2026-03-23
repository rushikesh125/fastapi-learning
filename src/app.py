from fastapi import FastAPI,HTTPException,status
import json
from pathlib import Path 
from src.schemas import PostCreate
app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR/ "posts.json"


def load_posts():
    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)
# def write_posts():
#     with open(file_path,"w") as file:

@app.get("/")
def app_get():
    return {"message":"Hello, Everything is good!."}

@app.get("/posts")
def get_all_posts(limit:int=None):
    data = load_posts()
    posts = data["posts"]
    if (limit and limit<len(posts)):
        return posts[:limit]
    return posts

@app.get("/posts/{id}")
def get_post(id:int):
    data = load_posts()
    posts = data["posts"]
    if(id>len(posts)):
        raise HTTPException(status_code=404,detail="Post Not Found")
    return posts[id-1]

@app.post("/post")
def create_post(post:PostCreate):
    try:
        data = load_posts()
        posts = data["posts"]
        posts.append(post)
        return posts
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
