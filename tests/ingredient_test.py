import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import unittest
from werkzeug.test import Client
from werkzeug.wrappers import Response
from app import get_app
from models import Ingredient
from config import Session
from sqlalchemy import select

class TestIntegration(unittest.TestCase):

    def setUp(self):
        with Session(expire_on_commit=False) as session:
            self.client = Client(get_app(), Response)
            self.ingridient = Ingredient(name="Integration Ingredient", measurement_unit='onz')
            session.add(self.ingridient)
            session.commit()

    def tearDown(self):
        with Session() as session:
            ingredient = session.scalars(select(Ingredient).where(Ingredient.id == self.ingridient.id)).first()
            session.delete(ingredient)
            session.commit()

    def test_get_ingridient(self):
        response = self.client.get(f'/ingredient/{self.ingridient.id}')
        self.assertEqual(response.status_code, 200)
        ingridient = response.json
        self.assertEqual(ingridient["name"], "Integration Ingredient")
        self.assertEqual(ingridient["measurement_unit"], "onz")

if __name__ == '__main__':
    unittest.main()
