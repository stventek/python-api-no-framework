# python-api-no-framework

Simple python recipe REST API built with no framework using:

- Python as Programming Language. 
- Werkzeug for WSGI utilities.
- Marshmallow and Marshmallow-SQLAlchemy for serialization and deserialization. 
- SQLAlchemy as an ORM.
- PostgreSQL as a database. 
- Alembic 2.0 as database migrations tool. 

This is a WSGI application that utilizes ```wsgiref.simple_server``` for development purposes. Additionally, it includes a wsgi.py file for deploying the application with Gunicorn.

## Models

Model: Ingredient

| Attribute              | Type                 |
| ----------------------|---------------------|
| id                     | int (primary key)    |
| name                   | str (30)             |
| measurement_unit       | str (30)             |

| Relationship       | Type                     |
| -------------------|-------------------------|
| recipes (viewonly)  | List[Recipe]             |
| recipe_associations | List[AssociationIngredientRecipe] |

Model: Recipe

| Attribute         | Type                 |
| ------------------|---------------------|
| id                | int (primary key)    |
| name              | str (30)             |
| description       | Optional[str]        |
| instructions      | Optional[str]        |

| Relationship         | Type                     |
| ---------------------|-------------------------|
| ingredients (viewonly)| List[Ingredient]         |
| ingredient_associations| List[AssociationIngredientRecipe] |

Model: AssociationIngredientRecipe

| Attribute         | Type                  |
| ------------------|----------------------|
| ingredient_id      | int (primary key)    |
| recipe_id          | int (primary key)    |
| quantity           | Optional[str]        |

| Relationship | Type       |
| --------------|-----------|
| recipe        | Recipe     |
| ingredient    | Ingredient |

## Endpoints

The app supports the following endpoints:

- `/recipes` - Gets all recipes
- `/recipe/<int:id>` - Gets a recipe by ID
- `/ingredients` - Gets all recipes
- `/ingredient/<int:id>` - Gets a recipe by ID

## Database

The application uses PostgreSQL as its database. To set up the database, create a PostgreSQL instance and set the DATABASE_URL environment variable to the connection string.

## Setup

1. Clone the repository:

```bash
git clone git@github.com:xenizs/python-api-no-framework.git
cd 
python-api-no-framework
```

2. Create Virtual env:

```python -m venv venv```

3. activate virtual env:

```source venv/bin/activate``` 

4. install dependencies

```pip install -r requirements.txt```

5. set the ```DATABASE_URL``` environment variable for the connection to a postgreSQL database.

6. run the migrations

```alembic upgrade head```

7. Start the application

```python main.py```

8. (optional, run with gunicorn)

```gunicorn wsgi:app```

## Running tests

Run all tests:

```python -m unittest discover -s tests -p "*.py"```

## Migration commands:

- Initialize migrations:  

```alembic init migrations```

- Make migrations

```alembic revision --autogenerate -m "Initial migration"```

- apply migrations: 

```alembic upgrade head```

## Seeding the database

```python seeders/recipe_seeder.py```

```python seeders/ingridient_seeder.py```