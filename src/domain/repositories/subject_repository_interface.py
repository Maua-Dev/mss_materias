from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC):

    @abstractmethod
    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:    
        pass
    @abstractmethod
    def getSubjectStudents(self, codeSubject: str) -> tuple:
        pass

    @abstractmethod
    def getAllSubjects(self) -> tuple:
        pass

    @abstractmethod
    async def getSubjectByCode(self, codeSubject: str) -> Subject:
        pass

    @abstractmethod
    def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        pass