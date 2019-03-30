import time


def start():
    now = time.time()
    print(now)
    print(time.ctime(now))
    print(time.localtime(now))
    print(time.gmtime(now))


if __name__ == "__main__":
    start()
