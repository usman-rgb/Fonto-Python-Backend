# migrate.py
from app.database import Base, engine
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
