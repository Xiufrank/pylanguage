import urllib.request as ur


def urlOpen():
    url = 'http://news.cctv.com/2019/03/20/ARTI3YAs8YFOSkXHPFnV8IVj190320.shtml'
    conn = ur.urlopen(url)
    print(conn)

    data = conn.read()
    print(data)
    print(conn.status)

    print(conn.getheader('Content-Type'))
    for key, value in conn.getheaders():
        print(key, value)


if __name__ == '__main__':
    urlOpen()

