from flask import Flask, render_template, url_for
import os
import redis
from rq import Queue
import requests
import json


app = Flask(__name__)

#client= redis.Redis('localhost',6379,0)
#q = Queue(connection=client)


@app.route('/')
@app.route('/home')

def home():
    r = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key=1b4b5da3860135ee31a089ea237baae3')
    return render_template('home.html', movies=json.loads(r.text) )




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



#deployed to: https://young-refuge-73995.herokuapp.com