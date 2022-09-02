from ast import literal_eval


def read_file():
    return literal_eval(open('database', 'r').read())


def update_file(body):
    open('database', 'w').write(str(body))
