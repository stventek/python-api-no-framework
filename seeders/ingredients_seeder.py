import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models import Recipe
from config import Session
from sqlalchemy import select
from models import Ingredient
from models import AssociationIngredientRecipe

def seed_ingredients():
    with Session() as session:
        recipes = session.scalars(select(Recipe)).all()
        for recipe in recipes:
            for i in range(1, 4):
                ingredient = Ingredient(
                    name=f'Ingrdient {i}',
                    measurement_unit='onz'
                )
                association = AssociationIngredientRecipe(quantity="10")
                association.recipe = recipe
                ingredient.recipe_associations.append(association)
                session.add(ingredient)
        session.commit()

if __name__ == "__main__":
    seed_ingredients()
