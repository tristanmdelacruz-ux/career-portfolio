# idk what i am doing 7/19/2026
from pathlib import Path
from flask import Flask, abort, render_template

ROOT_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__)

PROJECTS = [
    {
        "slug": "vertical-suspension-test-rig", "clickable": True,
        "name": "Vertical Suspension Test Rig",
        "role": "Dynamics Engineer",
        "date": "December 2025 – June 2026",
        "image": "vertical_sus_linkages.png",
        "design_one": "Round_Design.png",
        "design_two": "Suspension_Test_Rig.png",
        "design_three": "vertical_sus_linkages.png",
        "overview": "Conceptual Vertical Suspension Test Rig to simulate external bumps on aluminum track beam",
        "purpose": "During my time at UCI HyperXite did not have a method to validate suspension responses. We had validated our responses by using Simulink and equations of motion. So I took the initiative to 3D model a vertical suspension test rig that would react to different external forces and read the spring-damper compression.",
        "why": ["Create a repeatable way to compare test data against simulation results.", "Give future generations a method of physical testing."],
        "design_p1": "Using already in-house materials, I went the route to use round shafts to hold one metal plate at the top of the suspension system, and the other having free movement to oscillate. However I realized that creating a perfect fit for the metal plate to move smoothly would pose an issue.",
        "design_p2": "So my next design is taking a page out of our braking system and using linear rails mounted to metal bases to guide vertical oscillation. The pneumatic actuator would simulate an external bump and the wheel would experience force upwards to oscillate.",
        "design_p3": "Lastly, I added guide linkages at each side of the test rig to ensure constriction of vertical oscillations.",
        "roadblocks": [
            {"title": "Timeline", "text": "Unfortunately, this only reached the design phase as I did not have enough time to finalize the design & hardware."},
            {"title": "Measurement plan", "text": "The early draft needed a clearer approach for sensors, data capture, and repeatable loading."}
        ],
        "result": "A complete mechanical concept and a clear handoff package for a future team to refine, manufacture, and validate.",
        "lessons": ["Ask for feedback as much as you can. I believe if I asked for help earlier I would have at least built part of a physical system.", "Work in tandem with hardware and measurement plan. This would be helpful when passing the design along to the next team."],
    },
    {
        "slug": "lateral-suspension-system", "clickable": True,
        "name": "Lateral Suspension System",
        "role": "Dynamics Engineer",
        "date": "July 2025 – June 2026",
        "image": "final_lateral_sus.png",
        "design_one": "torsion_design.png",
        "design_two": "hx_lateral_suspension.png",
        "design_three": "final_lateral_sus.png",
        "overview": "Spring-Damper Suspension Linkage System that prevents yaw movement for a 100+ kg Hyperpod",
        "purpose": "Redesign the HyperPod 11 lateral suspension so the pod stays guided along the I-beam track while accommodating expected yaw movement.",
        "why": ["Optimize more oscillation on the pod to improve mechanical advantage.", "Create a design that can be tuned as real test data becomes available."],
        "design_p1": "For HX 11, we wanted a complete redesign of the lateral suspensions. The past suspension system was too stiff which meant more force being exerted onto the chassis. Thus we first tried to change the type of spring we would use — a torsion spring.",
        "design_p2": "However, that posed a few problems such as assembly, mounting, and strength. So we decided to pivot back to a spring-damper system, but choose less stiff springs so the suspension would absorb more external forces.",
        "design_p3": "Once we decided on the design, unfortunately during purchasing we were given longer spring-dampers than requested. We did not have enough time to reorder, so we pivoted to a singular spring-damper with the same stiffness.",
        "roadblocks": [
            {"title": "Creativeness", "text": "When given the task to make a complete redesign, we struggled to creatively come up with a unique design that balanced optimization and effectiveness."},
            {"title": "Incorrect Order", "text": "During purchasing our spring-dampers, we received the incorrect size. Purchasing earlier would help compensate for any mis-orders."}
        ],
        "result": "A final lateral suspension was implemented and posed no issues on the Hyperpod.",
        "lessons": ["It's okay to redesign. Ensure that you have leeway for any modifications needed.", "Design parameters should remain adjustable when the system is still being validated."],
    },
    {
        "slug": "bell-crank-lateral-suspension", "clickable": True,
        "name": "Bell Crank Lateral Suspension",
        "role": "Dynamics Engineer",
        "date": "July 2025 – July 2026",
        "image": "HX_BELL_CRANK.png",
        "design_one": "bellcrank_one.png",
        "design_two": "bellcrank_two.png",
        "design_three": "bellcrank_three.png",
        "overview": "Conceptual Bell Crank Lateral Suspension System to prevent yaw movement for a 100+ kg Hyperpod",
        "purpose": "Explore a bell-crank mechanism that translates lateral pod motion into controlled spring-and-damper travel, providing a more compact and tunable suspension alternative.",
        "why": ["Use leverage geometry to package the suspension in a compact area.", "Provide an alternative to a direct acting suspension layout."],
        "design_p1": "I first got the idea of a bell crank from looking at F1 car suspensions. My first iteration of design, I had misproportioned the parts so the bell crank was way too small compared to the linkages.",
        "design_p2": "From there I increase the bell crank size, however my issue was finding the right size where it could fit in the margins of space that was given to me and optimizing the rotation of the bell crank.",
        "design_p3": "The final design was a good sized bell crank and to compensate to getting a bigger spring-damper that I would be able to buy on the market, I angled the spring-damper so that it would align better in compression when hitting an external bump.",
        "roadblocks": [
            {"title": "Motion ratio", "text": "Small changes to pivot locations significantly affected force and travel, so the geometry needed repeated checks. Lots of hand calculations"},
            {"title": "Complexity", "text": "The final geometry had to stay realistic for the task, and at this time I did not feel confident in my hand calculations to ensure that the concept worked."}
        ],
        "result": "A documented suspension concept that demonstrated the relationship between linkage geometry and system behavior, providing a strong foundation for potential future teams to build on.",
        "lessons": ["Mechanism geometry should be checked with both sketches and physical constraints.", "A design is stronger when the analysis and manufacturing plan develop together."],
    },
    {
        "slug": "mars-rover-wheel-hub", "clickable": True,
        "name": "Mars Rover Wheel Hub",
        "role": "Dynamics Engineer",
        "date": "September 2025 – December 2025",
        "image": "LEGACY_Wheel_Hub.png",
        "design_one": "before.png",
        "design_two": "LEGACY_Wheel_Hub.png",
        "design_three": "weight.jpg",
        "overview": "Wheel Hub with Drive Motor Housing and Aluminum Sheet Metal for connection to Rocker Bogie Suspension System",
        "purpose": "Create a robust wheel-hub concept for a Mars rover that supports expected loading while integrating the wheel and drive hardware into a manufacturable package.",
        "why": ["Execute drive during terrain competitiion traversals.", "Make it manufacturable & changeable to independent steering."],
        "design_p1": " I was coming in with a design that had already been made, however my task was to switch the connection from pvp pipes to aluminum sheet metal.",
        "design_p2": " Thus I collaborated with my team lead to make a aluminum sheet metal shape that would help connect to the drive motor housing and create a connection to the rocker bogie suspension system. ",
        "design_p3": "The final design incorporated standoffs to increase the strenght of the sheet metal has it would hold up a 50+ pound mars rover.",
        "roadblocks":[
            {"title": "3D Printing Treads", "text": "3D Printing the treads from TPU held a huge problem with our design as our 3D printer could not handle the amount of tpu being displaced and putting the tread on top of a wheel frame posed difficult due to it's stiffness."},
            {"title": "Timeline", "text": " Unfortunately this design did not make it to the fabrication process as the year ended and a new team took over the responsibility. However the design was used as an influence to more new designs."}],
        "result": "A wheel-hub design that served it's intent with being compatible with tank steering capabilities and structural integrity.",
        "lessons": ["Communicate when you need help. There was a time where I stayed up until 4am designing when in reality I just needed some feedback.", "Design for it's purpose, sometimes overdesigning can kill the product."],
    },
    

    {
        "slug": "remote-controlled-cargo-drone", "clickable": False,
        "name": "Remote-Controlled Cargo Drone",
        "role": "Mechanical Engineer",
        "date": "December 2024 – May 2025",
        "image": "fep_remote_drone.png",
        "design_one": "fep_remote_drone.png",
        "design_two": "fep_remote_drone.png",
        "design_three": "fep_remote_drone.png",
        "overview": "Quadcopter with claw attachment capable of lifting small payloads through a gripper mechanism",
        "purpose": "Design the base frame for a precision cargo drone that could support the required components and carry out a payload-focused mission.",
        "why": ["Provide a stable mechanical foundation for the flight and payload systems.", "Build confidence with CAD, integration, and team-based design decisions."],
        "design_p1": "The initial frame concept used a simple cross-arm layout sized around the motor mounts and battery placement. Early sketches focused on minimizing arm flex while keeping the total weight within the flight budget.",
        "design_p2": "As the team's electronics and payload subteams finalized their component sizes, the frame was updated to include defined attachment points for the flight controller, ESCs, and the claw mounting interface. Each change was tracked against the weight budget.",
        "design_p3": "The final design incorporated a central body plate with extended arms and integrated standoffs for the payload claw. Landing legs were added to protect the claw mechanism on touchdown and keep the frame level during loading operations.",
        "roadblocks": [
            {"title": "Interfaces", "text": "Mechanical decisions depended on components being developed simultaneously by other subteams, requiring constant communication to avoid mismatches."},
            {"title": "Weight", "text": "Each added bracket solved an attachment problem but affected the overall mass budget, requiring repeated trade studies."}
        ],
        "result": "A complete frame design that gave the team a practical base for integrating the full cargo-drone system and successfully demonstrating payload pickup.",
        "lessons": ["Communicate interfaces early and often — waiting for other teams to finalize before starting creates bottlenecks.", "The simplest structure that meets the requirement is usually the best starting point."],
    },
    {
        "slug": "mobile-gestured-robotic-arm",
        "name": "Mobile Gestured Robotic Arm",
        "role": "Mechanical Engineer",
        "date": "December 2023 – June 2024",
        "image": "Mobile_Gestured_Robotic_Arm.png",
        "design_one": "Mobile_Gestured_Robotic_Arm.png",
        "design_two": "Mobile_Gestured_Robotic_Arm.png",
        "design_three": "Mobile_Gestured_Robotic_Arm.png",
        "overview": "2DOF Robotic Arm compatible with a designed chassis and end-effector, tasked to assist the end-effector pick up small payloads and drop them into the chassis compartments",
        "purpose": "Design a two-joint robotic arm that could mount to a team-built chassis and work with an end effector developed by other members to pick up and store small payloads.",
        "why": ["Translate a motion requirement into a functional mechanical system.", "Learn the fundamentals of collaborative CAD and physical prototyping as a first-year engineering student."],
        "design_p1": "This was my very first engineering project. The initial concept focused on defining the two degrees of freedom and sizing the link lengths to reach the required workspace. Early sketches helped establish the joint positions relative to the chassis mounting point.",
        "design_p2": "As the chassis and end-effector designs matured, the arm geometry was adjusted to match their interface dimensions. Joint housings were modeled in SOLIDWORKS and revised multiple times as the team refined the overall system layout.",
        "design_p3": "The final arm incorporated two pivot joints with defined travel limits and a mounting bracket sized to the chassis connection. The link proportions were chosen to balance reach, stiffness, and the manufacturing constraints of the team's available tools.",
        "roadblocks": [
            {"title": "Integration", "text": "The arm design had to remain compatible with evolving chassis and end-effector designs, requiring frequent check-ins with other subteam members."},
            {"title": "First-time learning curve", "text": "Learning CAD conventions and mechanism design simultaneously made iteration essential — nearly every part was redesigned at least once."}
        ],
        "result": "A functional two-joint robotic arm that successfully integrated with the chassis and end-effector, completing payload pickup and storage tasks during the final demonstration.",
        "lessons": ["Start simple, then iterate with evidence — overcomplicating the first design wastes time.", "Good team projects depend on clear interface dimensions and shared deadlines established early."],
    },
]

CARD_METADATA = {
    "vertical-suspension-test-rig": {"concepts": ["Suspension test rigs"], "softwares": ["SOLIDWORKS"]},
    "lateral-suspension-system": {"concepts": ["Spring-damper systems", "Damping ratios"], "softwares": ["SOLIDWORKS", "MATLAB / Simulink"]},
    "bell-crank-lateral-suspension": {"concepts": ["Spring-damper systems", "Damping ratios"], "softwares": ["SOLIDWORKS", "MATLAB / Simulink"]},
    "mars-rover-wheel-hub": {"concepts": ["Sheet-metal FEA", "Drive motor housings", "Wheel-material selection"], "softwares": ["SOLIDWORKS"]},
    "remote-controlled-cargo-drone": {"concepts": ["Drone mechanics"], "softwares": ["SOLIDWORKS"]},
    "mobile-gestured-robotic-arm": {"concepts": ["Arm mechanics"], "softwares": ["SOLIDWORKS"]},
}

for project in PROJECTS:
    project.update(CARD_METADATA[project["slug"]])


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((item for item in PROJECTS if item["slug"] == slug), None)
    if project is None:
        abort(404)
    return render_template("project_details.html", project=project)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/connect")
def about():
    return render_template("connect.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)