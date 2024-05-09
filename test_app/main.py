from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_ping():
    print("pong")
    return "Hello"


@app.get("/another")
async def another():
    print("another")
    return "World"
