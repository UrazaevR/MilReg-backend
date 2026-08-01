from fastapi import APIRouter
from src.schemas import MenuResponse, MenuButton, MenuList

router = APIRouter(prefix="/api/menu", tags=["menu"])

@router.get("/", response_model=MenuResponse)
async def get_menu():
    menu_data = [
        MenuButton(
            id="home",
            title="Главная",
            icon="mdi-home",
            type="button",
            metaEndpoint="api/meta/home",
            dataEndpoint="api/home"
        ),
        MenuList(
            id="persons-root",
            title="Ведение учёта",
            icon="mdi-account-multiple-outline",
            type="list",
            children=[
                MenuButton(
                    id="persons-all",
                    title="Общий учёт",
                    type="button",
                    metaEndpoint="api/meta/persons",
                    dataEndpoint="api/persons"
                ),
                MenuButton(
                    id="staffing",
                    title="Учет часов",
                    type="button",
                    metaEndpoint="api/meta/staffing",
                    dataEndpoint="api/staffing"
                )
            ]
        )
    ]
    return MenuResponse(menu=menu_data)