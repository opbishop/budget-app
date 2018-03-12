from config import Base
from sqlalchemy import Column, Integer, String, REAL

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
