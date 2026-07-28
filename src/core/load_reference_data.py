import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.okato import OKATO
from src.models.okin_01 import OIN_01
from src.models.okin_02 import OIN_02
from src.models.okin_10 import OIN_10
from src.models.okin_30 import OIN_30
from src.models.okpdtr import OKPDTR


# --- Загрузка ОКАТО ---
async def load_okato(db: AsyncSession, json_path: str):
    result = await db.execute(select(OKATO))
    if result.scalars().first():
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get("data", {}).get("records", [])
    okato_list = []

    for rec in records:
        attrs = {item["attributeUid"]: item["value"] for item in rec["attributeValues"]}
        code = attrs.get("4963c57c-c5fb-43b3-bdda-fa8ff13c0a81")
        name = attrs.get("0e9efca0-bd54-4de0-b694-af6a5f381c9c")
        autokey = attrs.get("5fde107c-2a42-45e3-865a-f6970bbe43e1")
        if code and name and autokey:
            okato_list.append(OKATO(code=code, name=name, autokey=autokey))

    if okato_list:
        db.add_all(okato_list)
        await db.commit()


# --- Загрузка единого справочника ОКИН (все фасеты) ---
async def load_okin(db: AsyncSession, json_path: str):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get("data", {}).get("records", [])
    facet_uid = "788f82f5-c8d3-4e72-8fd3-ede5eecda9af"
    code_uid = "5cf5390d-f22f-4a79-b957-64e7f011f645"
    name_uid = "4111ec8f-34ac-4563-8077-151c4e42a661"
    autokey_uid = "8f6d0dd9-59e5-460c-aa56-8715707113f3"

    okin_01_list = []
    okin_02_list = []
    okin_10_list = []
    okin_30_list = []

    for rec in records:
        attrs = {item["attributeUid"]: item["value"] for item in rec["attributeValues"]}
        facet = attrs.get(facet_uid)
        code = attrs.get(code_uid)
        name = attrs.get(name_uid)
        autokey = attrs.get(autokey_uid)

        if not facet or not autokey:
            continue

        if facet == "001":
            okin_01_list.append(OIN_01(code=code, name=name, autokey=autokey))
        elif facet == "002":
            okin_02_list.append(OIN_02(code=code, name=name, autokey=autokey))
        elif facet == "010":
            okin_10_list.append(OIN_10(code=code, name=name, autokey=autokey))
        elif facet == "030":
            okin_30_list.append(OIN_30(code=code, name=name, autokey=autokey))

    # Проверяем каждую таблицу отдельно
    if okin_01_list:
        result = await db.execute(select(OIN_01))
        if not result.scalars().first():
            db.add_all(okin_01_list)

    if okin_02_list:
        result = await db.execute(select(OIN_02))
        if not result.scalars().first():
            db.add_all(okin_02_list)

    if okin_10_list:
        result = await db.execute(select(OIN_10))
        if not result.scalars().first():
            db.add_all(okin_10_list)

    if okin_30_list:
        result = await db.execute(select(OIN_30))
        if not result.scalars().first():
            db.add_all(okin_30_list)

    await db.commit()


# --- Загрузка ОКПДТР ---
async def load_okpdtr(db: AsyncSession, json_path: str):
    result = await db.execute(select(OKPDTR))
    if result.scalars().first():
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get("data", {}).get("records", [])
    okpdtr_list = []

    for rec in records:
        attrs = {item["attributeUid"]: item["value"] for item in rec["attributeValues"]}
        code = attrs.get("48512cd1-0900-4389-8c35-b076f7298818")
        kch = attrs.get("e6017388-d254-4d88-828c-f544b51f1faf")
        profession_name = attrs.get("ac565da8-34f3-4c35-999b-50cc39e67e84")
        job_name = attrs.get("bdfc70ec-6681-4bd5-97ee-be97449c672f")
        code_category = attrs.get("e1ed6087-835a-4cfa-9351-12999235a8db")
        code_etks = attrs.get("9ac44b1e-04ec-4a46-93d7-7d907ab58b25")
        code_okz = attrs.get("09e942e3-9e9c-4e06-affe-918e96c42b9c")
        autokey = attrs.get("43af857e-7a53-487c-876c-a5afc4e26b27")

        if code and autokey:
            okpdtr_list.append(OKPDTR(
                code=code,
                kch=kch,
                profession_name=profession_name,
                job_name=job_name,
                code_category=code_category,
                code_etks=code_etks,
                code_okz=code_okz,
                autokey=autokey
            ))

    if okpdtr_list:
        db.add_all(okpdtr_list)
        await db.commit()