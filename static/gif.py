from pathlib import Path

from PIL import Image, ImageOps

static_dir = Path(__file__).parent

image_paths = [
    static_dir / "Tristan.jpg",
    static_dir / "HX_DYNAMICS_SUBTEAM.jpg",
    static_dir / "UCI_LEGACY_SUBTEAM.jpg",
    static_dir / "LeDrone_Pic.jpg",
]

first_frame = Image.open(image_paths[0]).convert("RGB")
frame_size = first_frame.size
frames = []

for path in image_paths:
    image = Image.open(path).convert("RGB")
    image = ImageOps.contain(image, frame_size)
    frame = Image.new("RGB", frame_size, "white")
    frame.paste(image, ((frame_size[0] - image.width) // 2, (frame_size[1] - image.height) // 2))
    frames.append(frame)

frames[0].save(
    static_dir / "intro.gif",
    save_all=True,
    append_images=frames[1:],
    duration=1500,
    loop=0,
)