"""Apple screensaver downloader."""
import json
import requests

JSON_URL = "https://bzamayo.com/extras/apple-tv-screensavers.json"

try:
    request = requests.get(JSON_URL)
    data = json.loads(request.text)["data"]

    with open("url_list.txt", "w") as url_file:
        for entry in data:
            url = entry["screensavers"][0]["videoURL"]
            name = entry["name"].replace(" ", "-")
            ftype = url.rsplit("/")[-1].split(".")[1]
            local_file = f"{name}.{ftype}"
            try:
                r = requests.get(url, allow_redirects=True, verify=False)
                open(local_file, "wb").write(r.content)
            except Exception as e:
                print(name, e)
except Exception as e:
    print(e)
