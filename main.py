from fastapi import FastAPI 

app = FastAPI(title='A little IMDB',
             description='With this project movies can be reviewed',
             version='1.0')

@app.get('/')
async def index():
    return 'hello world'
