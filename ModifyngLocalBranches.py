import requests
from git import Repo

localReport="/Users/cair/Documents/src/ubuy"
file="/Users/cair/Documents/src/ubuy/webapp/integration_testing/demofile.txt"

def adding_file():
    repo = Repo(localReport)
    actual_branch = repo.active_branch.name

    commit_message = 'new file deleted through automated Python code'
    repo.index.remove(file)
    repo.index.commit(commit_message)
    origin = repo.remote()
    origin.push()

if __name__ == "__main__":
    adding_file()






