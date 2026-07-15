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

# Fonts offered in the font-selection dropdown (a curated subset of the
# fonts pyfiglet ships with).
AVAILABLE_FONTS = [
    'slant', 'standard', 'big', 'block', 'bubble', 'digital', 'ivrit',
    'lean', 'mini', 'script', 'shadow', 'slscript', 'small', 'smslant',
    'starwars', 'straight',
]
DEFAULT_FONT = 'slant'

def generate_ascii_art(text, font=DEFAULT_FONT):
    if not text:
        return "Please enter some text"

    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    selected_font = DEFAULT_FONT

    if request.method == 'POST':
        text = request.form.get('text')
        selected_font = request.form.get('font', DEFAULT_FONT)
        ascii_art = generate_ascii_art(text, selected_font)

    return render_template('index.html', ascii_art=ascii_art, fonts=AVAILABLE_FONTS, selected_font=selected_font)

if __name__ == '__main__':
    # When running directly with python app.py, use port 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)