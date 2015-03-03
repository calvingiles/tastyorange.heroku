from flask import Flask
from segmentation import get_segmented_url


app = Flask(__name__, static_url_path='')


@app.route('/')
def route_index():
    return app.send_static_file('index.html')

@app.route('/segment/<url>')
def route_segment(url):
    with open('static/history.txt', 'a') as f:
        f.write('{}\n'.format(url))
    return get_segmented_url(url)
