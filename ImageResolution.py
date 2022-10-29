from PIL import Image

zoom_ratio = 8

image_file = Image.open("HEAT_IMG\OUT\Area.png")
h, w = image_file.size
size = h * zoom_ratio, w * zoom_ratio
im_resized = image_file.resize(size, Image.ANTIALIAS)
im_resized.save("HEAT_IMG\OUT\diskheat.png", "PNG")
