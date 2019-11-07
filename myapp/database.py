import redis
import requests
import json
from datetime import datetime

class Database:

    redis_db = None

    def __init__(self, redis_connection):
        self.redis_db = redis_connection
        self.movies()

    def movies(self):
        trending = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key=1b4b5da3860135ee31a089ea237baae3')
        tv = requests.get('https://api.themoviedb.org/3/trending/tv/week?api_key=1b4b5da3860135ee31a089ea237baae3')
        sci_fi = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=1b4b5da3860135ee31a089ea237baae3&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=%20878')
        self.redis_db.set('trending_json', trending.text )
        self.redis_db.set('tv_json', tv.text)
        self.redis_db.set('sci_fi_json',sci_fi.text)
        self.timestamp = datetime.now()
        self.movie_votes()
    
    def check_cache(self):
        now = datetime.now()
        diff = (now-self.timestamp).total_seconds()
        print(diff)
        if( diff > 1000) :
            self.refresh_cache()
        else:
             pass 

    def refresh_cache(self):
        self.movies()
    
    def movie_votes(self):
        trending = self.redis_db.get('trending_json')
        tv = self.redis_db.get('tv_json')
        sci_fi = self.redis_db.get('sci_fi_json')
        all_jsons=[trending, tv,sci_fi]
        for movie_json in all_jsons:
            movies = json.loads(movie_json)
            for movie in movies.get('results'):
                if self.redis_db.exists(f'{movie.get("id")}'):
                    pass
                else:
                    self.redis_db.set(f'{movie.get("id")}', movie.get("vote_count"))
    
    def upvote(self, id):
        self.redis_db.incr(f'{id}')
        print(self.redis_db.get(f'{id}'))

    def downvote(self,id):
        self.redis_db.decr(f'{id}',  )
