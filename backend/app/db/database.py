from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base

DATABASE_URL = "postgresql://gpbreed:gpbreed_password@localhost:5432/gpbreed"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()