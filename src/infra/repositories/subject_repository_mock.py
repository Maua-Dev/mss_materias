from typing import List, Tuple

from src.domain.entities.degree import Degree
from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.entities.student import Student
from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.domain.enums.period import PERIOD
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class SubjectRepositoryMock(ISubjectRepository):

    students: List[Student]
    subjects: List[Subject]
    degrees: List[Degree]

    def __init__(self):
        self.subjects = [
            Subject(
                name="Engenharia de Software",
                code="ECM231",
                degreeCode=DegreeEnum.ECM,
                year=2022,
                academicYear=YEAR._4,
                semester=SEMESTER.AN,
                situation=SITUATION.IN_PROGRESS,
                grades=[
                    Grade(
                        value= 8.5,
                        evaluationType= EVALUATION_TYPE.P1,
                        weight= 0.1,
                    ),
                    Grade(
                        value=4.0,
                        evaluationType=EVALUATION_TYPE.P2,
                        weight=0.1,
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.P3,
                        weight=0.2
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.P4,
                        weight=0.2
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T1,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T2,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T3,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T4,
                        weight=0.1
                    )
                ],
                professor=Professor(
                    name="Ana Paula Gonçalves Serra",
                    email="ana.serra@maua.br",
                    phoneNumber="4239-3008"),
                coordinator=Professor(
                    name="Angelo Sebastiao Zanini",
                    email="angelo.zanini@maua.br",
                    phoneNumber="4239-3009"
                )
            ),
            Subject(
                name="Banco de Dados",
                code="ECM401",
                degreeCode=DegreeEnum.ECM,
                year=2022,
                academicYear=YEAR._4,
                semester=SEMESTER.AN,
                situation=SITUATION.IN_PROGRESS,
                grades=[
                    Grade(
                        value=3.0,
                        evaluationType=EVALUATION_TYPE.P1,
                        weight=0.2,
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.P2,
                        weight=0.4,
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T1,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T2,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T3,
                        weight=0.1
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.T4,
                        weight=0.1
                    )
                ],
                professor=Professor(
                    name="Aparecido Valdemir de Freitas",
                    email="aparecido.freitas@maua.br",
                    phoneNumber="4239-3009"
                ),
                coordinator=Professor(
                    name="Angelo Sebastiao Zanini",
                    email="angelo.zanini@maua.br",
                    phoneNumber="4239-3009"
                )
            )
        ]

        self.degrees = [
            Degree(
                name="Engenharia de Computação",
                code="ECM",
                subjects=self.subjects,
                coordinator=Professor(
                    name="Angelo Sebastiao Zanini",
                    email="angelo.zanini@maua.br",
                    phoneNumber="4239-3009"
                ),
            )
        ]

        self.students = [
            Student(
                name="Bruno Vilardi",
                ra="19003315",
                email="bruno@bruno.com",
                password="Teste123!",
                degreeCode=DegreeEnum.ECM,
                academicYear=YEAR._4,
                subjects=self.subjects,
                period=PERIOD.DAY,
                photo="https://drive.google.com/uc?export=view&id=1IKIyM5G5jivSx0y7YLnZ-XWD-QvnQ5AC"
            )
        ]

    async def get_all_subjects(self) -> List[Subject]:
        return self.subjects

    async def get_subjects_by_student(self, ra: str) -> List[Subject]:
        for student in self.students:
            if ra == student.ra:
                return student.subjects
        return None

    async def get_subject(self, ra: str, code: str) -> Subject:
        subjects = await self.get_subjects_by_student(ra=ra)
        if subjects == None:
            return None
        for subject in subjects:
            if subject.code == code:
                return subject
        return None