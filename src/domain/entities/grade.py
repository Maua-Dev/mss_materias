from typing import List
from pydantic.class_validators import validator
from pydantic.main import BaseModel

from src.domain.errors.errors import EntityError

from src.domain.entities.subject import Subject

class Grade(BaseModel):
    value: float
    idGrade: int

    @validator('value')
    def value_is_not_empty(cls, v: float) -> float:
        if v < 0:
            raise EntityError('Value')
        return v

    @validator('idGrade')
    def idGrade_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('idGrade')
        return v

"""class Degree(BaseModel):
    name: str
    subjects: List[Subject]
    duration: int
    idDegree: int

    @validator('name')
    def name_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v

    @validator('duration')
    def duration_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('duration')
        return v

    @validator('subjects')
    def subjects_not_empty(cls, v: List[Subject]) -> List[Subject]:
        if len(v) == 0:
            raise EntityError('Subjects')
        return v

    @validator('idDegree')
    def idDegree_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('idDegree')
        return v"""
