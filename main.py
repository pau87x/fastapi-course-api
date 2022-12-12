from fastapi import FastAPI 

app = FastAPI(title='A little IMDB',
             description='With this project movies can be reviewed',
             version='1.0')

@app.on_event('startup')
def startup():
    print('Starting server')

@app.on_event('shutdown')
def shutdown():
    print('Shutdown server')

@app.get('/')
async def index():
    return 'hello world'

@app.get('/about')
async def about():
    return 'about'