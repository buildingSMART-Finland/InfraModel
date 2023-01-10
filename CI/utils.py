import subprocess
import datetime

def get_git_branch_name():
    """ get the current branch name """
    return subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).rstrip().decode("utf-8")

def get_git_branch_head_SHA1():
    """ get the HEAD commit hash """
    return subprocess.check_output("git rev-parse HEAD", shell=True).rstrip().decode("utf-8")[0:8]

def get_doc_version():
    return "**branch** %s **sha** %s **at** %s" % (
        get_git_branch_name(),
        get_git_branch_head_SHA1(),
        datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    print(get_git_branch_name())
    print(get_git_branch_head_SHA1())
    print(datetime.datetime.utcnow())
    print(get_doc_version())
