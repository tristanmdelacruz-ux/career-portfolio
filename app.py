# idk what i am doing 7/19/2026
"""Standalone preview for the project-detail experience.

Run from this folder with: python app.py
The preview uses the existing portfolio's static images without changing the main site.
"""

from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory


ROOT_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__)

PROJECTS = [
    {
        "slug": "vertical-suspension-test-rig",
        "name": "Vertical Suspension Test Rig",
        "role": "Dynamics Engineer",
        "date": "December 2025 – June 2026",
        "image": "Suspension_Test_Rig.png",
        "purpose": "Develop a concept for a bench-top rig that could physically load a HyperPod suspension assembly and record its response before the component goes onto the pod.",
        "why": ["Create a repeatable way to compare test data against simulation results.", "Give the next team a practical starting point for suspension validation."],
        "design": "The draft uses accessible lab hardware—aluminum extrusion, linear rails, a pneumatic actuator, and adaptable mounting plates—so the structure can be adjusted as the test plan evolves.",
        "roadblocks": [{"title": "Timeline", "text": "The concept arrived late in the design cycle, leaving limited time to move into fabrication."}, {"title": "Measurement plan", "text": "The early draft needed a clearer approach for sensors, data capture, and repeatable loading."}],
        "result": "A complete mechanical concept and a clear handoff package for a future team to refine, manufacture, and validate.",
        "lessons": ["Ask for feedback early, especially when a design depends on a testing workflow.", "Build the measurement strategy alongside the mechanism—not after it."],
    },
    {
        "slug": "lateral-suspension-system",
        "name": "Lateral Suspension System",
        "role": "Dynamics Engineer",
        "date": "July 2025 – June 2026",
        "image": "hx_lateral_suspension.png",
        "purpose": "Redesign the HyperPod 11 lateral suspension so the pod stays guided along the I-beam track while accommodating expected movement.",
        "why": ["Improve directional stability during operation.", "Create a design that can be tuned as real test data becomes available."],
        "design": "The layout explores a spring-and-damper linkage with mounting points sized around the pod structure. Early CAD studies focused on packaging, travel, and access for assembly.",
        "roadblocks": [{"title": "Packaging", "text": "The mechanism had to fit within a crowded pod envelope without blocking adjacent systems."}, {"title": "Tuning", "text": "Selecting stiffness and damping values required balancing simulation assumptions with realistic component limits."}],
        "result": "A final lateral-suspension direction that established a stronger basis for future dynamic testing and iteration.",
        "lessons": ["A clear packaging model prevents late-stage interference issues.", "Design parameters should remain adjustable when the system is still being validated."],
    },
    {
        "slug": "bell-crank-lateral-suspension",
        "name": "Bell Crank Lateral Suspension",
        "role": "Dynamics Engineer",
        "date": "July 2025 – July 2026",
        "image": "HX_BELL_CRANK.png",
        "purpose": "Explore a bell-crank mechanism that translates lateral pod motion into controlled spring-and-damper travel.",
        "why": ["Use leverage geometry to package the suspension in a compact area.", "Provide a tunable alternative to a direct-acting suspension layout."],
        "design": "The concept used a pivoting bell crank, adjustable linkage points, and a compact damper placement. CAD drafts compared motion ratios and potential mounting locations.",
        "roadblocks": [{"title": "Motion ratio", "text": "Small changes to pivot locations significantly affected force and travel, so the geometry needed repeated checks."}, {"title": "Manufacturability", "text": "The final geometry had to stay realistic for the tools, material thicknesses, and fasteners available to the team."}],
        "result": "A documented suspension concept that demonstrated the relationship between linkage geometry and system behavior.",
        "lessons": ["Mechanism geometry should be checked with both sketches and physical constraints.", "A design is stronger when the analysis and manufacturing plan develop together."],
    },
    {
        "slug": "mars-rover-wheel-hub",
        "name": "Mars Rover Wheel Hub",
        "role": "Dynamics Engineer",
        "date": "September 2025 – December 2025",
        "image": "LEGACY_Wheel_Hub.png",
        "purpose": "Create a robust wheel-hub concept for a Mars rover that supports expected loading while integrating the wheel and drive hardware.",
        "why": ["Protect the drive components during terrain traversal.", "Make the hub easier to manufacture and service with the team’s available processes."],
        "design": "The draft combines sheet-metal structure with 3D-printed housings and wheel elements. The team evaluated mounting patterns, material thickness, and service access.",
        "roadblocks": [{"title": "Load path", "text": "The hub needed a clear route for forces from the wheel into the rover frame."}, {"title": "Material tradeoffs", "text": "Lightweight parts were desirable, but durability and manufacturing time had to remain realistic."}],
        "result": "A wheel-hub direction that connected structural intent, motor packaging, and practical fabrication choices.",
        "lessons": ["Define the load path before refining individual brackets.", "Serviceability is a design requirement, not a finishing touch."],
    },
    {
        "slug": "remote-controlled-cargo-drone",
        "name": "Remote-Controlled Cargo Drone",
        "role": "Mechanical Engineer",
        "date": "December 2024 – May 2025",
        "image": "fep_remote_drone.png",
        "purpose": "Design the base frame for a precision cargo drone that could support the required components and payload-focused mission.",
        "why": ["Provide a stable mechanical foundation for the flight and payload systems.", "Build confidence with CAD, integration, and team-based design decisions."],
        "design": "Early drafts explored a lightweight frame with defined attachment points for electronics, landing structure, and payload hardware. The model was refined in SOLIDWORKS as interfaces became clearer.",
        "roadblocks": [{"title": "Interfaces", "text": "Mechanical decisions depended on components being developed by other subteams."}, {"title": "Weight", "text": "Each added bracket helped an attachment problem but affected the overall mass budget."}],
        "result": "A frame concept that gave the team a practical base for integrating the cargo-drone system.",
        "lessons": ["Communicate interfaces early and often.", "The simplest structure that meets the requirement is usually the best starting point."],
    },
    {
        "slug": "mobile-gestured-robotic-arm",
        "name": "Mobile Gestured Robotic Arm",
        "role": "Mechanical Engineer",
        "date": "December 2023 – June 2024",
        "image": "Mobile_Gestured_Robotic_Arm.png",
        "purpose": "Design a two-joint robotic arm that could mount to a team-built chassis and work with an end effector developed by other members.",
        "why": ["Translate a motion requirement into a functional mechanical system.", "Learn the fundamentals of collaborative CAD and physical prototyping."],
        "design": "The drafts focused on two degrees of freedom, link proportions, and joint mounting. The arm was modeled around the chassis envelope and revised as the team’s interface dimensions matured.",
        "roadblocks": [{"title": "Integration", "text": "The arm design had to remain compatible with evolving chassis and end-effector designs."}, {"title": "First-time learning curve", "text": "Learning CAD conventions and mechanism design at the same time made iteration essential."}],
        "result": "A foundational robotics project that turned early CAD practice into a functional system-level design experience.",
        "lessons": ["Start simple, then iterate with evidence.", "Good team projects depend on clear interface dimensions and shared deadlines."],
    },
]

