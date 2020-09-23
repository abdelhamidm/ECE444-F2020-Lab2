from flask import Flask
#create an application instance to handle requests
app = Flask(__name__)

#Decorator
@app.route('/')
#view function to register the function index as the handler for the application's root URL
def index():
    return '<h1>Hello World! </h1>'

#Decorator
@app.route('/user/<name>')
#define another function to dynamically display the user's name
def user(name):
    return '<h1>Hello, %s</h1>' % name

#run the server to service web requests
if __name__ == '__main__':
    app.run(debug=True)