from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker #, declarative_base


host = 'localhost' # 127.0.0.1
port = '5432'
user = 'postgres'
password = '123123'
database = 'BPTSO-20-IT-2'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
# postgresql+psycopg2://postgres:123123@localhost:5432/BPTSO-20-IT-2

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cityname = Column(String(50), nullable=False)
    zipcode = Column(String(4), nullable=False)

    def __init__(self, cityname, zipcode):
        self.cityname = cityname
        self.zipcode = zipcode


class AccountTypes(Base):
    __tablename__ = 'accounttypes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    accounttypename = Column(String(50), nullable=False)


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idnumber = Column(String(11), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(50))
    dateofbirth = Column(Date)
    cityid = Column(Integer, ForeignKey('cities.id'))
    street = Column(String(70))
    housenumber = Column(String(5))
    income = Column(Float)
    create_date = Column(DateTime)
    update_date = Column(DateTime)


    # def __repr__(self):
    #     return self.first_name


class Account(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customeridnumber = Column(String(11), ForeignKey('customers.idnumber'), nullable=False)
    accountnumber = Column(String(50), nullable=False)
    accounttypeid = Column(Integer, ForeignKey('accounttypes.id'), nullable=False)
    balance = Column(Float, default=0)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


