# Borrower API v2

## Install

```shell
pip install -r src/requirements.txt
```

For init database, in addition

```shell
pip install -r init-db/requirements.txt
```

## Migrate database

```shell
cp init-db/old_database.db data/database.db
cd src
alembic upgrade head
cd ../init-db
python load.py
```

Migration history:
```shell
alembic revision --autogenerate -m "add child_count and social_family_quotient"
```

# Run api

```shell
cd src
```

For dev

```shell
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

go to 

http://localhost:8000/docs

![](api-create_borrower_borrowers__post.png)
