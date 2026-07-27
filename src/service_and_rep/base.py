from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import TypeVar, Generic, Type, Optional, List, Dict, Any
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def get_all(self) -> List[ModelType]:
        result = await self.db.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, obj_id: int) -> Optional[ModelType]:
        result = await self.db.execute(select(self.model).where(self.model.id == obj_id))
        return result.scalar_one_or_none()

    async def create(self, data: CreateSchemaType) -> ModelType:
        instance = self.model(**data.model_dump())
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def update(self, obj_id: int, data: UpdateSchemaType) -> Optional[ModelType]:
        instance = await self.get_by_id(obj_id)
        if not instance:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(instance, key, value)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def delete(self, obj_id: int) -> bool:
        instance = await self.get_by_id(obj_id)
        if not instance:
            return False
        await self.db.delete(instance)
        await self.db.commit()
        return True