import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    pres_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison",
                 "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
                 "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge",
                 "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
                 "Clinton", "Obama", "Trump", "Biden"]
    pres_text = []
    resp = requests.get(url_ddg + "/?q=Presidents of the united States&format=json")
    pres_data = resp.json()
    for i in pres_data["RelatedTopics"]:
        pres = i["Text"].split("-")[0]
        if len(pres.split(" ")) > 2:
            pres_text.append(pres.split(" ")[-2])

    for i in pres_list:
        assert i in pres_text
