from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True) # debug mode means that if there is an error, it will be visible in the app(webpage here)

# Bootstrap is a framework, we get style components, example templates,
# my-4 gives us some more space between website header and title