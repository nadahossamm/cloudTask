from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer , String
from config.db import meta

restaurants = Table(
    'restaurants',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('type',String(255)),
    Column('location',String(255)),

)