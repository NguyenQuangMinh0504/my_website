from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from redis import Redis
import json
redis_client = Redis(host="127.0.0.1", port=6379, db=0)
app = FastAPI()


class Data(BaseModel):
    day: str
    duration: int
    distance: float
    password: str


@app.post("/running", status_code=200)
async def add_data(data: Data):
    try:
        date = datetime.strptime(data.day, "%x")
        redis_client.set(data.day, json.dumps(
            {"time": data.duration, "distance": data.distance})
            )
        print(date)
        print(data.duration)
        print(data.distance)
        if data.password != "qmqmqm8c3":
            raise HTTPException(status_code=404, detail="Sai mật khẩu")
    except ValueError:
        raise HTTPException(status_code=404, detail="Format ngày không hợp lệ")
    return "Update thành công"
