from flask import Flask, render_template, url_for, request
import os
import requests
import json
import redis
from database import Database

app = Flask(__name__)

r = redis.Redis('redis://h:p37e3ac52cecd741df775cce85f0659b031283a9b5f0a5ed0acd2f00768e8a987@ec2-3-231-99-188.compute-1.amazonaws.com:7979')
db = Database(r)




@app.route('/')
@app.route('/home')

def home():
    db.check_cache()
    return render_template('home.html', movies=json.loads(db.redis_db.get('trending_json')), db=db.redis_db)


@app.route('/tv')
def tv():
    db.check_cache()
    return render_template('home.html', movies=json.loads(db.redis_db.get('tv_json')), db=db.redis_db)

@app.route('/Sci-fi')
def Sci_fi():
    db.check_cache()
    return render_template('home.html', movies=json.loads(db.redis_db.get('sci_fi_json')), db=db.redis_db )


@app.route('/upvote', methods=['POST'])
def upvote_post():
    if request.method == "POST":
        movie_id = json.loads(request.data).get('postid')
        db.upvote(movie_id)
        return json.dumps({'status' : 'success'})
              
    #     if post:
    #         setattr(post, "upvote_count", post.upvote_count + 1)
    #         db_session.commit()
                 
    #         return json.dumps({'status' : 'success'})
    #     return json.dumps({'status' : 'no post found'})
    # return redirect(url_for('index'))

@app.route('/downvote', methods=['POST'])
def downvote_post():
    if request.method == "POST":
        movie_id = json.loads(request.data) 
        db.downvote(movie_id)
        return json.dumps({'status' : 'success'})





if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



#deployed to: https://young-refuge-73995.herokuapp.com