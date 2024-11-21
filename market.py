from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# 03 : Sending data to Templates
@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '#893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '#123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '#231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)
# render_template is a way to accept the requests & redirect into the html files basically it is just a way to connect our route directly to the html files. We have to import it with our Flask module!

# In order to handle 2 routes with our single html page (since we want to display the same in the case of home & in the case of our root url of website) so we just have to define 1 more route which contains the url of '/home'

# Jinja is a special web templating syntax that we are able to access through html bcoz it is specially designed for python web frameworks. It is a special template that allows us to access the info from the route.

# By using {{}} we are allowed to access the information that we have sent from our route by writing the key of the passed data inside a webpage we will see the value of the key!

# By using {% %} allows us to write the actual code which include the logic & not the variables only

#  {% endfor %} to end the for loop we can use this

# 04: Template Inheritance
# Template inheritance is used when we want to use the same layout for every page. Create a base html file with which we want to implement the layout functionality to every page of our website. We can do this by using a special Jinja Syntax which allows us to do this: 

# {% extends 'name_of_base_html_file' %}

#  If we want specific changes for our pages with which we can differentiate among them is also by using a special Jinja syntax which is as follows: block is the name of that special function & title is the name of that block!

# {% block title %}
# {% endblock %}

# Use different blocks for different specialization. 

# To use the url inside the href of the nav bar make use of url_for() from a jinja template instead of using the hard coded values of the url bcoz if we want to change our routes/urls in future it will become difficult for us to change it everytime so put the argument of the name of the route inside of our url_for() function.It will work even if we change our urls so this is the best practice to take and use the name of the route with url_for()