from pydantic import BaseModel
from typing import Optional, Union

class MenuBase(BaseModel):
    id: str
    title: str
    icon: Optional[str | None] = None
    type: str

class MenuButton(MenuBase):
    metaEndpoint: str
    dataEndpoint: str

class MenuList(MenuBase):
    children: list[Union["MenuButton", "MenuList"]]

class MenuResponse(BaseModel):
    menu: list[Union[MenuButton, MenuList]]

    class Config:
        from_attributes = True

