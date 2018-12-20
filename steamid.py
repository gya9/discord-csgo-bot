import re
import requests
import json

def get_steam_id(url):
    url = str(url)

    count = 0
    steamid_ans = []
    split = url.split("/")

    if split[3] == "profiles":
        steamid_ans = split[4]

    elif split[3] == "id":
        res = requests.get(url)
        pat = re.compile("\"steamid\":")

        steamid_index = pat.search(str(res.content)).span()[1] + 1

        while True:
            check = str(res.content)[steamid_index + count]
            if check in map(str,range(10)):
                steamid_ans.append(check)
                count +=1
                pass
            else:
                break

    return("".join(steamid_ans))