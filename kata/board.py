class Board:
    def __init__(self, title, is_public=True, columns=[]):
        self.title = title
        self.is_public = None
        self.tags = []
        self._columns = columns

    @property
    def columns(self):
        return self._columns
