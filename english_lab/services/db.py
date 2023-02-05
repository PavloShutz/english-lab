"""Module for working with database."""


from english_lab.instances import database


def add_new_object_to_db(obj) -> None:
    """Add new model to the database."""
    database.session.add(obj)
    database.session.commit()
