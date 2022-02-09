from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest, NoContent, BadRequest
from src.domain.entities.subject import Subject

class Test_GetSubjectByCodeController:

    def test_get_subject_by_code_controller(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 'ecm505'})
        answer = getSubjectByCodeController(req)
        
        assert type(answer.body) is Subject        
        assert answer.status_code == 200

    def test_get_subject_by_code_controller_no_item_found(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 'esm505'})
        answer = getSubjectByCodeController(req)

        assert type(answer) is NoContent
        assert answer.status_code == 204

    def test_get_subject_by_code_controller_error(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 2})
        answer = getSubjectByCodeController(req)

        assert type(answer) is BadRequest
        assert answer.status_code == 400
