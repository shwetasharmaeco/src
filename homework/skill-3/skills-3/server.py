from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'

MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

@app.route("/")
def homepage():
    melons_dict = MOST_LOVED_MELONS
    

    if "name" in session:
        name = session.get("name")

        # return redirect ("/top-melons")
                        
        return render_template("homepage.html")


@app.route("/get-name")
def get_name():

    name = request.args.get("name")

    session["name"]= request.args.get("name")
    
    return redirect ("/top-melons")



@app.route("/top-melons")
def display_melons():

    melons_dict = MOST_LOVED_MELONS
    

    if "name" in session:
        name = session.get("name")

        return render_template("top-melons.html", 
                        melons_dict= melons_dict,
                        )
    else:
        return redirect("/")


@app.route("/love-melon",  methods=["POST"])
def add_like():

    for melon, val in MOST_LOVED_MELONS.items():
        melon_liked = request.values.get("melon")
        print("**********", melon_liked)

        if melon_liked == val['name']:  
            val['num_loves']+=1
           

    return render_template("thank-you.html")



if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
