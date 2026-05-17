from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    bio = Column(String, nullable=True)
    avatar_url= Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    cover_img_url = Column(String, nullable=True)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class Vote(Base):

    __tablename__ = "votes"

    user_id= Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
    post_id= Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True)

class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)

class PostTags(Base):
    __tablename__ = "post_tags"

    post_id= Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True)
    tag_id= Column(Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)