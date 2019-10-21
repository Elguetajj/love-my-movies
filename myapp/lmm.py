from flask import Flask, render_template, url_for
import os
import redis

app = Flask(__name__)

client = redis.Redis('localhost','6379',0)
client.set('language', 'python')


@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', client= client)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#deployed to: https://young-refuge-73995.herokuapp.com