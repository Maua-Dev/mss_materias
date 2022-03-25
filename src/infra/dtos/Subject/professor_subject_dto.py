from sqlalchemy import Column, ForeignKey, Integer
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class ProfessorSubjectDTO(Base):
    __tablename__ = 'ProfessorSubjects'

    id = Column(Integer, primary_key=True)
    idProfessor = Column(Integer, nullable=False)
    idSubject = Column(Integer, ForeignKey('Subjects.id'))

    def getId(self) -> int:
        return self.id

    def getIdProfessor(self) -> int:
        return self.idProfessor

    def getIdSubject(self) -> int:
        return self.idSubject