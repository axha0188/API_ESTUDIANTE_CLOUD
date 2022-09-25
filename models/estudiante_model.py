from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from database.conexion import meta, engine

estudiante = Table(
    "estudiante",
    meta,
    Column("id", Integer, primary_key=True),
    Column("cedula", String(10), unique=True),
    Column("nombre", String(100)),
    Column("apellido", String(100)),
    Column("edad", Integer),
    Column("email", String(100)),
    Column("genero", String(1)),
)

meta.create_all(engine)
