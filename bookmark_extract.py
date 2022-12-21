import os
import subprocess
import json
book_dict = dict()
_user = subprocess.check_output("whoami", shell=True).decode().strip()
_path = "/home/{0}/.config/".format(_user)
_path_len = _path.split('/').__len__()
for paths, dirs, files in os.walk(_path):
    if paths.split('/').__len__() == _path_len and os.path.basename(paths).startswith("Brave"):
        path = paths
        print()
        break
_cmd = 'find {0} -name "Book*s"'.format(_path)
bookmark_file = subprocess.check_output(_cmd, shell=True).decode().strip()


def bookmark_dict():
    with open(bookmark_file, "r") as f:
        return json.load(f)
