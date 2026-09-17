# idk what i am doing 7/19/2026
from flask import Flask, render_template                #importing toolboxes

app = Flask(__name__)                                   #starts the website

all_projects = [
    #{"name": "Engineering Portfolio", "date": "June 2026 - September 2026", "role":"Personal Project" "overview:" "I wanted to upgrade my google slides portfolio to something where I can develop another set of skills. In which I leaned toward Web Development!" "concepts": "Python(Flask), HTML, CSS"},
    {"name": "Vertical Suspension Test Rig", "date": "December 2025 – June 2026", "role": "Dynamics Engineer", "overview": "A conceptual test rig for HyperXite suspension components, designed around available aluminum extrusions, pneumatic hardware, and spare test parts.", "image": "Suspension_Test_Rig.png", "softwares": ["Solidworks"], "concepts": ["Suspension Test Rigs",]},
    {"name": "Lateral Suspension System", "date": "July 2025 – June 2026", "role": "Dynamics Engineer", "overview": "A redesigned lateral suspension for the UCI HyperPod 11 that guides the pod along the track and manages lateral movement.", "image": "hx_lateral_suspension.png", "softwares": ["Solidworks", "Matlab/Simulink"], "concepts": ["Spring-Damper Systems", "Damping Ratios"]},
    {"name": "Bell Crank Lateral Suspension", "date": "July 2025 – July 2026", "role": "Dynamics Engineer", "overview": "A bell-crank suspension concept intended to control lateral motion on a 100+ kg hyperloop pod while accommodating repeated oscillations.", "image": "HX_BELL_CRANK.png","softwares": ["Solidworks", "Matlab/Simulink"], "concepts": ["Spring-Damper Systems", "Damping Ratios"]},
    {"name": "Mars Rover Wheel Hub", "date": "September 2025 – December 2025", "role": "Dynamics Engineer", "overview": "A tank-inspired wheel hub concept for a Mars rover, combining aluminum sheet metal with 3D-printed housings and wheel components.", "image": "LEGACY_Wheel_Hub.png", "softwares": ["Solidworks"],"concepts": ["Sheet Metal Finite Element Analysis", "Drive Motor Housings", "Wheel Material & Designs Differences"]},
    {"name": "Remote-Controlled Cargo Drone", "date": "December 2024 – May 2025", "role": "Mechanical Engineer", "overview": "A precision cargo-drone project focused on the base frame, CAD development in SOLIDWORKS, and mechanical integration.", "image": "fep_remote_drone.png", "softwares": ["Solidworks"], "concepts": ["Drone Mechanics"]},
    {"name": "Mobile Gestured Robotic Arm", "date": "December 2023 – June 2024", "role": "Mechanical Engineer", "overview": "A two-joint, two-degree-of-freedom robotic arm designed to integrate with a team-built chassis and end effector.", "image": "Mobile_Gestured_Robotic_Arm.png", "softwares": ["Solidworks"], "concepts": ["Arm Mechanics"]},
]



@app.route("/")                                         #first page = home
def home():
    return render_template("home.html")                 #render_template(location or file)

@app.route("/connect")                                    #second page = about me section
def about():
    return render_template("connect.html")                #render_template(location or file)

@app.route("/projects")                                 #third page = projects section
def projects():
    return render_template("projects.html", projects=all_projects)        #render_template(location or file)


if __name__ == "__main__":                              #runs the websites
    app.run(debug=True)

