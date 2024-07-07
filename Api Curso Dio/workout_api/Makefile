run:
	@uvicorn workout_api.Main:app --reload


create-migrations:
    @python -m alembic revision --autogenerate -m "init_db"


run-migrations:
    @python -m alembic upgrade head

