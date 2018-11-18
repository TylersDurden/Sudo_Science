import os, yaml, logging
from flask import Flask, render_template, Markup
if os.name != 'nt':
    try:
        import markdown, logging
    except:
        pass

app = Flask(__name__)
app.config.from_pyfile('settings.py')

cache = {}
logger = logging.getLogger(__name__)


def get_page(dir, file):
    filename = (file)

    if filename in cache:
        return cache[filename]

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), dir,filename))
    try:
        file_contents = open(path, encoding='utf-8').read()
    except:
        return None

    data, text = file_contents.split('---\n', 1)
    page = yaml.load(data)
    page['content'] = Markup(markdown.markdown(text))
    page['path'] = file

    cache[filename] = page
    return page


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('sample.html')

@app.route('/')
def switch(name=None):
    dataout = ''
    dataout += 'OS: ' + os.name+'\n'
    



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)