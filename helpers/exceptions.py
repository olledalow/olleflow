from typing import Any


class ItemNotFoundError(Exception):
    def __init__(self, db_obj_name: str, id: Any):
        Exception.__init__(self)
        self.db_obj_name = db_obj_name
        self.id = str(id)
        self.message = "Nincs találat"
        self.error = f"{db_obj_name} with id: {str(id)} not found"
