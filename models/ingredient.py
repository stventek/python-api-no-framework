from typing import List, Optional
from sqlalchemy import String
from config import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Ingredient(Base):
    __tablename__  = 'ingredients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    measurement_unit: Mapped[str] = mapped_column(String(30))
    
    # many-to-many relationship to Recipe, bypassing the `AssociationIngredientRecipe` class
    recipes: Mapped[List["Recipe"]] = relationship(
        secondary="association_ingredient_recipe", back_populates="ingredients", viewonly=True)
    
    # association between Ingridient -> AssociationIngredientRecipe -> Recipe
    recipe_associations: Mapped[List["AssociationIngredientRecipe"]] = relationship(
        back_populates="ingridient"
    )
    
    def __repr__(self):
        return self.id