from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# The Engine
engine = create_engine('sqlite:///zoo.db', echo=False)
# bind will bind the session context to the engine database
Session = sessionmaker(bind=engine)
session = Session()
# a model tells SQLAlchemy the name of our table and the names and contents of each column
# Base (a class) maps our models to the database
Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat = Column(String)

    # this is a relationship between the Animal and Zookeeper tables
    # this will create a list of zookeepers for each animal
    logs = relationship('Logbook', back_populates='animal', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f'\n<Animal(name={self.name}, habitat={self.habitat})>'


class Logbook(Base):
    __tablename__ = 'logbook'

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey('animals.id'))
    notes = Column(String)

    # this will create a relationship between the Logbook and Animal tables
    # this will create a list of logs for each animal
    animal = relationship('Animal', back_populates='logs')

    def __repr__(self):
        return f'\n<Logbook(animal_id={self.animal_id}, notes={self.notes})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    lion = Animal(name="Lion", habitat="Savannah")
    wombat = Animal(name="Wombat", habitat="Ocean")
    # session.add(lion)
    # session.add(wombat)
    # session.commit()
    # # print(lion.name)

    # lion_log = Logbook(animal_id=1, notes="Loves to eat MEAT!!!")
    # lion_log2 = Logbook(animal_id=1, notes="MEAT!!!")
    # wombat_log = Logbook(animal_id=2, notes="Why do they like the OCEAN?!")
    # wombat_log2 = Logbook(animal_id=2, notes="Seems to be adapting as a Fish....")
    # session.add(lion_log)
    # session.add(lion_log2)
    # session.add(wombat_log)
    # session.add(wombat_log2)
    # session.commit()

    # print(lion_log.id)
    # print(lion_log.animal)
    # print(lion.logs)

    # lion = session.query(Animal).filter(Animal.name == "lion").first()
    # wombat = session.query(Animal).filter(Animal.name == "wombat").first()
    # lion_log =session.query(Logbook).filter(Logbook.animal_id == 1).first()
    # seal_log = session.query(Logbook).filter(Logbook.animal_id == 2).first()

    # session.delete(seal)
    # session.commit()
    # session.delete(lion_log)
    # session.commit()
    for logs in session.query(Logbook):
        print(logs)

    for animal in session.query(Animal):
        print(animal)

    print(lion.logs)


