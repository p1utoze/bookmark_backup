import os
import subprocess
import json


class Bookmark(object):
    def __init__(self):
        _user = subprocess.check_output("whoami", shell=True).decode().strip()
        self._path = "/home/{0}/.config/".format(_user)
        self._path_len = self._path.split('/').__len__()

    def _getpath(self, path):
        for paths, dirs, files in os.walk(path):
            if paths.split('/').__len__() == self._path_len and os.path.basename(paths).startswith("Brave"):
                path = paths
                break
        return path

    def _bookmark_search(self, path: str) -> str:
        path = self._getpath(path)
        _cmd = 'find {0} -name "Book*s"'.format(path)
        bookmark_file = subprocess.check_output(_cmd, shell=True).decode().strip()
        return bookmark_file

    def bookmark_dict(self, fetchpath:bool=False):
        fullpath = self._bookmark_search(self._path)
        if fetchpath:
            return fullpath
        with open(fullpath, "r") as f:
            return json.load(f)

    @staticmethod
    def python_path():
        try:
            return subprocess.check_output("which python", shell=True).decode().strip()
        except subprocess.CalledProcessError:
            try:
                return subprocess.check_output("which python2", shell=True).decode().strip()
            except subprocess.CalledProcessError:
                return subprocess.check_output("which python3", shell=True).decode().strip()
