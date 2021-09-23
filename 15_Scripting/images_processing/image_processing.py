from PIL import Image, ImageFilter

my_image = Image.open("./files/astro.jpg")

# to keep the aspect ratio of the image, we use .thumbnail.
# .thumbnail() modifies the original image, no need to define a new variable and save.
my_image.thumbnail((600, 300))
my_image.save("./files/astro_thumbnail.png", "png")

my_image.show()
