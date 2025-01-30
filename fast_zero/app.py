from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    x = 'teste'
    return x
