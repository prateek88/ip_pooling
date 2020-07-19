from flask import Flask, render_template, request, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import IP, Base

app = Flask(__name__)

engine = create_engine('sqlite:////root/python_virtual_envs/ip_pooling/pool.db')
Base.metadata.bind = engine

@app.route('/')
def index():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    ips = session.query(IP).all()
    return render_template('index.html', ips=ips)

if __name__ == '__main__':
	app.run(debug = True)
