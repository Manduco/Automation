from git import Repo

def git_push():

    repo = Repo('')  # if repo is CWD just do '.'

    repo.index.add(['file.txt'])
    repo.index.commit('Auto test description')
    origin = repo.remote('origin')
    origin.push()
    print("pushing to repo")

git_push()