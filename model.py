from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///ratings.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __repr__(self):
        """Show info about itself instead of memory location."""
        return "<User id=%d, email=%s, password=%s, age=%d, zipcode=%s>" %(self.id, self.email, self.password, self.age, self.zipcode)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    
    release_date = Column(DateTime)
    imdb_url = Column(String(64))

    def __repr__(self):
        """Show info about itself instead of memory location."""
        return "<Movies id=%d, name=%s, release_date=%r, imdb_url=%s" %(self.id, self.name, self.release_date, self.imdb_url)

class Rating(Base):
    __tablename__ = "ratings"
    
    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)

    user = relationship("User", backref=backref ("ratings", order_by=id))
    movie = relationship("Movie", backref=backref ("ratings", order_by=id))

    def __repr__(self):
        """Show info about itself instead of memory location."""
        return "<Ratings id=%d, movie_id=%d, user_id=%d, rating=%d>" %(self.id, self.movie_id, self.user_id, self.rating)

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
