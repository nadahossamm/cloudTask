from fastapi import APIRouter
from config.db import conn
from Models.index import restaurants
from schema.index import Restaurant

restaurant = APIRouter()


@restaurant.get("/")
async def read_restaurant_data():
    return conn.execute(restaurants.select()).fetchall()


@restaurant.get(f"/{type}")
async def get_restaurant_data(type: str):
    return conn.execute(restaurants.select().where(restaurants.c.type == type)).fetchall()


@restaurant.get("/{location}")
async def get_restaurant_data(location: str):
    return conn.execute(restaurants.select().where(restaurants.c.location == location)).fetchall()


@restaurant.get("/{location,type}")
async def get_restaurant_data(location: str, type:str):
    return conn.execute(restaurants.select().where(restaurants.c.location == location and restaurants.c.type==type)).fetchall()


@restaurant.post("/")
async def add_data(restaurant : Restaurant):
    conn.execute(restaurants.insert().values(name=restaurants.name,
                                             type=restaurants.type,
                                             location=restaurants.location
                                             ))
    return conn.execute(restaurants.select()).fetchall()



@restaurant.put("/{id}")
async def update_data(id:int,restaurant:Restaurant):
    conn.execute(restaurants.insert().values(name=restaurants.name,
                                             type=restaurants.type,
                                             location=restaurants.location
                                             ).where(id==restaurants.id,
                                                     ))
    return conn.execute(restaurants.select()).fetchall()

