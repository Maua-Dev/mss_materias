from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetAllSubjectsUsecase:

    def __init__(self, subjectRepository: ISubjectRepository):
        self._subjectRepository = subjectRepository

    def __call__(self):
        try:
            subjects = self._subjectRepository.getAllSubjects()

            if len(subjects) == 0 or subjects is None:
                raise NoItemsFound('')

            return subjects

        except NoItemsFound:
            raise NoItemsFound('GetAllSubjects')

        except Exception as error:
            raise UnexpectedError('GetAllSubjects', str(error))


