from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetStudentSubjectsUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository
    
    def __call__(self, idStudent: int) -> List[Subject]:
        try:
            if idStudent is None:
                raise Exception('idStudent is None')

            subjects = self._subjectRepository.getStudentSubjects(idStudent)

            if len(subjects) == 0 or subjects is None:
                raise NoItemsFound('')

            return subjects

        except NoItemsFound:
            raise NoItemsFound('GetAllSubjects')

        except Exception as error:
            raise UnexpectedError('GetStudentSubject', str(error))
