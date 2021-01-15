#Halló heimur með innbyggðum flask server
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application
app = Flask(__name__)

# route that calls a Python function. A route maps what you type in the browser (the url) to a Python function.
@app.route('/')
def index():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return """ <a href="/sida2">sida2</a><a href="/mynd">mynd<a>
    <h1>Hello, World!</h1>
    """

@app.route('/sida2')
def sida2():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return 'Hello, World2!'
@app.route('/mynd')
def mynd():
    return '<img src="art.png"><img>'
# This starts the web app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)   
     # debug=True. This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.
     # use_reloader. use_reloader=True þýðir að þú þarft ekki að endurkeyra python skrá stöðugt þegar þú gerir kóðabreytingar. 
     

