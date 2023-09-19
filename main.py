from flask import Flask, render_template
import pandas as pd


#__name__ -->
app = Flask(__name__)



#connect HTML pages to class object -- give path (home)
#return the HTML file through render
#HTML needs to be inside templates folder
@app.route("/")
def home():
    return render_template("home.html")

#any value user enters for station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    file_name = "data_small/TG_STAID" + str(station).zfill(6)+".txt"

    df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze()/10


    return {"station": station,
            "date": date,
            "temperature": temperature}



if __name__ == "__main__":
    # debug=True allows you to see errors/bugs in webpage
    app.run(debug=True)



