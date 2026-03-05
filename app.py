from flask import Flask, render_template, request, redirect
import csv

# create flask app
app = Flask(__name__)

# login credentials
USERNAME = "veera"
PASSWORD = "12345"

# load attendance data into a list of dicts
data = []
try:
    with open("attendance.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
except FileNotFoundError:
    data = []


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect("/dashboard")

        return "Invalid Login"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    student = None

    if request.method == "POST":

        roll = request.form["roll"]

        # find the first matching student by roll
        result = [r for r in data if r.get("roll") == roll]

        if result:
            student = result[0]

    return render_template("dashboard.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)