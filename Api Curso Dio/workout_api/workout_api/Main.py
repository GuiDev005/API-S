from fastapi import FastAPI
from workout_api.routers import api_router



app = FastAPI(title = 'Minha_API')

app.include_router(api_router)

#if __name__ == 'Main':
    #import uvicorn
    
    #uvicorn.run('Main:app', host ='0.0.0.0', port = 8000, log_level = 'info', reload = True)