from models.political_party import PoliticalParty
from repositories.political_party_repository import Political_Party_Repository


class PoliticalPartyController:
    def __init__(self):
        """
        Constructor of the class
        """
        print("Political party controller ready...")
        self.political_repository = Political_Party_Repository()

    def index(self) -> list:
        """
        get ALL political party
        :return:
        """
        print("Get all")
        return self.political_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id_")
        return self.political_repository.find_by_id(id_)

    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """
        print("Insert ONE political party")
        political = PoliticalParty(political_party_)
        return self.political_repository.save(political)

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("Update ONE political_party")
        political = PoliticalParty(political_party_)
        return self.political_repository.update(id_, political)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete ONE political party")
        return self.political_repository.delete(id_)
