from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from redis import Redis
import json
from running.generate_graph import generate_graph
redis_client = Redis(host="127.0.0.1", port=6379, db=0)
app = FastAPI()


class Data(BaseModel):
    day: str
    duration: int
    distance: float
    password: str


@app.post("/api/running", status_code=200)
async def add_data(data: Data):
    try:
        datetime.strptime(data.day, "%x")
        redis_client.set(data.day, json.dumps(
            {"time": data.duration, "distance": data.distance})
            )
        if data.password != "qmqmqm8c3":
            raise HTTPException(status_code=404, detail="Sai mật khẩu")
        generate_graph()
    except ValueError:
        raise HTTPException(status_code=404, detail="Format ngày không hợp lệ")
    return "Update thành công"
