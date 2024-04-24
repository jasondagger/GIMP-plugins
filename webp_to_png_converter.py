#!/usr/bin/env python

import math
import os
from gimpfu import *



def convert_webps_to_pngs(path):

    # grab files within folders
    files = []
    for f in os.listdir(path):
        filePath = os.path.join(path, f)
        if os.path.isfile(filePath):
            files.append(filePath)
            
    for file in files:
        image = pdb.file_webp_load(file, file)
        os.remove(file)
        drawable = pdb.gimp_image_get_active_drawable(image)
        file = file.replace("webp", "png")
        pdb.file_png_save_defaults(image, drawable, file, file)



register(
    "python-fu-convert_webps_to_pngs",
    "Converts .webp extensions to .png extensions",
    "Converts .webp extensions to .png extensions",
    "Jason Dagger",
    "Jason Dagger",
    "2024",
    "WEBPs to PNGs",
    "",
    [
        (PF_STRING, "path", "Folder Path:", "Path")
    ],
    [],
    convert_webps_to_pngs,
    menu="<Image>/Image/Scripts/Convert"
)



main()