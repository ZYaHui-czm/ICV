def diary(content):
    with open("diary.txt","a",encoding="utf-8") as d:
        d.write(content + "\n")

    with open("diary.txt","r",encoding="utf-8") as d:
        for line in d:
            print(line.strip())
            # print()

if __name__ == "__main__":
    content = input("Please enter what want to write :")
    diary(content)