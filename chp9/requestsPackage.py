import requests


def getRequest(url):
    re = requests.get(url)
    # print(re.text)
    cookie = re.cookies;
    head = re.headers;

    print(type(cookie))
    print(cookie)
    print(type(head))
    print(head)


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    # url = 'http://122.224.233.66:9083/login/Login.jsp?logintype=1'
    getRequest(url)
