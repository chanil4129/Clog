from flask import Flask

app=Flask(__name__)

@app.route('/') #데코레이터라고 함
def index():
    return 'hi'

app.run()