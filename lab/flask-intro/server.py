"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = ["loser", "dumbo" , "bore"]


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    <head>
    <title>start here</title>
    </head>
    <body>
    <a href='/hello'>
    Hi! This is the home page.
    </a>
    </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
          <label for = "compliment"> select your compliment </label><br>
          <select name = "compliment">
            <option value='awesome'> awesome </option>
            <option value = "terrific"> terrific </option>
            <option value=" lovely">lovely </option>
            <option value="wonderful"> wonderful</option>
          </select><br><br>
          <input type="submit"><br><br><br><br>
          </form>

        <form action="/diss">
        What's your name? <input type="text" name="person1"><br><br>
        If you dont like us much submit this instead <br><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def diss_person():
  player = request.args.get("person1")

  diss = choice(DISS)

  return """ <!doctype html>
  <html>
  you're a {} , HAHA!
  </html>""".format(diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
