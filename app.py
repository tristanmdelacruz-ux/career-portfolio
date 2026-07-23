# idk what i am doing 7/19/2026
from flask import Flask, render_template                #importing toolboxes

app = Flask(__name__)                                   #starts the website]

project_one = {                                         #importing project one for the project section. importing the important info
"name":  "Mobile Gestured Robotic Arm",                 
"overview":  "As a freshman in college, I was tasked to build a robotic arm of to combine a tank a wooden chassis and 3d printed end-effector",
"role": "Mechanical Engineering Subteam Member",
"skills": ["Solidworks", "3D Printing"],
}

@app.route("/")                                         #first page = home
def home():
    return render_template("home.html")                 #render_template(location or file)

@app.route("/about")                                    #second page = about me section
def about():
    return render_template("about.html")                #render_template(location or file)

@app.route("/projects")                                 #third page = projects section
def projects():
    return render_template("projects.html", project=project_one)        #render_template(location or file)


if __name__ == "__main__":                              #runs the websites
    app.run(debug=True)

