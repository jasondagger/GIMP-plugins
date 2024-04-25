#!/usr/bin/env python

import math
from gimpfu import *



def export_etsy_mockup_collections_7_phones(path):

    # load mockup
    mockup_path = r"D:\Portfolio\Etsy\Product\Phone\MockUp\7\mockup_phones.xcf"
    image = pdb.gimp_xcf_load(0, mockup_path, mockup_path)
    #pdb.gimp_display_new(image)



    # load phone mockups
    phone_layer_names = {
        0:"iphone15promax_7.jpg", # front right
        1:"galaxys24ultra_6.jpg", # front center right
        2:"pixel8pro_5.jpg",      # front center left
        3:"iphone14promax_4.jpg", # front left
        4:"iphone13promax_3.jpg", # back right
        5:"galaxys23ultra_2.jpg", # back center
        6:"pixel7_1.jpg",         # back left
    }
    for i in range(7):
        
        # add mockup to display
        phone_mockup_path = path + "\\" + phone_layer_names.get(i)
        layer = pdb.gimp_file_load_layer(image, phone_mockup_path)
        pdb.gimp_image_insert_layer(image, layer, None, -1)

        # change name
        target_phone_layer_name = "base " + phone_layer_names.get(i)
        pdb.gimp_item_set_name(layer, target_phone_layer_name)



    # retrieve collection layer
    collection_layer_name = "collection"
    target_layer_collection = pdb.gimp_image_get_layer_by_name(image, collection_layer_name)



    # get background
    background_layer = pdb.gimp_image_get_layer_by_name(image, "background")
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, background_layer)

    # copy & paste the background
    pdb.gimp_edit_copy(background_layer)
    floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
    pdb.gimp_floating_sel_anchor(floating_layer)



    # copy shadow
    target_shadow_layer = pdb.gimp_image_get_layer_by_name(image, "shadow")
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, target_shadow_layer)

    # copy & paste the shadow
    pdb.gimp_edit_copy(target_shadow_layer)
    floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
    pdb.gimp_floating_sel_anchor(floating_layer)

    
    
    translationXs = {
        0:0, 
        1:0, 
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    translationYs = {
        0:0, 
        1:0, 
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    widths = {
        0:0, 
        1:0, 
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    heights = {
        0:0, 
        1:0, 
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    rotations = {
        0:0, 
        1:0, 
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    cutout_layer_names = {
        0:"cutout iphone15promax", 
        1:"cutout galaxys24ultra", 
        2:"cutout pixel8pro",
        3:"cutout iphone14promax",
        6:"cutout iphone13promax",
        4:"cutout galaxys23ultra",
        5:"cutout pixel7",
    }
    for i in range(7):

        # get cutout selection
        cutout_layer = pdb.gimp_image_get_layer_by_name(image, cutout_layer_names.get(i))
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, cutout_layer)
        
        # get layer
        phone_layer = pdb.gimp_image_get_layer_by_name(image, "base " + phone_layer_names.get(i))
        cutout_layer_name = "cutout " + phone_layer_names.get(i)
        target_phone_layer_cutout = pdb.gimp_image_get_layer_by_name(image, cutout_layer_name)

        # copy & paste the cutout
        pdb.gimp_edit_copy(phone_layer)
        floating_layer = pdb.gimp_edit_paste(target_phone_layer_cutout, True)
    
        # scale layer to appropriate size
        width = widths.get(i)
        height = heights.get(i)
        pdb.gimp_layer_scale(floating_layer, width, height, True)

        # anchor & move to position
        pdb.gimp_floating_sel_anchor(floating_layer)
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, target_phone_layer_cutout)
        pdb.gimp_item_transform_translate(target_phone_layer_cutout, translationXs.get(i), translationYs.get(i))
        
        # rotate layer
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, target_phone_layer_cutout)
        floating_layer = pdb.gimp_item_transform_rotate(target_phone_layer_cutout, math.radians(rotations.get(i)), True, 0, 0)
        pdb.gimp_floating_sel_anchor(floating_layer)
    


    # move cutouts to export layer
    phone_layer_names_sorted = {
        0:"pixel7_1.jpg",         # back left
        1:"galaxys23ultra_2.jpg", # back center
        2:"iphone13promax_3.jpg", # back right
        3:"iphone14promax_4.jpg", # front left
        4:"pixel8pro_5.jpg",      # front center left
        5:"galaxys24ultra_6.jpg", # front center right
        6:"iphone15promax_7.jpg", # front right
    }
    for i in range(7):
        
        # get new cutout back layer
        cutout_layer_name = "cutout " + phone_layer_names_sorted.get(i)
        cutout_layer = pdb.gimp_image_get_layer_by_name(image, cutout_layer_name)
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, cutout_layer)
    
        # copy & paste the cutout
        pdb.gimp_edit_copy(cutout_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)
    
    
    
    # export out final image
    file_name = path + "\\_cover.png"
    pdb.file_png_save_defaults(image, target_layer_collection, file_name, file_name)



def export_etsy_mockup_collections_7_showcases(path):

    # load mockup
    mockup_path = r"D:\Portfolio\Etsy\Product\Phone\MockUp\7\mockup_showcases.xcf"
    image = pdb.gimp_xcf_load(0, mockup_path, mockup_path)



    # load phone mockups
    phone_layer_names = {
        0: "pixel8pro_1.jpg", 1: "galaxys24ultra_1.jpg", 2: "iphone15promax_1.jpg",
        3: "pixel8pro_2.jpg", 4: "galaxys24ultra_2.jpg", 5: "iphone15promax_2.jpg",
        6: "pixel8pro_3.jpg", 7: "galaxys24ultra_3.jpg", 8: "iphone15promax_3.jpg",
        9: "pixel8pro_4.jpg", 10:"galaxys24ultra_4.jpg", 11:"iphone15promax_4.jpg",
        12:"pixel8pro_5.jpg", 13:"galaxys24ultra_5.jpg", 14:"iphone15promax_5.jpg",
        15:"pixel8pro_6.jpg", 16:"galaxys24ultra_6.jpg", 17:"iphone15promax_6.jpg",
        18:"pixel8pro_7.jpg", 19:"galaxys24ultra_7.jpg", 20:"iphone15promax_7.jpg",
    }
    for i in range(21):
        
        # add mockup to display
        phone_mockup_path = path + "\\" + phone_layer_names.get(i)
        layer = pdb.gimp_file_load_layer(image, phone_mockup_path)
        pdb.gimp_image_insert_layer(image, layer, None, -1)

        # change name
        target_phone_layer_name = "base " + phone_layer_names.get(i)
        pdb.gimp_item_set_name(layer, target_phone_layer_name)



    # retrieve collection layer
    collection_layer_name = "collection"
    target_layer_collection = pdb.gimp_image_get_layer_by_name(image, collection_layer_name)



    # create cut outs of phone sides
    translationXs = {
        0:-276, 
        1:-1, 
        2:432
    }
    translationYs = {
        0:-18, 
        1:42, 
        2:102
    }
    widths = {
        0:407, 
        1:419, 
        2:422
    }
    heights = {
        0:831, 
        1:831, 
        2:830
    }
    cutout_layer_names = {
        0:"cutout pixel8pro", 
        1:"cutout galaxys24ultra", 
        2:"cutout iphone15promax"
    }
    for showcaseId in range(7):

        # get background
        background_layer = pdb.gimp_image_get_layer_by_name(image, "background")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, background_layer)

        # copy & paste the background
        pdb.gimp_edit_copy(background_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get shadow iphone
        shadow_iphone_layer = pdb.gimp_image_get_layer_by_name(image, "shadow iphone15promax")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, shadow_iphone_layer)

        # copy & paste the shadow
        pdb.gimp_edit_copy(shadow_iphone_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get shadow galaxy
        shadow_galaxy_layer = pdb.gimp_image_get_layer_by_name(image, "shadow galaxys24ultra")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, shadow_galaxy_layer)

        # copy & paste the shadow
        pdb.gimp_edit_copy(shadow_galaxy_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get shadow pixel
        shadow_pixel_layer = pdb.gimp_image_get_layer_by_name(image, "shadow pixel8pro")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, shadow_pixel_layer)

        # copy & paste the shadow
        pdb.gimp_edit_copy(shadow_pixel_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get logo iphone
        logo_iphone_layer = pdb.gimp_image_get_layer_by_name(image, "logo iphone")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, logo_iphone_layer)

        # copy & paste the logo
        pdb.gimp_edit_copy(logo_iphone_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get logo galaxy
        logo_galaxy_layer = pdb.gimp_image_get_layer_by_name(image, "logo galaxy")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, logo_galaxy_layer)

        # copy & paste the logo
        pdb.gimp_edit_copy(logo_galaxy_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        # get logo pixel
        logo_pixel_layer = pdb.gimp_image_get_layer_by_name(image, "logo pixel")
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, logo_pixel_layer)

        # copy & paste the logo
        pdb.gimp_edit_copy(logo_pixel_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)



        for mockupId in range(3):
            index = showcaseId * 3 + mockupId

            # get cutout selection
            cutout_layer = pdb.gimp_image_get_layer_by_name(image, cutout_layer_names.get(mockupId))
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, cutout_layer)

            # get layer
            phone_layer = pdb.gimp_image_get_layer_by_name("base " + image, phone_layer_names.get(index))
            cutout_layer_name = "cutout " + phone_layer_names.get(index)
            target_phone_layer_cutout = pdb.gimp_image_get_layer_by_name(image, cutout_layer_name)

            # copy & paste the cutout
            pdb.gimp_edit_copy(phone_layer)
            floating_layer = pdb.gimp_edit_paste(target_phone_layer_cutout, True)

            # scale layer to appropriate size
            width = widths.get(mockupId)
            height = heights.get(mockupId)
            pdb.gimp_layer_scale(floating_layer, width, height, True)

            # anchor & move to position
            pdb.gimp_floating_sel_anchor(floating_layer)
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, target_phone_layer_cutout)
            pdb.gimp_item_transform_translate(target_phone_layer_cutout, translationXs.get(mockupId), translationYs.get(mockupId))

            # copy & paste to final image
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, target_phone_layer_cutout)
            pdb.gimp_edit_copy(target_phone_layer_cutout)
            floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
            pdb.gimp_floating_sel_anchor(floating_layer)



        # get number layer
        number_layer = pdb.gimp_image_get_layer_by_name(image, "number " + str(showcaseId + 1))
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, number_layer)

        # copy & paste the number
        pdb.gimp_edit_copy(number_layer)
        floating_layer = pdb.gimp_edit_paste(target_layer_collection, True)
        pdb.gimp_floating_sel_anchor(floating_layer)

        # export out final image
        file_name = path + "\\_showcase" + str(showcaseId + 1) + ".png"
        pdb.file_png_save_defaults(image, target_layer_collection, file_name, file_name)




def export_etsy_mockup_collections_7(path):
    export_etsy_mockup_collections_7_phones(path)
    export_etsy_mockup_collections_7_showcases(path)



register(
    "python-fu-export_etsy_mockup_collections_7",
    "Exports Etsy mockup collections of 7 phones",
    "Exports Etsy mockup collections of 7 phones",
    "Jason Dagger",
    "Jason Dagger",
    "2024",
    "Export Collection 7",
    "",
    [
        (PF_STRING, "path", "Folder Path:", "Path"),
    ],
    [],
    export_etsy_mockup_collections_7,
    menu="<Image>/Image/Scripts/Etsy"
)



main()