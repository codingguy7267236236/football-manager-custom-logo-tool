# Importing libraries
import os
from PIL import Image

# folder locations
imgFld = "E:/Python/football-manager-custom-logo-tool-main/football-manager-custom-logo-tool-main/logos" # images for the teams must map to in game id to display correctly.
graphics = "E:/Documents/Sports Interactive/Football Manager 2023/graphics/logos/" # replace with path to your fm graphics folder

# function to resize image graphics for football manager ui
def ResizeImages():
    # contains structure for the config file
    configTxt = '''<record>
	<!-- resource manager options -->
	<boolen id="preload" value="false"/>
	<boolen id="map" value="false"/>
	<!--Logo mapping section this is where images go-->
	<list id="maps">'''
    
    fmTxt = "" # used to hold the config records data

    # going through all images in the folder to resize and then add record
    for images in os.listdir(imgFld):
        if(images.endswith(".png")):
            img = Image.open(f"{imgFld}/{images}")

            # setting size dimensions for the icon and logo of the club
            logoSize = (180,180)
            iconSize = (18,18)

            # resizing the original image for both icon and logo files needed in game
            icon = img.resize(iconSize)
            icon.save(f"{graphics}smll{images}")
            logo = img.resize(logoSize)
            logo.save(f"{graphics}big{images}")
            
            # getting club id from image filename (this is because the clubs logo image should be their in-game id)
            id = images.split(".")[0]

            # adding the config data for setting the 
            fmTxt += f'<record from="smll{id}" to="graphics/pictures/club/{id}/icon"/>\n'
            fmTxt += f'<record from="big{id}" to="graphics/pictures/club/{id}/logo"/>\n'
            
    # add the fmTxt containing team logo mapping records to config contents
    configTxt += fmTxt
    # closing the config file elements of list and record
    configTxt += '''</list>
    </record>'''
    ###saving txt to config.xml file which can then be copied to the fm graphics folder. 
    # (done this way to ensure no rewriting of existing config files in graphics folder) allows user to backup existing or
    # allow user to paste the records inside <list></list> into pre-existing config file
    with open("config.xml","w") as txt:
        txt.write(configTxt)
        txt.close()

ResizeImages()
