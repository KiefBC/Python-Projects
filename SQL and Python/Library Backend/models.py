from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create Engine
engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Our Model
class Library(Base):
    __tablename__ = 'LibraryDB'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    date_pub = Column('Date Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'<Book: (name={self.title}, author={self.author}, date_published={self.date_pub}, price={self.price})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
