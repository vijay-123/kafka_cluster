
from sqlalchemy import Integer, String
from sqlalchemy import Column
from db.database import Base


class DbUser(Base):
    __tablename__ = "vijay"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
