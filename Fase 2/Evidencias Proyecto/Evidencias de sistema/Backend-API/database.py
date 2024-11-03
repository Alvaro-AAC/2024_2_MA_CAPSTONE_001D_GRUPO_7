import os
import sqlalchemy
from sqlalchemy import create_engine

def get_engine():
    """Obtiene el engine de la base de datos. 

    Si la base de datos no existe, la crea.

    Returns:
        sqlalchemy.engine.Engine: El engine de la base de datos.
    """
    db_path = os.path.abspath("./../Database/db.sqlite3")
    return create_engine(db_path)  # Llama a create_engine con la ruta


def create_engine(db_path):
    """Crea el engine de la base de datos.

    Si la base de datos no existe, la crea.

    Args:
        db_path (str): La ruta a la base de datos.

    Returns:
        sqlalchemy.engine.Engine: El engine de la base de datos.
    """
    if not exists_database(db_path):
        create_database(db_path)
    return sqlalchemy.create_engine(f"sqlite:///{db_path}")


def exists_database(db_path):
    """Verifica si la base de datos existe.

    Args:
        db_path (str): La ruta a la base de datos.

    Returns:
        bool: True si la base de datos existe, False en caso contrario.
    """
    return os.path.exists(db_path)


def create_database(db_path):
    """Crea la base de datos.

    Args:
        db_path (str): La ruta a la base de datos.
    """
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    engine = sqlalchemy.create_engine(f"sqlite:///{db_path}")
    engine.connect().close()