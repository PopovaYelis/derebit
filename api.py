from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException, Query
from sqlalchemy.future import select
from pydantic import BaseModel
from models import Coins, session, engine, Base
from datetime import datetime, timezone, timedelta
from typing import List, Optional


app = FastAPI()
#  schema for HTTP requests
class BaseView(BaseModel):
    id: Optional[int]
    title: Optional[str]
    price: Optional[float]
    time: Optional[datetime]

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


#GET-запрос для получения списка валютных пар по тикеру, последнюю цену или по дате и времени.
@app.get("/currency")
async def get_currencies(ticker: str = Query(...),
                         date_filter: Optional[datetime] = Query(None),
                         latest: Optional[bool] = Query(False)
                         ):
    async with session.begin():
        query  = select(Coins).where(Coins.title == ticker+'_usd')
        if latest:
            query = query.order_by(Coins.time.desc()).limit(1)
        elif date_filter:
            query = query.where(Coins.time >= date_filter, Coins.time < date_filter + timedelta(seconds=1))


        res = await session.execute(query)
        coins = res.scalars().all()

    if not coins:
        raise HTTPException(status_code=404, detail="Криптовалюта не найдена")

    base_views = [BaseView(**jsonable_encoder(coin)) for coin in coins]
    return base_views


