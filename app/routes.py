from app import app
from flask import render_template


@app.route('/')
@app.route('/shop')
def shop():
    
    
    """Index URL"""
    return render_template('shop.html', title='Shop Page')
    
@app.route('/register')
def register():
    
    
    """Index URL"""
    return render_template('register.html', title='Register Page')
    
@app.route('/login')
def login():
    
    
    """Index URL"""
    return render_template('login.html', title='Login Page')


    
    