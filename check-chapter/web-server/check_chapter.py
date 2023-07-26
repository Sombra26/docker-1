import time
import datetime
import requests


chapter_id = 1089


while True:


    r = requests.get("http://www.volonte-d.com/", verify=False)
    is_new_chapter_released = f"chapitre {chapter_id}" in str(r.content).lower()
    now = datetime.datetime.now()

    with open("index.html", "a") as file:
        if is_new_chapter_released:
            message = f"<h1>{now} - chapter: {chapter_id} is available 👌</h1>"

        else:
            message = f"<h1>{now} - chapter: {chapter_id} is not available 😢</h1>"

        file.write(message)

    time.sleep(10)