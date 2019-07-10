# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
# db = SQLAlchemy(app)


@app.route('/123')
def num():
    rv = sqlite3.connect(app.config['DATABASE'])
    c = rv.cursor()
    all=c.execute('SELECT * FROM abc;')
    # print(c.fetchone())
    for row in all:
        print(row)
        
    print(c.fetchall())
    return '123111'


@app.route('/')
def home():
    return 'home'


# def connect_db2():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv


# def connect_db():
#     """Connects to the specific database."""
#     return sqlite3.connect(app.config['DATABASE'])


# @app.before_request
# def before_request():
#     g.db = connect_db()


# @app.teardown_request
# def teardown_request(exception):
#     if hasattr(g, 'db'):
#         g.db.close()
# def query_db(query, args=(), one=False):
#     cur = g.db.execute(query, args)
#     rv = [dict((cur.description[idx][0], value)
#                for idx, value in enumerate(row)) for row in cur.fetchall()]

#     return (rv[0] if rv else None) if one else rv


# def get_connection():
#     db = getattr(g, '_db', None)
#     if db is None:
#         db = g._db = connect_db()
#     return db


# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


# def get_db():
#     pass


if __name__ == "__main__":
    app.run(debug=True)

