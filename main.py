import json
import asyncio
from bookmark_extract import bookmark_dict

def json_dump(d):
    for id, name, url in filtered_json():
        # await asyncio.sleep(0.5)
        d[id] = {'name': name, 'url': url}

def filtered_json():
    book_dict = bookmark_dict()['roots']['bookmark_bar']['children']
    for i in range(len(book_dict)):
        # await asyncio.sleep(0.5)
        yield book_dict[i]['id'], book_dict[i]['name'], book_dict[i]['url']


def main():
    with open('data.json', 'w+') as f:
        try:
            d = json.load(f)

        except json.decoder.JSONDecodeError:
            d = {}
        json_dump(d)
        json.dump(d, f, indent=4)


main()
