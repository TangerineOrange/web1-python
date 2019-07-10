from flask import Flask

app = Flask(__name__)


@app.route('/123')
def home():
    return 'home'
 
if __name__ == "__main__":
    app.run()
