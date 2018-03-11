from sqlalchemy import create_engine
engine = create_engine('sqlite:///foo.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return '<User(name={}, fullname={}, password={})>'.format(self.name, self.fullname, self.password)

# Base.metadata.create_all(engine)
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# print(ed_user.name)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
print(our_user.name)
# print(ed_user is our_user)
# session.commit()