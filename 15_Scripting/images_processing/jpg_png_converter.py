import os
import sys

from PIL import Image
"""
JPG to PNG converter

"""
print(end="\n\n")
src_folder = sys.argv[1]
dst_folder = sys.argv[2]


def png_converter(src, dst):

  # check if new folder exists, if not then create it.
  if not os.path.exists(dst):
    os.makedirs(dst_folder)

  else:
    # iterate over the entire newly created folder, and convert all images
    # to png.
    for filename in os.listdir(src):
      img = Image.open(f"{src}/{filename}")
    
     # split each files extension from it's filename
      if os.path.splitext(filename)[1] != ".png":
        split_img = os.path.splitext(filename)[0]
    
      img.save(f"{dst}/{split_img}.png", "png")

  return os.listdir(dst)


if __name__ == "__main__":
  print(png_converter(src_folder, dst_folder))

