from models.vote import Vote
from repositories.vote_file import VoteRepository


class VoteController:
    def __init__(self):
        """
        Constructor of the class
        """
        print("Vote controller ready...")
        self.vote_repository = VoteRepository

    def index(self) -> list:
        """
        get ALL vote
        :return:
        """
        print("Get all")
        return self.vote_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id_")
        return self.vote_repository.find_by_id(id_)

    def create(self, vote_: dict) -> dict:
        """

        :param vote_:
        :return:
        """
        print("Insert ONE vote")
        vote = Vote(vote_)
        return self.vote_repository.save(vote)

    def update(self, id_: str, vote_: dict) -> dict:
        """
        UPDATE ONE vote by ID
        :param id_:
        :param vote_:
        :return:
        """
        print("Update ONE vote")
        vote = Vote(vote_)
        return self.vote_repository.update(id_, vote)


