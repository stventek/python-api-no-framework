from typing import Optional
from sqlalchemy import String
from config import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__  = 'recipes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]]
    instructions: Mapped[Optional[str]]

    # many-to-many relationship to Ingredient, bypassing the `AssociationIngredientRecipe` class
    ingredients: Mapped[List["Ingredient"]] = relationship(
        secondary="association_ingredient_recipe", back_populates="recipes", viewonly=True)
    
    # association between Recipe -> AssociationIngredientRecipe -> Ingridient
    ingridient_associations: Mapped[List["AssociationIngredientRecipe"]] = relationship(
        back_populates="recipe"
    )

    def __repr__(self):
        return self.id