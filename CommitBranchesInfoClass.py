from datetime import timedelta, date
from git import Repo

localRepo="/Users/cair/Documents/src/ubuy"
COMMITS_TO_PRINT = 2
COMMIT_DATE = str(date.today() - timedelta(days=1))
repo = Repo(localRepo)

class CommitInfo:
    def __init__(self):
        self.repo = repo

    def get_list_from_commit_data(self, commits):
        for commit in commits:
            commitValues = [commit.summary, commit.message, str(commit.hexsha), commit.author.name, commit.author.email, commit.authored_datetime]
        return commitValues

    def print_repository_info(self):
        print("-----Repo Summary-----")
        print('Repository description : {}'.format(self.repo.description))
        print('Repository active branch : {}'.format(self.repo.active_branch))

        for remote in self.repo.remotes:
            print('Remote named : "{}" with URL : "{}"'.format(remote, remote.url))

        print('Last commit for repository : {}.'.format(str(self.repo.head.commit.hexsha)))

    def validate_repo(self):
        if not self.repo.bare:
            #repo_path = os.getenv('ENV-VAR') we can set our repo path as env variable that way we can query from any place
            print('Repo at {} successfully loaded.'.format(localRepo))
            self.print_repository_info()
            # this filter is optional we can limit the number of elements we want to query doing [:10] minium only last 10 commits from the list
            commits = list(self.repo.iter_commits(self.repo.active_branch))[:COMMITS_TO_PRINT]
            commits3 = self.get_list_from_commit_data(commits)
            print(commits3)
        else:
            print('Could not load repository at {} :'.format(localRepo))

ci = CommitInfo()

ci.validate_repo()

