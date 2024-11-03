from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    """Modelo para crear un nuevo usuario."""
    name: str
    age: int | None = None
    email: str

class ItemCreate(BaseModel):
    """Modelo para crear un nuevo item."""
    name: str
    description: str | None = None
    price: float
    user_id: int 

class UserUpdate(BaseModel):
    """Modelo para actualizar un usuario existente. Todos los campos son opcionales."""
    name: str | None = None
    age: int | None = None
    email: str | None = None


class ItemUpdate(BaseModel):
    """Modelo para actualizar un item existente. Todos los campos son opcionales."""
    name: str | None = None
    description: str | None = None
    price: float | None = None
    user_id: int | None = None