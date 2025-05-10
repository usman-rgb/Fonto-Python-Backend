<<<<<<< HEAD
# migrate.py
from app.database import Base, engine
Base.metadata.create_all(bind=engine)
=======
# migrate.py
from app.database import Base, engine
Base.metadata.create_all(bind=engine)
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
print("Tables created successfully!")