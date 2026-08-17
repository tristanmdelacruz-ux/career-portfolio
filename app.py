# idk what i am doing 7/19/2026
from flask import Flask, render_template                #importing toolboxes

app = Flask(__name__)                                   #starts the website



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



###

# project_HX_SUSPENSION_TESTRIG = {
# "name": "Suspension Test Rig (conceptual)",
# "date": "December 2025 - June 2026",
# "role": "Dynamics Engineer",
# "overview": """Involved with my college engineering project, UCI HyperXite. I wanted to build a suspension test rig as
# my team was waiting for our parts to arrive. I took inspiration from research papers and took consideration of what we already
# have in our lab space as it combines penumatics, spare aluminum extrusions, and spare test parts""",
# "image": "Suspension_Test_Rig.png",

# }

# project_HX_LATERALSUSPENSION = {
# "name": "Lateral Shock Absorber Suspension System",
# "date": " July 2025 - June 2026",
# "role": "Dynamics Engineer",
# "overview": """Involved with my college engineering project, UCI HyperXite. We were tasked to completely redesign the lateral suspension of the 
# UCI HyperPod 11. The purpose of the Lateral Suspension System is to ensure that the pod only moves in the forward direction and does not
# deviates off the track.""",
# "image": "hx_lateral_suspension.png",
# }


# project_HX_BELLCRACKSUSPENSION = {                                         #importing project one for the project section. importing the important info
# "name": "Bell Crank Lateral Suspension System",  
# "date": "July 2025 - July 2026",  
# "role": "Dynamics Engineer",             
# "overview":  """Designed the Lateral Susepension System for a Hyperloop Pod. It purpose is to restrict movement of a 100+ kg pod in the 
# lateral direction. The system is designed to experience more load in purposed to experience more oscillations as last year's suspenion system was
# overdamped.""",
# "image": "HX_BELL_CRANK.png",

# }

# project_LEGACY_WHEELHUB = {                                         #importing project one for the project section. importing the important info
# "name":  "Mars Rover Wheel Hub",  
# "date": "September 2025 - December 2025",  
# "role": "Dynamics Engineer",             
# "overview":  """Designed with inspiration from Military Tanks, this Wheel Hub to be used sustain 100+ pounds of weight
# using aliumimun sheet metal and 3D printed housings and wheel""",
# "image": "LEGACY_Wheel_Hub.png",

# }


# project_FEP_REMOTEDRONE = {
# "name": "Remote Controlled Precision Cargo Drone",
# "date": "December 2024 - May 2025",
# "role": "Mechanical Engineer Subteam Member",
# "overview": """As a mechanical engineer subteam member, I was task to create the base frame of the drone.From this project I strengthened my CAD skills
# through SOLIDWORKS and learned how a dronee functions""",
# "image": "fep_remote_drone.png",
# }

# project_FEP_MOBILEGESTUREDARM = {
# "name": "Mobile Gestured Robotic Arm",
# "date": "December 2023 - June 2024",
# "role": "Mechanical Engineer",
# "overview": """ As a mechanical engineer subteam member, I was tasked to create a 2 jointed 2 DOF Robotic Arm that would be compatible
# to a chassis and end-effector design from my other subteam members. This was my FIRST EVER project that I did and it was what lead me into 
# engineering! """,
# "image": "Mobile_Gestured_Robotic_Arm.png",
# }

# all_projects = [
#     project_HX_SUSPENSION_TESTRIG,
#     project_HX_LATERALSUSPENSION,
#     project_HX_BELLCRACKSUSPENSION,
#     project_LEGACY_WHEELHUB,
#     project_FEP_REMOTEDRONE,
#     project_FEP_MOBILEGESTUREDARM,  
# ]
