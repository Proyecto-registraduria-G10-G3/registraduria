from models.candidate import Candidate
from repositories.candidate_repository import CandidateRepository


class CandidateController:

    def __init__(self):
        """
        Constructor of the class
        """
        print("Candidate controller ready...")
        self.candidate_repository = CandidateRepository

    def index(self) -> list:
        """
        get ALL candidates
        :return:
        """
        print("Get all")
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id_")
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("Insert ONE candidate")
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("Update ONE candidate")
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)


    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete ONE candidate")
        return self.candidate_repository.delete(id_)
