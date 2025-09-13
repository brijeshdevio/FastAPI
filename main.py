from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from models import Product, User, Feedback
from pydantic import BaseModel

# create FastAPI app
app = FastAPI(title="NeonDB + FastAPI Demo")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        # Create tables if they don't exist
        yield db
    finally:
        # Close DB session
        db.close()

# Pydantic model for user request 
class UserCreate(BaseModel):
    name: str
    email:str

# Pydantic model for user response 
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Enables ORM mode to work with SQLAlchemy models
    class Config:
        orm_mode: True

# Pydantic model for product request 
class ProductCreate(BaseModel):
    product_name: str
    quantity: str
    in_stock: bool

# Pydantic model for product response 
class ProductResponse(BaseModel):
   product_id: int
   product_name: str
   quantity: str
   in_stock: bool

# Enables ORM mode to work with SQLAlchemy models
   class Config:
        orm_mode: True

# Pydantic model for feedback request
class FeedbackCreate(BaseModel):
    name: str
    comment: str

# Pydantic model for feedback response
class FeedbackResponse(BaseModel):
    id: int
    name: str
    comment: str

# Enables ORM mode to work with SQLAlchemy models
    class Config:
        orm_mode: True


# default route
@app.get("/")
def root():
    return {"message": "Welcome to the NeonDB + FastAPI Demo!"}

# create a new user
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # create new user
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get all users
@app.get("/users/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# create a new product
@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        product_name=product.product_name,
        quantity=product.quantity,
        in_stock=product.in_stock
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# get all products
@app.get("/products/", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# create feedback
@app.post("/feedback/", response_model=FeedbackResponse)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = Feedback(name=feedback.name, comment=feedback.comment)
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback

# get all feedback
@app.get("/feedback/", response_model=list[FeedbackResponse])
def read_feedback(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).all()
    return feedbacks