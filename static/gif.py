from PIL import Image

image_paths = [
    "static/Tristan.jpg",
    "static/Tristan_HX_HEADSHOT.jpg",
    "static/Tristan_TTMExpo",
    "static/TTM_Intern_Expo_Photo",
    "static/HX_DYNAMICS_SUBTEAM",
    "static/UCI_LEGACY_SUBTEAM",
]

frames = [Image.open(path).convert("RGB") for path in image_paths]

frames[0].save(
    "static/intro.gif"
    save_all=True
    append_images=frames[1:]
    duration=1500
    loop=0
)