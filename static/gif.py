from pathlib import Path

from PIL import Image, ImageOps

static_dir = Path(__file__).parent

image_paths = [
    static_dir / "Tristan.jpg",
    static_dir / "HX_DYNAMICS_SUBTEAM.jpg",
    static_dir / "HX_11.jpg",
    static_dir / "ASME_HEADSHOT.jpg",
    static_dir / "asme_2026.jpg",
    
]

first_frame = Image.open(image_paths[0]).convert("RGB")
frame_size = ImageOps.contain(first_frame, (1200, 800)).size
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