from sqlalchemy import create_engine
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
connection = engine.connect()
print("Connection successful!")
connection.close()
