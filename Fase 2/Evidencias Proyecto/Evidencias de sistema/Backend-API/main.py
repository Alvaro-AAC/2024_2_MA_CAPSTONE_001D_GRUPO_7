from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import clases

# Obtener el engine de la base de datos
engine = database.get_engine()

# Crear las tablas si no existen (esto es una simplificación, normalmente se usarían migraciones)
clases.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependencia para obtener una sesión de la base de datos
def get_db():
    db = database.SessionLocal() #Suponiendo que tienes database.SessionLocal configurado para sesiones
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=clases.UserCreate, status_code=201)
def create_user(user: clases.UserCreate, db: Session = Depends(get_db)):
    db_user = clases.User(**user.model_dump()) #Convertir a diccionario y luego a modelo de SQLAlchemy
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/items/", response_model=clases.ItemCreate, status_code=201)
def create_item(item: clases.ItemCreate, db: Session = Depends(get_db)):

    db_item = clases.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



# ... otros endpoints para obtener, actualizar y eliminar usuarios e items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)