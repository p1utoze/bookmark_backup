from datetime import datetime
import os
import subprocess
import json
def bookmark_dict():
    with open(__full_path, "r") as f:
        return json.load(f)

book_dict = dict()
_user = subprocess.check_output("whoami", shell=True).decode().strip()
_path = "/home/{0}/.config/".format(_user)
_path_len = _path.split('/').__len__()


def getpath(path):
    for paths, dirs, files in os.walk(path):
        if paths.split('/').__len__() == _path_len and os.path.basename(paths).startswith("Brave"):
            path = paths
            break
    return path


def bookmark_search(path: str)-> str:
    path = getpath(path)
    _cmd = 'find {0} -name "Book*s"'.format(path)
    bookmark_file = subprocess.check_output(_cmd, shell=True).decode().strip()
    return bookmark_file

__full_path = bookmark_search(_path)
