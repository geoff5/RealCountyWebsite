"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CountyWebsite import app, cms, database, utils

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    
    
    return render_template(
        'index.html',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        year=datetime.now().year
    )

@app.route('/news')
def news():
    """Renders the news page."""
    return render_template(
        'news.html',
        title='News',
        year=datetime.now().year
    )

@app.route('/register')
def register():
    """Renders the registration page."""
    return render_template(
        'register.html',
        title='Register',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year
    )