#!/usr/bin/env py
from sqlalchemy import Column, BigInteger, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import short_url

Base = declarative_base()


def get_session():
    engine = create_engine(f"sqlite:///flask_app.db")
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session


class Url(Base):
    __tablename__ = 'url'
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    original = Column(String(255), unique=True)
    short = Column(String(25), unique=True)

    def __init__(self, original_url):
        self.id = abs(hash(original_url))
        self.original = original_url
        self.short = short_url.encode_url(self.id)

    def __repr__(self):
        return f'Url(original={self.original}, short={self.short})'


def link_hash(original_url):
    session = get_session()

    if not session.query(Url).filter(Url.original == original_url).all():
        db_url_entity = Url(original_url)
        session.add(db_url_entity)
        session.commit()

    return session.query(Url).filter(Url.original == original_url).one().short
