'''command for running: uvicorn main:app --reload
'''
from fastapi import FastAPI
from routers import audio

app = FastAPI()
app.include_router(audio.router)

def main():
    pass


if __name__ == "__main__":
    main()