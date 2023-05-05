import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import Session
from models import Recipe

def seed_recipes():
    recipes = [
        Recipe(name="Recipe 1"),
        Recipe(name="Recipe 2"),
        Recipe(name="Recipe 3"),
    ]
    with Session() as session:
        session.add_all(recipes)
        session.commit()

if __name__ == "__main__":
    seed_recipes()
