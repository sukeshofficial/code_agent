from git import Repo
import os

def commit_and_push(commit_message, repo_path, remote_name='origin', branch='main'):
    repo = Repo(repo_path)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name=remote_name)
    origin.push(origin.push(refspec=f"{branch}:{branch}"))