### models.py ###
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, TIMESTAMP
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class post(Base):
    __tablename__ = 'flash'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, unique=True)
    up = Column(Integer)
    down = Column(Integer)
    title = Column(String)
    content = Column(Text)
    views = Column(Integer)
    timestamp = Column(TIMESTAMP)
    tags = Column(String)

    def __repr__(self):
        return "<post(post_id='{}', up='{}', down={}, content={})>" \
            .format(self.post_id, self.up, self.down, self.content)


### config.py ###

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = 'postgres+psycopg2://postgres:laurence@127.0.0.1:5432/eightbtc'

### crud.py ###

from sqlalchemy import create_engine


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    recreate_database()
