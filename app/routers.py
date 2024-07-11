from flask import render_template
from app.app import app


@app.route('/')
def test():
    return render_template('test.html')
