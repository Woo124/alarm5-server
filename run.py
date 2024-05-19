from src.main.app import uvicorn, app


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
