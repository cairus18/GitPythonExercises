from datetime import timedelta, date
from git import Repo
import json

localRepo = "/Users/cair/Documents/src/ubuy"
COMMIT_DATE = str(date.today() - timedelta(days=0))

repo = Repo(localRepo)

# repo = Repo.remote(remoteRepo)

def print_commit_data(commit):
    print('-----')
    print("Commit Description : {}".format(commit.summary))
    print("Commit Message : {}".format(commit.message))
    print("Commit Number : " + str(commit.hexsha))
    print("By : {}".format(commit.author.name))
    print("Email : {}".format(commit.author.email))
    print("Commit Date Time :" + str(commit.authored_datetime))
    commitJson = {
        "CommitDescription":commit.summary,
        "CommitMessage":commit.message,
        "CommitNumber":str(commit.hexsha),
        "By":commit.author.name,
        "Email":commit.author.email,
        "CommitDateTime":str(commit.authored_datetime)
    }
    generateJsonFile(commitJson)

def generateJsonFile(commitDict):
    commitDict = json.dumps(commitDict, indent=4)
    with open("commitsDay_" + str(date.today()) + ".json", "w") as outfile:
        outfile.write(commitDict)

def files_diff(currentCommit, previousCommit):
    currentCommit = repo.commit('0405206f2777e110c09fbbbfa4c26c83a47e35a0')
    previousCommit = repo.commit('cb446e59217ce7c42358bdfa0e181f333099a29f')

    diff_index = previousCommit.diff(currentCommit)
    for diff in diff_index:
        print(diff.change_type)
        print("{} -> {}".format(diff.a_path, diff.b_path))


def main():
    if not repo.bare:
        commits = list(repo.iter_commits(repo.active_branch))
        for commit in commits:
            if date.fromtimestamp(commit.committed_date).strftime('%Y-%m-%d') == COMMIT_DATE:
                print_commit_data(commit)
        pass
    else:
        print('Could not load repository at {} :'.format(localRepo))


if __name__ == "__main__":
    main()
