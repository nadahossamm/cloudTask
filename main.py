from fastapi import FastAPI
from routes.index import restaurant

app=FastAPI()

app.include_router(restaurant)