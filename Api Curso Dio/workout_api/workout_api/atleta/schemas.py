from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categorias.schemas import Categoria
from workout_api.centro_de_treinamento.schemas import CentroDeTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchemas, OutMixin



class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome do atleta', examples = ['João'], max_lenght = 50)]
    cpf: Annotated[str, Field(description = 'CPF do atleta', examples = ['11223344500'], max_lenght = 11)]
    idade: Annotated[int, Field(description = 'Idade do atleta', examples = ['23'])]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do atleta', examples = ['84.2'])]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do Atleta', examples = ['1.86'])]
    sexo: Annotated[str, Field (description = 'Sexo do atleta', examples = ['M'], max_length = 1)]
    categoria: Annotated[Categoria, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroDeTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIN(Atleta):
    pass



class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example=['Joao'], max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]