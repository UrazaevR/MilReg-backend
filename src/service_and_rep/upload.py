import csv
import uuid
from io import StringIO
from typing import Any, Dict, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, inspect
from pydantic import ValidationError
from fastapi import HTTPException, status

from src.models import (
    Department, StaffingTable, Person, DriversLicense,
    EducationDoc, Language, Passport,
    OKATO, OIN_01, OIN_02, OIN_10, OIN_30, OKPDTR
)
from src.schemas import (
    DepartmentCreate, DepartmentUpdate,
    StaffingCreate, StaffingUpdate,
    PersonCreate, PersonUpdate,
    DriversLicenseCreate, DriversLicenseUpdate,
    EducationDocCreate, EducationDocUpdate,
    LanguageCreate, LanguageUpdate,
    PassportCreate, PassportUpdate,
    OIN_01Create, OIN_01Update,
    OIN_02Create, OIN_02Update,
    OIN_10Create, OIN_10Update,
    OIN_30Create, OIN_30Update,
    OKATOCreate, OKATOUpdate,
    OKPDTRCreate, OKPDTRUpdate,
)

ENTITY_MAP = {
    "departments": {
        "model": Department,
        "create_schema": DepartmentCreate,
        "update_schema": DepartmentUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "staffing": {
        "model": StaffingTable,
        "create_schema": StaffingCreate,
        "update_schema": StaffingUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "persons": {
        "model": Person,
        "create_schema": PersonCreate,
        "update_schema": PersonUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "drivers_licenses": {
        "model": DriversLicense,
        "create_schema": DriversLicenseCreate,
        "update_schema": DriversLicenseUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "education_docs": {
        "model": EducationDoc,
        "create_schema": EducationDocCreate,
        "update_schema": EducationDocUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "languages": {
        "model": Language,
        "create_schema": LanguageCreate,
        "update_schema": LanguageUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "passports": {
        "model": Passport,
        "create_schema": PassportCreate,
        "update_schema": PassportUpdate,
        "pk_field": "id",
        "pk_type": uuid.UUID,
    },
    "okin_01": {
        "model": OIN_01,
        "create_schema": OIN_01Create,
        "update_schema": OIN_01Update,
        "pk_field": "code",
        "pk_type": str,
    },
    "okin_02": {
        "model": OIN_02,
        "create_schema": OIN_02Create,
        "update_schema": OIN_02Update,
        "pk_field": "code",
        "pk_type": str,
    },
    "okin_10": {
        "model": OIN_10,
        "create_schema": OIN_10Create,
        "update_schema": OIN_10Update,
        "pk_field": "code",
        "pk_type": str,
    },
    "okin_30": {
        "model": OIN_30,
        "create_schema": OIN_30Create,
        "update_schema": OIN_30Update,
        "pk_field": "code",
        "pk_type": str,
    },
    "okato": {
        "model": OKATO,
        "create_schema": OKATOCreate,
        "update_schema": OKATOUpdate,
        "pk_field": "code",
        "pk_type": str,
    },
    "okpdtr": {
        "model": OKPDTR,
        "create_schema": OKPDTRCreate,
        "update_schema": OKPDTRUpdate,
        "pk_field": "code",
        "pk_type": str,
    },
}

async def process_csv_upload(
    db: AsyncSession,
    entity_name: str,
    file_content: bytes,
    mode: str = "create"
) -> Dict[str, Any]:
    if entity_name not in ENTITY_MAP:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown entity: {entity_name}. Allowed: {list(ENTITY_MAP.keys())}"
        )

    config = ENTITY_MAP[entity_name]
    model = config["model"]
    create_schema = config["create_schema"]
    update_schema = config["update_schema"]
    pk_field = config["pk_field"]
    pk_type = config["pk_type"]

    try:
        content = file_content.decode("utf-8-sig")
        reader = csv.DictReader(StringIO(content))
        rows = list(reader)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid CSV file: {str(e)}")

    if not rows:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CSV file is empty")

    created = 0
    updated = 0
    errors = []

    for row_num, row in enumerate(rows, start=2):
        try:
            clean_row = {k: v for k, v in row.items() if v and v.strip()}
            pk_value = clean_row.get(pk_field)

            existing = None
            if pk_value is not None:
                # Приводим к типу
                if pk_type == uuid.UUID:
                    try:
                        pk_value = uuid.UUID(pk_value)
                    except ValueError:
                        errors.append({
                            "row": row_num,
                            "error": f"Invalid UUID for field '{pk_field}'",
                            "data": row
                        })
                        continue
                # Ищем существующую запись
                stmt = select(model).where(getattr(model, pk_field) == pk_value)
                result = await db.execute(stmt)
                existing = result.scalar_one_or_none()

            if mode == "create":
                if existing:
                    errors.append({
                        "row": row_num,
                        "error": f"Record with {pk_field}={pk_value} already exists (mode=create)",
                        "data": row
                    })
                    continue
                validated = create_schema(**clean_row)
                data_dict = validated.model_dump()
                # Для UUID автогенерация происходит в модели (default=uuid.uuid4)
                instance = model(**data_dict)
                db.add(instance)
                created += 1

            elif mode == "upsert":
                if existing:
                    validated = update_schema(**clean_row)
                    update_data = validated.model_dump(exclude_unset=True)
                    update_data.pop(pk_field, None)  # не обновляем первичный ключ
                    for key, value in update_data.items():
                        setattr(existing, key, value)
                    db.add(existing)
                    updated += 1
                else:
                    validated = create_schema(**clean_row)
                    data_dict = validated.model_dump()
                    instance = model(**data_dict)
                    db.add(instance)
                    created += 1

        except ValidationError as e:
            errors.append({
                "row": row_num,
                "errors": e.errors(),
                "data": row
            })
        except Exception as e:
            errors.append({
                "row": row_num,
                "error": str(e),
                "data": row
            })

    if errors:
        await db.rollback()
        return {
            "status": "error",
            "created": 0,
            "updated": 0,
            "errors": errors
        }
    else:
        await db.commit()
        return {
            "status": "success",
            "created": created,
            "updated": updated,
            "errors": []
        }