import json
from datetime import datetime
from bookmark_extract import Bookmark
import subprocess
# from timeit import default_timer
def bookmark_mod(path):
    command = f'stat -c "%Y" {path}'
    timestamp = subprocess.check_output(command, shell=True).decode()
    # print(type(timestamp), timestamp)
    return int(timestamp)


def bookmark_data(d):
    for id, name, url in filtered_json():
        # await asyncio.sleep(0.5)
        d[id] = {'name': name, 'url': url}
    d['last_updated'] = fetch_epoch_time()
    d['last_synced'] = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')


def filtered_json():
    book_dict = mybookmark.bookmark_dict()['roots']['bookmark_bar']['children']
    for i in range(len(book_dict)):
        # await asyncio.sleep(0.5)
        yield book_dict[i]['id'], book_dict[i]['name'], book_dict[i]['url']


def fetch_epoch_time():
    curr_time = bookmark_mod(mybookmark.bookmark_dict(fetchpath=True))
    # epoch_start = datetime.datetime(1601, 1, 1)
    # delta = datetime.timedelta(microseconds=int(curr_time))
    # return (epoch_start + delta).strftime("%d-%m-%Y %H:%M:%S")
    last_synced = datetime.utcfromtimestamp(curr_time).strftime("UTC: %d-%m-%Y %H:%M:%S")
    return last_synced


def main():
    with open(f'data.json', 'w+') as f:
        try:
            d = json.load(f)
        except json.decoder.JSONDecodeError:
            d = {}
        bookmark_data(d)
        json.dump(d, f, indent=4)

    with open(f"bookmark_log.txt", 'a+') as f:
        try:
            if f.readlines()[0].startswith("Created"):
                mode = 'Updated'
        except IndexError:
            mode = 'Created'
        log_text = f"{mode} 'data.json' -> {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n" \
                   f"Saved in default home directory!]\n"
        subprocess.run(['cat'], text=True, input=log_text, stdout=f)


if __name__ == '__main__':
    mybookmark = Bookmark()
    main()
