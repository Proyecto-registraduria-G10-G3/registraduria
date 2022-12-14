from models.table import Table
from repositories.table_party import TableRepository


class TableController:
    def __init__(self):
        """
        Constructor of the class
        """
        print("Table controller ready...")
        self.table_repository = TableRepository()

    def index(self) -> list:
        """
        get ALL table
        :return:
        """
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id_")
        return self.table_repository.find_by_id(id_)

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert ONE table")
        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update ONE table")
        table = Table(table_)
        return self.table_repository.update(id_, table)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete ONE table")
        return self.table_repository.delete(id_)
