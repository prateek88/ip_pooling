import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

# https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html
from sqlalchemy_utils import IPAddressType

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class IP(Base):
    __tablename__ = 'ips'

    ip = Column(IPAddressType, primary_key = True)
    reserved = Column(Boolean, unique=False, default=False)
    description = Column(String(250))


######### End ##########

engine = create_engine('sqlite:////root/python_virtual_envs/ip_pooling/pool.db')

Base.metadata.create_all(engine)
