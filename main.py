import asyncio
import time
from datetime import datetime, timezone, timedelta
from aiohttp import ClientSession
from models import Coins, session, engine, Base
import json



async def  get_price(ticker):
    url = "https://deribit.com/api/v2/public/get_index_price"
    params = {
        'index_name': f'{ticker}_usd'
    }

    async with ClientSession() as sessions:
        async with sessions.get(url=url, params=params) as response:
            data = await response.text()
            json_data = json.loads(data)
            data = [json_data['result']['index_price'],json_data['usOut']]
            milliseconds = float(data[1])/1000
            dt = datetime.fromtimestamp( milliseconds/1000, tz=timezone.utc)
    new_record = Coins(title=ticker+'_usd', price=data[0], time=dt)
    return new_record


async def do_tasks():
    while True:
        results = await asyncio.gather(
            get_price("btc"),
            get_price("eth")
        )
        async with session.begin():
            session.add(results[0])
        async with session.begin():
            session.add(results[1])
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(do_tasks())