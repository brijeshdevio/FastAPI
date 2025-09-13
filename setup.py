from db import Base, engine
from models import Feedback
from models import User 
from models import Product
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")

