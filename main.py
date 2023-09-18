from flask import Flask, render_template


#__name__ -->
app = Flask(__name__)



#connect HTML pages to class object -- give path (home)
#return the HTML file through render
#HTML needs to be inside templates folder
@app.route("/")
def home():
    return render_template("home.html")

#any value user enters for station and date
@app.route("api/vi/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}



if __name__ == "__main__":
    # debug=True allows you to see errors/bugs in webpage
    app.run(debug=True)



