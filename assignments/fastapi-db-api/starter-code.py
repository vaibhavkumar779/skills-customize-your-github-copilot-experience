from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float


class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True


app = FastAPI()


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup_event():
    init_db()


@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate):
    with Session(engine) as db:
        db_item = ItemModel(name=item.name, description=item.description, price=item.price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


@app.get("/items", response_model=list[ItemResponse])
def read_items():
    with Session(engine) as db:
        items = db.query(ItemModel).all()
        return items


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    with Session(engine) as db:
        item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    with Session(engine) as db:
        db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db_item.name = item.name
        db_item.description = item.description
        db_item.price = item.price
        db.commit()
        db.refresh(db_item)
        return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as db:
        db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(db_item)
        db.commit()
        return {"detail": "Item deleted"}
