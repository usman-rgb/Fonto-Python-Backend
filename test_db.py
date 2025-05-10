<<<<<<< HEAD
from sqlalchemy import create_engine
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
connection = engine.connect()
print("Connection successful!")
=======
from sqlalchemy import create_engine
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
connection = engine.connect()
print("Connection successful!")
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
connection.close()