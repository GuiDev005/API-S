from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchemas


class Categoria(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome da categoria', examples = ['Scale'], max_lenght = 10)]



class CategoriaOUT(Categoria):
    id: Annotated [UUID4, Field(description = 'Identificador da categoria')]