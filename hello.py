from flask import Flask,request,abort,jsonify,make_response,redirect,url_for,session
from flask import g
from urllib.parse import urljoin,urlparse
from jinja2.utils import generate_lorem_ipsum
from jinja2 import escape

app = Flask(__name__)
app.secret_key = 'dinggelongdongqiang'


@app.before_request
def get_name():
    g.name = request.args.get('name')

@app.route('/index')
@app.route('/')
def index():
    name = request.args.get('name')
    if not name:
        name = request.cookies.get('name', 'DDD')
    response = '<h1>Gourds, %s</h1>' % name
    if 'logged_in' in session:
        response += 'Auth'
    else:
        response += 'Not auth'
    return response

@app.route('/hello', defaults={'name': 'PPP'})
@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hi, %s</h1>' % escape(name)

@app.route('/test')
def test_json():
    return jsonify(name='haha', gender='male')

@app.route('/404')
def not_found():
    abort(404)

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name',name)
    return response

@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    abort(403)

@app.route('/foo')
def foo():
    return '<h1> foo page</h1><a href="%s">Do something</a>' % url_for('do_something', next=request.full_path)

@app.route('/bar')
def bar():
    return '<h1> bar page </h1><a href="%s">Do something</a>' % url_for('do_something', next=request.full_path)

@app.route('/do_something')
def do_something():
    # return redirect(url_for('index'))
    # return redirect(request.referrer or url_for('hello'))
    # return redirect(request.args.get('next', url_for('index')))
    for target in request.args.get('next'), request.referrer:
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for('index'))

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    print(ref_url, test_url)
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
<h1> long post </h1>
<div class="body"> %s </div>
<button id="load"> Load More</button>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script type="text/javascript">
$(function(){
 $('#load').click(function(){
    $.ajax({
       url: '/more',
       type: 'get,
       success: function(data){
          $('.body').append(data);
       }
    })
 })
})
</script>''' % post_body

@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)

if __name__ == '__main__':
    app.run()