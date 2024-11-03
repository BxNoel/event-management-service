import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#Make connection to DOCKERIZED Database:
connection = mysql.connector.connect(
    user='root',
    password='password',
    host='mysql',
    port=3306,
    database='event_management_service'
)
print("DB connected")


# Database URL for MySQL (adjust your actual connection string accordingly)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@mysql:3306/event_management_service"

# Create the SQLAlchemy engine (no need for connect_args)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
