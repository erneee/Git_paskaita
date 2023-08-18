import datetime
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Klientas(Base):
    __tablename__ = 'klientas'
    id = Column(Integer, primary_key=True)
    f_name = Column("vardas", String)
    email = Column("el_pastas", String, unique=True)

    class Produktai(Base):
        __tablename__ = 'produktai'
        id = Column(Integer, primary_key=True)
        name = Column("pavadinimas", String)
        price = Column("kaina", Float)
        order_products = relationship('OrderProduct', back_populates='product')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# git commit -m "" parasytu ka padareme
# git config --global user.email "ernestasvvv@gmail.com"
# git config --global user.name "Ernestas"
