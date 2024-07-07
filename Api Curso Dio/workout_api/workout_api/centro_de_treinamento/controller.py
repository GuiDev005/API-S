from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.centro_de_treinamento.models import CentroDeTreinamentoModel
from workout_api.centro_de_treinamento.schemas import CentroDeTreinamento, CentroDeTreinamentoOUT
from workout_api.contrib.depedencies import DatabaseDependency
from sqlalchemy.future import select


router = APIRouter()


@router.post('/', summary = 'Criar novo centro de treinamento',
             status_code = status.HTTP_201_CREATED,
             response_model = CentroDeTreinamentoOUT
             )
async def post(db_session: DatabaseDependency, centrodetreinamento_in: CentroDeTreinamento= Body(...)) -> CentroDeTreinamentoOUT:
    centros_de_treinamento = CentroDeTreinamentoOUT(id=uuid4(), **centrodetreinamento_in.model_dump())
    centrodetreinamento_model = CentroDeTreinamentoModel(**centrodetreinamento_model.model_dump())
    
    
    db_session.add(centrodetreinamento_model)
    await db_session.commit()
    return centros_de_treinamento

@router.get('/', summary = 'Consultar todos centros de treinamento',
             status_code = status.HTTP_201_CREATED,
             response_model = list[CentroDeTreinamentoOUT]
             )

async def query(
    db_session: DatabaseDependency,
) -> list[CentroDeTreinamentoModel]:
    centros_de_treinamento: list[CentroDeTreinamentoOUT] = (await db_session.execute(select(CentroDeTreinamentoModel))).scalars().all()
    return centros_de_treinamento

@router.get('/{id}', summary = 'Consultar um centro de treinamento',
             status_code = status.HTTP_201_CREATED,
             response_model = list[CentroDeTreinamentoOUT]
             )

async def query( id: UUID4,
    db_session: DatabaseDependency,
) -> list[CentroDeTreinamentoModel]:
    centros_de_treinamento: CentroDeTreinamentoOUT = (await db_session.execute(select(CentroDeTreinamentoModel).filter_by(id = id))).scalars().first()
    
    if not centros_de_treinamento:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, details = f'Centro de treinamento não encontrado no id: {id}')
    
    return centros_de_treinamento
    
