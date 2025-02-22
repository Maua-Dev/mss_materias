from typing import List

from pydantic import validator, BaseModel

from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR
from src.helpers.errors.domain_errors import EntityError


class Subject(BaseModel):
    name: str
    code: str
    year: int
    academicYear: YEAR
    degreeCode: DegreeEnum
    semester: SEMESTER
    situation: SITUATION
    grades: List[Grade]
    professor: Professor
    coordinator: Professor

    @validator('name')
    def name_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('name')
        return v

    @validator('code')
    def codeSubject_is_not_empty(cls,v: str)-> str:
        if len(v) == 0:
            raise EntityError('code')
        return v

    @validator('year')
    def year_makes_sense(cls,v: int) -> int:
        minimal = 1961
        maximum = 2100
        if v < minimal or v > maximum:
            raise EntityError(f"Year is not valid - should be between {minimal} and {maximum}")
        return v

    @validator('academicYear')
    def academicYear_is_not_empty(cls,v: YEAR) -> YEAR:
        if v is None:
            raise EntityError("academicYear")
        return v

    @validator('semester')
    def semester_is_valid(cls,v: SEMESTER) -> SEMESTER:
        if v is None:
            raise EntityError('semester')
        return v

    @validator('situation')
    def situation_is_valid(cls,v: SITUATION) -> SITUATION:
        if v is None:
            raise EntityError('situation')
        return v

    @validator('professor')
    def professor_is_valid(cls,v: Professor) -> Professor:
        if v is None:
            raise EntityError('professor')
        return v

    @validator('coordinator')
    def coordinator_is_valid(cls,v: Professor) -> Professor:
        if v is None:
            raise EntityError('coordinator')
        return v

    @staticmethod
    def getCurrentGrade(self) -> float:
        current_grade = 0
        for grade in self.grades:
            if grade.value != None:  # se for None, eu somaria à current_grade 0
                current_grade += grade.value * grade.weight

        return current_grade

    @staticmethod
    def getPartialGrade(self) -> float:
        partial_grade = 0
        partial_weight = 0
        for grade in self.grades:
            if grade.value != None:
                partial_grade += grade.value * grade.weight
                partial_weight += grade.weight

        return partial_grade / partial_weight
