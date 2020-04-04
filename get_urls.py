"""Apple screensaver downloader."""
import json
import requests

__author__ = "ronaldgarrison"
__copyright__ = "Copyright 2020, Ronald Garrison"
__license__ = "MIT License"
__project__ = "background video collector"

JSON_URL = "https://bzamayo.com/extras/apple-tv-screensavers.json"

try:
    request = requests.get(JSON_URL)
    data = json.loads(request.text)["data"]

    with open("url_list.txt", "w") as url_file:
        for entry in data:
            for idx, track in enumerate(entry["screensavers"]):
                url = track["videoURL"]
                name = entry["name"].replace(" ", "-")
                ftype = url.rsplit("/")[-1].split(".")[1]
                local_file = f"{name}-{idx}.{ftype}"
                try:
                    r = requests.get(url, allow_redirects=True, verify=False)
                    open(local_file, "wb").write(r.content)
                except Exception as e:
                    print(name, e)
except Exception as e:
    print(e)
