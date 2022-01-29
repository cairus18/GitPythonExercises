import os
import shutil
from datetime import timedelta, date
from git import Repo

# to query a remote repo instead of local
#remoteRepo="https://github.com/craigstockton-tgs/ubuy.git"
localRepo="/Users/cair/Documents/src/ubuy"
COMMITS_TO_PRINT = 5
COMMIT_DATE = str(date.today() - timedelta(days=1))

'''
if os.path.exists(localRepo):
    shutil.rmtree(localRepo)

repo = Repo.clone_from(remoteRepo, localRepo)
'''
repo = Repo(localRepo)
#repo = Repo.remote(remoteRepo)

def print_commit_data(commit):
    print('-----')
    print("Commit Description : {}".format(commit.summary))
    print("Commit Message : {}".format(commit.message))
    print("Commit Number : " + str(commit.hexsha))
    print("By : {}".format(commit.author.name))
    print("Email : {}".format(commit.author.email))
    print("Commit Date Time :"+str(commit.authored_datetime))

def print_repository_info(repo):
    print("-----Repo Summary-----")
    print('Repository description : {}'.format(repo.description))
    print('Repository active branch : {}'.format(repo.active_branch))

    for remote in repo.remotes:
        print('Remote named : "{}" with URL : "{}"'.format(remote, remote.url))

    print('Last commit for repository : {}.'.format(str(repo.head.commit.hexsha)))

def main():
    if not repo.bare:
        #repo_path = os.getenv('ENV-VAR') we can set our repo path as env variable that way we can query from any place
        print('Repo at {} successfully loaded.'.format(localRepo))
        print_repository_info(repo)
        # this filter is optional we can limit the number of elements we want to query doing [:10] minium only last 10 commits from the list
        commits = list(repo.iter_commits(repo.active_branch))
        for commit in commits:
            #Limiting the days we want to see in the commits filtering by minus how many days
            if date.fromtimestamp(commit.committed_date).strftime('%Y-%m-%d') == COMMIT_DATE:
                print_commit_data(commit)
        pass
    else:
        print('Could not load repository at {} :'.format(localRepo))

if __name__ == "__main__":
    main()

