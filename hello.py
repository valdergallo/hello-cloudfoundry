import bottle

# uwsgi will call application
app = application = bottle.Bottle()


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='localhost', port=3030, debug=True)
