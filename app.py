"""
 Copyright 2025 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """

import flask
import os
import time
import logging
from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.before_request
def before_request():
    flask.g.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - flask.g.start_time
    logger.info(f"Request to {request.path} took {duration:.2f} seconds")
    return response

# Available fonts for ASCII art generation
# To change the font, simply replace 'slant' in the generate_ascii_art function
# with one of these options:
# 'standard', 'slant', '3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator',
# 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3', 'banner4',
# 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block', 'bubble',
# 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal',
# 'computer', 'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive',
# 'cyberlarge', 'cybermedium', 'cybersmall', 'diamond', 'digital', 'doh', 'doom',
# 'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot',
# 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy',
# 'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 'isometric2',
# 'isometric3', 'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana',
# 'kban', 'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome', 'madrid',
# 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow',
# 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8',
# 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid',
# 'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap',
# 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short',
# 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript',
# 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars',
# 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin',
# 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi',
# 'twopoint', 'univers', 'usaflag', 'wavy', 'weird'

def generate_ascii_art(text):
    if not text:
        return "Please enter some text"
    
    # Change 'slant' to any of the fonts listed above to change the style
    ascii_art = pyfiglet.figlet_format(text, font='slant')
    return ascii_art

@app.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    
    if request.method == 'POST':
        text = request.form.get('text')
        ascii_art = generate_ascii_art(text)
    
    return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    # When running directly with python app.py, use port 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)