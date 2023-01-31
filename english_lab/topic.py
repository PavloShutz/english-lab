from .instances import database


class Topic(database.Model):
    """Topic that can be created by admin."""
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(255), nullable=False)
    body = database.Column(database.Text, nullable=False)
