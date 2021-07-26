from flask import Flask, render_template

#instantiate the Flask app
app = Flask(__name__)

#home page decorator
@app.route('/')
#function that handles home page route
def home():
    # render_template is a special function that returns an html doc
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

#how the script recognizes what is the main function to run
if __name__ == "__main__":
    app.run(debug=True)