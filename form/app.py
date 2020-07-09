from flask import Flask,render_template,request,redirect,flash
from forms import LoginForm,RichTextForm
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'python is good'

#article

app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_for_ckeditor'
ckeditor = CKEditor(app)


@app.route('/basic', methods=['GET','POST'])
def basic():
    form = LoginForm()
    if request.method == 'POST':
        print(form.username)
        flash('Welcome %s' % form.username.data)
        return redirect('index')
    return render_template('login.html', form=form)

# @app.route('/boot', methods=['GET','POST'])
# def bootstarp():
#     form = LoginForm()
#     return render_template('bootstrap.html', form=form)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    form = LoginForm()
    return render_template('upload.html',form=form)

@app.route('/article')
def article():
    form = RichTextForm()
    return render_template('article.html', form=form)

if __name__ == '__main__':
    app.run()