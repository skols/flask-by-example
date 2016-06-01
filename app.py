import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET','POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # Get URL that the user has entered
        try: 
            url = request.form['url']
            r = requests.get(url)
        except:
            errors.append("Unable to get URL. Please make sure it's valid and try again.")
            return render_template('index.html')
    
        if r:
            # Text processing
            raw = BeautifulSoup(r.text, 'html.parser').get_text()
            nltk.data.path.append('./nltk_data') # Set the path
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            
            # Remove puncuation, count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)
            
            # Stop words
            no_stop_words = [w for w in raw_words if w.lower() not in stops]
            no_stop_words_count = Counter(no_stop_words)
            
            # Save the results
            # results = sorted(
            #     no_stop_words_count.items(),
            #     key = operator.itemgetter(1),
            #     reverse = True
            # )
            
            # Display only first 10 words
            results = sorted(
                no_stop_words_count.items(),
                key = operator.itemgetter(1),
                reverse = True
            )[:10]
            
            try:
                result = Result (
                    url = url,
                    result_all = raw_word_count,
                    result_no_stop_words = no_stop_words_count
                )
                db.session.add(result)
                db.session.commit()
            except:
                errors.append("Unable to add item to database.")
    return render_template("index.html", errors=errors, results=results)

if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
    