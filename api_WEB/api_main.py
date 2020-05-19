#!flask/bin/python
from flask import Flask,request,url_for,render_template

app = Flask(__name__)

@app.route('/para/<user>')
def index(user):
    return render_template('index.html', user_template=user)

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST': 
        return 'Hello ' + request.values['username'] 

    return "<form method='post' action='/login'><input type='text' name='username' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

@app.route('/user/<username>')
def username(username):
    return 'i am ' + username

@app.route('/age/<int:age>')
def userage(age):
    return 'i am ' + str(age) + ' years old'

@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    #  會將使用者引導到'/a'這個路由
    return redirect(url_for('url_for_a'))

if __name__ == '__main__':
        app.run(debug=True)