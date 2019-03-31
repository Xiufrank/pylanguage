import time
import os


def save2File():
    now = time.localtime()
    tamest = time.strftime("%Y-%m-%d %H:%M:%S", now)

    f = open("now", "wt")
    f.write(tamest)


def readTime():
    f = open("now", "rt")
    savetime = f.readline()
    print(savetime)

    t = time.strptime(savetime, "%Y-%m-%d %H:%M:%S")
    print(t)


def consoleFiles():
    path = os.getcwd()
    par = os.path.dirname(path)
    # print(path)

    walkFiles(par)


def walkFiles(path):
    print(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
        for dir in dirs:
            childDir = os.path.join(root, dir)
            print(childDir)
            walkFiles(childDir)


if __name__ == "__main__":
    # save2File()
    # readTime()
    consoleFiles()

