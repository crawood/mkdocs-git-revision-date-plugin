from git import Git

class Util:

    def __init__(self):
        self.g = Git()

    def get_revision_date_for_file(self, path: str):
        date_commit = self.g.log(path, n=1, date='short', format='%ad')
        date_merge = self.g.log(path, '-1', '--min-parents=2', '--format=%ad', '--date=short')
        
        if(date_commit > date_merge):
            return date_commit
        else:
            return date_merge