# Card-front metadata mirrors the information shown on the current project page.
CARD_METADATA = {
    "vertical-suspension-test-rig": {"concepts": ["Suspension test rigs"], "softwares": ["SOLIDWORKS"]},
    "lateral-suspension-system": {"concepts": ["Spring-damper systems", "Damping ratios"], "softwares": ["SOLIDWORKS", "MATLAB / Simulink"]},
    "bell-crank-lateral-suspension": {"concepts": ["Spring-damper systems", "Damping ratios"], "softwares": ["SOLIDWORKS", "MATLAB / Simulink"]},
    "mars-rover-wheel-hub": {"concepts": ["Sheet-metal FEA", "Drive motor housings", "Wheel-material selection"], "softwares": ["SOLIDWORKS"]},
    "remote-controlled-cargo-drone": {"concepts": ["Drone mechanics"], "softwares": ["SOLIDWORKS"]},
    "mobile-gestured-robotic-arm": {"concepts": ["Arm mechanics"], "softwares": ["SOLIDWORKS"]},
}




@app.route("/")                                         #first page = home
def home():
    return render_template("home.html")                 #render_template(location or file)

@app.route("/connect")                                    #second page = about me section
def about():
    return render_template("connect.html")                #render_template(location or file)


for project in PROJECTS:
    project["overview"] = project["purpose"]
    project.update(CARD_METADATA[project["slug"]])


@app.route("/static/<path:filename>")
def portfolio_asset(filename):
    """Serve existing portfolio images without copying or changing them."""
    return send_from_directory(ROOT_DIR / "static", filename)


@app.route("/")
@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((item for item in PROJECTS if item["slug"] == slug), None)
    if project is None:
        abort(404)
    return render_template("project_detail.html", project=project)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
