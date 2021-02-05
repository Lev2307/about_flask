from database import add_user, read_from_db
from flask import Flask, render_template, request
from superhero_api import SuperHeroAPI

app  = Flask(__name__)
s = SuperHeroAPI()

@app.route('/', methods=['POST', 'GET'])
def index():
    img_url = s.get_hero_image_url('Arsenal')
    _data = img_url
    return render_template('index.html', data=_data)