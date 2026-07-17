import json
from datetime import datetime , date , timedelta
def save_diary(entry):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    diary = {
        "time" : now,
        "content" : entry
    }
    with open("diary.json","a",encoding="utf-8") as dia:
        json.dump(diary , dia , ensure_ascii = False , indent = 2)

if __name__ == "__main__":
    entry = input("please enter the content you want :")
    save_diary(entry)
