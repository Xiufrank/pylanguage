from bottle import route, run


@route('/')
def home():
    return "It isn't fancy, but it's my home page"


@route('/he')
def he():
    return '''My <b>new</b> and <i>improved</i> home page!!!'''


def static_file11(filename, path):
    name = os.path.join(path, filename)
    file = open(name, 'rt')
    str = file.readlines()
    file.close()
    return str


run(host='127.0.0.1', port=9999)
