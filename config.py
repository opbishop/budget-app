from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

data = 'data'
statement_data = '{}/statements'.format(data)
database = '{}/statements.db'.format(data)

engine = create_engine('sqlite:///{}'.format(database), echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()