import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import unittest
from werkzeug.test import Client
from werkzeug.wrappers import Response
from app import get_app
from models import Recipe
from config import Session
from sqlalchemy import select

class TestIntegration(unittest.TestCase):

    def setUp(self):
        with Session(expire_on_commit=False) as session:
            self.client = Client(get_app(), Response)
            self.recipe = Recipe(name="Integration test Recipe")
            session.add(self.recipe)
            session.commit()

    def tearDown(self):
        with Session() as session:
            recipe = session.scalars(select(Recipe).where(Recipe.id == self.recipe.id)).first()
            session.delete(recipe)
            session.commit()

    def test_get_recipe(self):
        response = self.client.get(f'/recipe/{self.recipe.id}')
        self.assertEqual(response.status_code, 200)
        recipe = response.json
        self.assertEqual(recipe["name"], "Integration test Recipe")

if __name__ == '__main__':
    unittest.main()
