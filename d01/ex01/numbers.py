def readNumber():
    try:
        numbers = open("numbers.txt").read()

    except:
        exit(1)

    for number in numbers.split(","):
        print (number.strip())

if __name__ == '__main__':
    readNumber()
