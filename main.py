import requests
import microdotphat
import time

tasks = requests.get(
    "https://api.mattglei.ch/things/cache", headers={"Authorization": "Bearer 1234"}
).json()

for task in tasks["today_todos"]:
    microdotphat.clear()
    task_name = task["name"]
    pixel_len = microdotphat.write_string(task["name"] + "   ", kerning=False)
    microdotphat.show()
    if len(task_name) > 6:
        for i in range(pixel_len):
            microdotphat.scroll()
            microdotphat.show()
            time.sleep(0.02)
    time.sleep(1)
