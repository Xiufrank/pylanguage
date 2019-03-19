import redis


def redisTest():
    conn = redis.Redis('127.0.0.1')
    print(conn.keys('*'))


if __name__ == "__main__":
    redisTest()
