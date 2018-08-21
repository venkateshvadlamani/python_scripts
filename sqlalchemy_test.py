import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


def main():
    #engine = create_engine('sqlite://', echo=True)
    engine = create_engine('postgresql://federer:grandestslam@localhost:5432/tennis')

    User.__table__

    Base.metadata.create_all(engine)

    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    print(ed_user.name)


if __name__ == "__main__":
    main()