from PIL import Image, ImageFilter

# opening an image file using Image
im = Image.open('./files/pikachu.jpg')

print(im)


# display image format
print(im.format)

# display image size
print(im.size)

# display image mode
print(im.mode)

print("")

# add blur effect to the image file
filtered_img = im.filter(ImageFilter.BLUR)

# save image
filtered_img.save("./files/blur.png", "png")

# smooth images squirtle.jpg

squirtle = Image.open("./files/squirtle.jpg")

smooth_squirtle = squirtle.filter(ImageFilter.SMOOTH)
smooth_squirtle.save("./files/squirtle_smooth.png", "png")


# image convert
squirtle_gray = squirtle.convert("L")
squirtle_gray.rotate(90)


# rotate
# for rotate to work, we need to save the images in a new variable.
rotate = squirtle_gray.rotate(90)

rotate.save("./files/rotate.png", "png")

squirtle_gray.save("./files/squirtle_gray.png", "png")


# display image file to the user
squirtle_gray.show()

# resize
new_size = filtered_img.resize((400, 200))
new_size.save("./files/resize.png", "png")
