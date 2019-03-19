import urllib.request as ur


def urlOpen():
    url = 'http://www.codeceo.com/article/github-gist-usage.html'
    conn = ur.urlopen(url)
    print(conn)

    data = conn.read()
    print(data)
    print(conn.status)


if __name__ == '__main__':
    urlOpen()

