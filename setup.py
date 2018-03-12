from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, REAL
import config

engine = create_engine('sqlite:///{}'.format(config.database), echo=True)

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    mcc = Column(REAL)
    description = Column(String)
    amount = Column(REAL)
    category = Column(String)

    def __repr__(self):
        return '<Transaction(date={}, mcc={}, description={}, amount={}, category={})>'.format(self.date, self.mcc,
                                                                                               self.description,
                                                                                               self.amount,
                                                                                               self.category)

def build_database():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
