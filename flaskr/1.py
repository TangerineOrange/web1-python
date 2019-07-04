from flask import Flask, url_for, render_template, request,flash, redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
            flash('You were successfully logged in')
            return redirect(url_for('index'))
            # return render_template('userinfo.html', username=request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def valid_login(username, pwd):
    print('username:  '+username)
    print('pwd:  '+pwd)
    
    if username == 'abc' and pwd == '123':
        return True
    return False


with app.test_request_context():
    print(url_for('index', pagenum=1))
    print(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
