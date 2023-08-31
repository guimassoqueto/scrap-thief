from pydantic import BaseModel
from datetime import datetime
from typing import Any, List, Optional


class Store(BaseModel):
    logo: str
    name: str
    slug: str
    url: str


class User(BaseModel):
    username: str
    image: str


class Category(BaseModel):
    name: str


class Subcategory(BaseModel):
    category: Category


class Item(BaseModel):
    id: Optional[int]
    store: Optional[Store]
    freight: Optional[str]
    warning: Optional[str]
    user_fake: Optional[User]
    user: Optional[User]
    subcategory: Optional[Subcategory]
    form_payment: Optional[str]
    total_comment: Optional[int]
    created_at: Optional[datetime]
    saved: Optional[List[Any]]
    title: Optional[str]
    slug: Optional[str]
    general_description: Optional[str]
    old_price: Optional[float]
    price: Optional[float]
    image: Optional[str]
    image_gif: Optional[str]
    image_real: Optional[str]
    image_real: Optional[str]
    image_insta: Optional[Any]
    image_four_promotion: Optional[Any]
    status: Optional[str]
    long_url: Optional[str]
    short_url: Optional[str]
    coupon: Optional[Any]
    warning_temp: Optional[Any]
    ame: Optional[bool]
    ame_attribute: Optional[Any]
    is_any_text_price: Optional[bool]
    any_text_price: Optional[Any]
    relevant: Optional[bool]
    exclusive: Optional[bool]
    call_app: Optional[bool]
    lowest_price: Optional[bool]
    whatsapp: Optional[bool]
    telegram: Optional[bool]
    instagram: Optional[bool]
    instagram_relevant: Optional[bool]
    facebook: Optional[bool]
    friend_pechinchou: Optional[bool]
    community: Optional[bool]
    treated_title: Optional[str]
    is_image_social: Optional[bool]
    resize_image_tam: Optional[str]
    alertcomment: Optional[int]
    likes: Optional[List[int]]