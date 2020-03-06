from git import Git

class Util:

    def __init__(self):
        self.g = Git()

    def get_revision_date_for_file(self, path: str):
        date_merge = self.g.log(path, '--min-parents'=2, 'n'=1, 'date'='short', 'format'='%ad')
        return date_merge
