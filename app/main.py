from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models import User, Order
from app.schemas import UserCreate, UserResponse, OrderCreate, OrderResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user_data.email, name=user_data.name, age=user_data.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/orders", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@app.post("/orders", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        user_id=str(order_data.user_id), 
        product_name=order_data.product_name, 
        total=order_data.total
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.delete("/users/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.name = user_data.name
    user.email = user_data.email
    user.age = user_data.age
    
    db.commit()
    db.refresh(user)
    return user

