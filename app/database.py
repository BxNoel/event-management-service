from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL for MySQL (adjust your actual connection string accordingly)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/event_management_service"

# Create the SQLAlchemy engine (no need for connect_args)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
