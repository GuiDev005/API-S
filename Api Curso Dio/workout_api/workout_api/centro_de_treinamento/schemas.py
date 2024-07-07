from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchemas


class CentroDeTreinamento(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome do centro de treinamento', examples = ['Treino Pesado'], max_lenght = 20)]
    endereco: Annotated[str, Field(description = 'Endereço do centro de treinamento', examples = ['Rua Emanuel Cardoso, 429 - 57283670'], max_lenght = 60)]
    proprietario: Annotated[str, Field(description = 'Nome do proprietario do centro de treinamento', examples = ['Guilherme'], max_lenght = 30)]


class CentroDeTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome do centro de treinamento', examples = ['Treino Pesado'], max_lenght = 20)]


class CentroDeTreinamentoOUT(CentroDeTreinamento):
    id: Annotated [UUID4, Field(description = 'Identificador do centro de treinamento')]