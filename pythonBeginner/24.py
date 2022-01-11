try:
    file = open('lecture.txt', encoding="utf-8")
    try:   
        # print(file.read())
        print(file.readline(), end='')
        print(file.readline(), end='')
    finally:
        file.close()
except FileNotFoundError:
    print('file not found')