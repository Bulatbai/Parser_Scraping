from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:world5526320480@localhost:5432/postgres")

Base = declarative_base()

class Parser(Base):
    __tablename__ = "Parser"

    id = Column(Integer, Sequence('good_id_seq'), primary_key=True)
    image = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    bed = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
     
    
Base.metadata.create_all(engine)





 