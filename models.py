from datetime import datetime
import json
from sqlalchemy import Column, Integer, String, \
    create_engine, Identity, DateTime, Float, TIMESTAMP
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Dict, Any
import csv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

#создаем асинхронное подключение database
engine = create_async_engine('postgresql+asyncpg://admin:admin@database:5432/admin', echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
session = async_session()
Base = declarative_base()
Session = sessionmaker(bind=engine)

# описываем таблицу currency_data
class Coins(Base):
    __tablename__ = 'currency_data'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    time = Column(TIMESTAMP(float), nullable=False)


    def __repr__(self):
        return f"Coin {self.title}, price {self.price}, timestamp {self.time}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

