# idk what i am doing 7/19/2026
from flask import Flask, render_template                #importing toolboxes

app = Flask(__name__)                                   #starts the website]

project_LEGACYWHEELHUB = {                                         #importing project one for the project section. importing the important info
"name":  "MARS ROVER WHEEL HUB",  
"date": "September 2023 - December 2023",  
"role": "Dynamics Engineer",             
"overview":  """Designed with inspiration from Military Tanks, this Wheel Hub to be used sustain 100+ pounds of weight
using aliumimun sheet metal and 3D printed housings and wheel""",

}

project_HXBELLCRACKSUSPENSION = {                                         #importing project one for the project section. importing the important info
"name":  "Bell Crank Lateral Suspension System",  
"date": "July 2025 - July 2026",  
"role": "Dynamics Engineer",             
"overview":  """Designed the Lateral Susepension System for a Hyperloop Pod. It purpose is to restrict movement of a 100+ kg pod in the 
lateral direction. The syste is designed to experience more load in purposed to experience more oscillations as last year's suspenion system was
overdamped.""",

}

@app.route("/")                                         #first page = home
def home():
    return render_template("home.html")                 #render_template(location or file)

@app.route("/about")                                    #second page = about me section
def about():
    return render_template("about.html")                #render_template(location or file)

@app.route("/projects")                                 #third page = projects section
def projects():
    return render_template("projects.html", project=project_LEGACYWHEELHUB, project2=project_HXBELLCRACKSUSPENSION)        #render_template(location or file)


if __name__ == "__main__":                              #runs the websites
    app.run(debug=True)

