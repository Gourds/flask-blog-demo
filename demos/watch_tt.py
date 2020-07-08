from flask import Flask, render_template,request,Markup,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = 'hahaha'

@app.route('/flash')
def just_flash():
    flash(u'Come on 骚骚龙')
    return redirect(url_for('index'))

@app.route('/watchlist')
def watch_list():
    user = {
        'username': 'Gli',
        'bio': 'A boy love music',
    }
    movies = [
        {'name': 'Totoro', 'year': '1988'},
        {'name': 'Tow sb', 'year': '1922'},
        {'name': 'Say Hello', 'year': '1918'},
        {'name': 'Do something', 'year': '1938'},
        {'name': 'Xzhanjing', 'year': '1978'},
    ]
    return render_template('watchlist.html', user=user, movies=movies)

@app.route('/index')
def index():
    return render_template('index.html')

@app.template_global()
def bar():
    return 'I am bar.'
#app.add_template_global(bar)

@app.context_processor
def inject_foo():
    foo = 'I am Foo'
    return dict(foo=foo)
#app.context_processor(inject_foo)

@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')
#app.template_filter(musical)

@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    else:
        return False
#app.template_test(baz)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run()