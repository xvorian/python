from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"
    OTHER = "other"


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    STUDENT = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: Role


class Employee(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: Role
