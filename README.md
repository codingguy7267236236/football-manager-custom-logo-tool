# Football Manager Custom Logo tool
Tool to quickly configure logos for clubs in football manager by simply creating or getting an image for the club logo, placing it in a folder with any others to add to the game and then let the program do all the resizing needed for the game and create the config elements needed to then manually add in the config.xml file.

## Steps
- Place your desired logos in a folder (make sure the name of the file corresponds to the team id in game)
- Set the logo folder (imgFld variable in the code) to the path to the folder containing your custom logos
- Set the graphics variable in the code to point to your fm graphics folder.
- Run the code - this will now create the required image sizes in your fm graphics folder and output a config file in the folder you stored the orignal logos in.
- Copy your config file into your graphics folder so that fm can understand the mappings. (Done this why to ensure you move any pre-existing config files and not have the code overwrite it)

If you already have a config file for graphics and just want to add new records then just copy everything inside of <list></list> and paste it inside your current config file.
