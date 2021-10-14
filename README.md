# FastAPI start template

[It's fork, with some changes. Thank for this work!🙂](https://github.com/visini/abstracting-fastapi-services)

### Defaul stack:
- DB: Postgresql
- ORM: SQLAlchemy
- test: pytest

### Just clone and have fun 😅

```
pip install -r requirmetns.txt
```
***NOTE: No version set in requirmetns!***

***NOTE: docker-compose only for dev env and only with DB!***

## Run:
create ```.env```:
```
DB_NAME="my_db_name"
DB_USER="my_user_name"
DB_PASSWORD="my_very_strong_password"
```
Then:
```
docker compose up
uvicorn app.main:app <MORE OPTIONS>
```
Then go to ```http://127.0.0.1:8000/docs#/``` and enjoy 😋
