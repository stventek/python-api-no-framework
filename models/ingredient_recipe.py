from __future__ import annotations
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from config import Base
from typing import Optional
from config import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class AssociationIngredientRecipe(Base):
    __tablename__ = "association_ingredient_recipe"
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id"), primary_key=True)
    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipes.id"), primary_key=True
    )
    quantity: Mapped[Optional[str]]
    # association between Assocation -> Recipe
    recipe: Mapped["Recipe"] = relationship(back_populates="ingridient_associations")
    # association between Assocation -> Ingredient
    ingridient: Mapped["Ingredient"] = relationship(back_populates="recipe_associations")
