from sqlalchemy.orm import Session
from app.database import SessionLocal

# Dependency to get a database session for each request
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
