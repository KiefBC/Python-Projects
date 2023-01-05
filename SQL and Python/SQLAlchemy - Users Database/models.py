from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The Engine
engine = create_engine('sqlite:///user.db', echo=False)
# bind will bind the session context to the engine database
Session = sessionmaker(bind=engine)
session = Session()
# a model tells SQLAlchemy - Users Database the name of our table and the names and contents of each column
# Base (a class) maps our models to the database
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    # our first columns
    # we import Column uptop which creates a Column in our table
    # we pass in Integer which tells SQLAlchemy - Users Database what the datatype is in this column
    # we set this id as the primary key
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, full_name={self.full_name}, nickname={self.nickname})>'


if __name__ == '__main__':
    # this will connect our engine with our model class to create our database table
    Base.metadata.create_all(engine)

    #######################
    # ADDING DATA TO THE DB
    #######################

    # # we dont need to issue a Pk here, it will be autocreated
    # kief_user = User(name='Kiefer', full_name='Kiefer H', nickname='Kiefx')
    # print(kief_user.name)
    # print(kief_user.id)
    # #
    # # # this will add our user to thge session which communitactes with the database but its not in the DB yet - think adding items to amazon shopping cart but nothing is finalized/comitted
    # # session.add(kief_user)
    # # # print(session.new) # IdentitySet([<User(name=Kiefer, full_name=Kiefer H, nickname=Kiefx)>])
    # # session.commit()
    # print(kief_user.id)
    #
    # # a way of adding multiple users at once
    # new_users = (
    #     [User(name='Grace', full_name='Grace Hopper', nickname='Pioneer'),
    #      User(name='Alan', full_name='Alan Turing', nickname='Computer Scientist'),
    #      User(name='Katherine', full_name='Katherine Johnson', nickname='')]
    # )
    # session.add_all(new_users)
    # session.commit()
    #
    # for user in new_users:
    #     print(user.id)

    # this tells python to go into our models file and find the User class and then use it to create the new user
    # new_user = User(name='Jethr', full_name='Jethro M', nickname='Jetty')
    # # session.add(new_user)
    # # shows new entries in our DB
    # # print(session.new)
    #
    # # now lets change the name to proper as Jethr != Jethro
    # # new_user.name = 'Jethro'
    # # print(session.new)
    # # session.commit()
    #
    # new_user.nickname = 'Jimbo'
    # # this will show ([]) aka nothing because this is not a 'new' entry. we already comitted aka we are changing a existing entry no longer new
    # # print(session.new)
    # # instead we use session.dirty
    # print(session.dirty)
    # # session.dirty

    ###########################
    # QUERY DELETE AND ROLLBACK
    ###########################

    # we can also query
    # jethro = session.query(User).filter(User.name=='Jethro').one()
    # jethro.nickname = 'Boon'
    # # print(session.dirty)
    #
    # aang = User(name='aang', full_name='aang junior', nickname='anger')
    # session.add(aang)
    # # print(session.new)
    #
    # # what if we dont want these changeS? ROLLBACK
    # # session.rollback()
    # # print(session.dirty)
    # # print(session.new)
    #
    # # how do we delete something?
    # # session.commit()
    # # oh no we comitted bad data, lets delete it
    # # session.delete(aang)
    #
    # # lets confirm they dead
    # aang_jr = session.query(User).filter(User.name == 'aang').one()
    # print(aang_jr)

    # querying will returns a tuple, for the non-tuple you need to print user.name user.nickname etc
    for user in session.query(User.name):
        print(user.name)

    # we can also order everything
    # to order DESC - sesison.query(User.name).order_by(User.name.desc())
    # we can slice it as well: sesison.query(User.name).order_by(User.name)[:2] - returns the first 2
    for user in session.query(User.name).order_by(User.name):
        print(user.name)

    # what if we want to start at 2 and stop at the 4th?
    session.query(User.name).order_by(User.name)[2:4]

    # what if we want EVERYTHING?!~
    session.query(User.name).all()

    # heres how we grab the first entry by our order_by
    session.query(User.name).order_by(User.name).first()

    # filter_by takes keyword args and uses regular python opers
    session.query(User.name).filter_by(User.name='Jethro')
    session.query(User.name).filter(User.name='Jethro')

    # we can even add more than filter to be extra sneaky
    session.query(User.name).filter(User.name=='Jethro').filter(User.nickname=='Megatron')



