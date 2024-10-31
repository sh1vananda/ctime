from fastapi import FastAPI
from get_time_for_location import get_time_for_location

app = FastAPI()

@app.get("/time")
async def read_time(country: str, city: str):
    try:
        current_time = get_time_for_location(country, city)
        return {"Country": country, "City": city, "Current Time": current_time}
    except Exception as e:
        return {"error": str(e)}

# http://localhost:8000/time?country=japan&city=tokyo