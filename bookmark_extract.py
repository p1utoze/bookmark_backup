from datetime import datetime
import os
import subprocess
import json
import datetime

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




def bookmark_dict():
    full_path = bookmark_search(_path)
    with open(full_path, "r") as f:
        return json.load(f)

def bookmark_mod(path):
    _user = subprocess.check_output("whoami", shell=True).decode().

def json_dump(d):
    for id, name, url in filtered_json():
        # await asyncio.sleep(0.5)
        d[id] = {'name': name, 'url': url}

def filtered_json():
    book_dict = bookmark_dict()['roots']['bookmark_bar']['children']
    for i in range(len(book_dict)):
        # await asyncio.sleep(0.5)
        yield book_dict[i]['id'], book_dict[i]['name'], book_dict[i]['url']

def fetch_epoch_time(timestamp):
    epoch_start = datetime.datetime(1601, 1, 1)
    delta = datetime.timedelta(microseconds=int(timestamp))
    return (epoch_start + delta).strftime("%d-%m-%Y %H:%M:%S")

def main():
    with open('data.json', 'w+') as f:
        try:
            d = json.load(f)
        except json.decoder.JSONDecodeError:
            d = {fetch_epoch_time()}
        json_dump(d)
        json.dump(d, f, indent=4)
