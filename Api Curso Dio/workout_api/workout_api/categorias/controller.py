from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import Categoria, CategoriaOUT
from workout_api.contrib.depedencies import DatabaseDependency
from sqlalchemy.future import select


router = APIRouter()


@router.post('/', summary = 'Criar categoria',
             status_code = status.HTTP_201_CREATED,
             response_model = CategoriaOUT
             )
async def post(db_session: DatabaseDependency, categoria_in: Categoria= Body(...)) -> CategoriaOUT:
    categoriaout = CategoriaOUT(id = uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoriaout.model_dump())
    
    
    db_session.add(categoria_model)
    await db_session.commit()
    return categoriaout

@router.get('/', summary = 'Consultar todas categorias',
             status_code = status.HTTP_201_CREATED,
             response_model = list[CategoriaOUT]
             )

async def query(
    db_session: DatabaseDependency,
) -> list[CategoriaModel]:
    categorias: list[CategoriaOUT] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return categorias

@router.get('/{id}', summary = 'Consultar uma categoria',
             status_code = status.HTTP_201_CREATED,
             response_model = list[CategoriaOUT]
             )

async def query( id: UUID4,
    db_session: DatabaseDependency,
) -> list[CategoriaModel]:
    categoria: CategoriaOUT = (await db_session.execute(select(CategoriaModel).filter_by(id = id))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, details = f'Categoria não encontrada no id: {id}')
    
    return categoria
    
