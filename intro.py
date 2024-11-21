# We import the flask instance from the entire flask package
from flask import Flask

# Below we are initializing the instance of the flask with the argument of __name__ (We can always call this variable from any python file & it is refering to the local python file we are working with)
app = Flask(__name__)

# Below is the decorator which takes the url of the website that it is going to get navigated to. Below / is the homepage of the website (root url of the website!). Decorators are required since it helps the route to understand which url we are enabling inside our website
@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

# We can see the hello world text bcoz it is the root url of our website & the hello_world() knows how to handle it well! If we were to check the /about we receive an error since we do not have any function which is handling that route!

# @app.route("/about")
# def about():
#     return '<h1>This is the about page of our website</h1>'

# Below is the dynamic routing used bcoz we won't create millions of routes for millions of users visiting our website so we created a dynamic route which helps the route to accept any string after the about route & to display the user's name with the help of our function implementation
@app.route("/about/<username>")
def about(username):
    return f'<h1>This is the about page of {username}</h1>'

# In order to make our app run successfully we have to set up some of the environment variables!
# Use debug mode on for our app to synchronize with the code change & to prevent the restarting of the app again & again, but set the debug mode of our website back to off when deploying our code since it shows some errors & it won't be a good experience for our users.