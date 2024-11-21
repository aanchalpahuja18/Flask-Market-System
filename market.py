from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# render_template is a way to accept the requests & redirect into the html files basically it is just a way to connect our route directly to the html files. We have to import it with our Flask module!

# In order to handle 2 routes with our single html page (since we want to display the same in the case of home & in the case of our root url of website) so we just have to define 1 more route which contains the url of '/home'

# Jinja is a special web templating syntax that we are able to access through html bcoz it is specially designed for python web frameworks. It is a special template that allows us to access the info from the route.

# By using {{}} we are allowed to access the information that we have sent from our route by writing the key of the passed data inside a webpage we will see the value of the key!

# By using {% %} allows us to write the actual code which include the logic & not the variables only

#  {% endfor %} to end the for loop we can use this