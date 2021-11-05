# backman
Backman is a random/fixed background image setter for major GTK desktops, X11, sway and other wlroots based wayland compositors

# Supported
Backman is tested to work on i3, sway, GNOME (Wayland), GNOME (Xorg), Cinnamon, XFCE, Budgie. It may also work on other platforms but is not tested.

# Dependencies:
The program depends on swaybg, python3-toml (or python-toml), python3, hsetroot, bash

# Installation:
Meet the required dependencies and run the provided "install" script like this:   
```bash
sudo ./install   
```  
Prepending the install script with "sudo" or executing in super user environment is required.
  
If you are using Arch Linux, there is an AUR package, called "backman". You can install by cloning or using an AUR helper.  
   
# Configuration
The configuration for backman resides at ~/.config/backman.toml The configuration follows the toml markup. The configuration contains three options:
- mode: this parameter can have two values, "fixed" and "random". The "fixed" option is used to have a single image as your background. The "random" option picks a random picture from your specified directories (defined in next configuration paratemer)   
- directories: this paramater is list type. For "random" feature to work, you have to specify directories which would be looked for pictures. Take care that you have to add full path and you can not add such values: "~/Pictures". You have to specify like "/home/user/Pictures"   
- fix_bg: this parameter should contain full path to an image. For "fixed" feature to work, you have to specify a fixed image to be set as background each time   
   
Example configuration 1:   
mode = "random"   
directories = [ "/home/cat/pix/bg", "/usr/share/backgrounds" ]   
fix_bg = "/home/cat/pix/bg/btwarch-black.png"   
   
Example configuration 2:
mode = "fixed"   
directories = [ "/home/cat/pix/bg", "/usr/share/backgrounds" ]   
fix_bg = "/home/cat/pix/bg/btwarch-black.png"   
  
Also note that you can also change these configurations without actually editing the configuration file, itself inside the program. See usage for knowing how.   

# Usage
usage: backman [-h] [--set] [--return-path] [--change-mode CHANGE_MODE] [--set-fix-bg SET_FIX_BG][--add-dir ADD_DIR]    
               [--rm-dir RM_DIR] [--list-dirs] [--toggle-mode]     
    
Backman is a random/fixed background image setter for major GTK desktops, X11, sway and other wlroots based wayland compositors    
    
optional arguments:    
  -h, --help            show this help message and exit    
  --set, -s             Set the background, either random or fixed (as specified in configuration)   
  --return-path, -r     Return the path of background that would be set, either random or fixed   
  --change-mode CHANGE_MODE, -m CHANGE_MODE   
                        Change mode to specified as arguement   
  --set-fix-bg SET_FIX_BG, -i SET_FIX_BG   
                        Set fixed background image in configuration   
  --add-dir ADD_DIR     Add a directory to configuration   
  --rm-dir RM_DIR       Remove a directory from configuration   
  --list-dirs, -l       List directories specified in configuration   
  --toggle-mode, -t     Toggle modes between fixed and random   

- The --set flag instructs the program to set the background (either fixed or random, as specified in configuration)
- The --return-path flag instructs the program to return the path of background image to be set (either fixed or random, as specified in configuration)
- The --change-mode parameter can change the modes between fixed and random   
 For example, to change the mode to fixed, you can execute:   
```bash
backman -m fixed   
```   
To change to random, you can execute:   
```bash
backman -m random   
```   
- The --toggle-mode flag instructs the program to toggle the mode between fixed and random.   
Example:   
```bash
backman -t   
```   
- The --set-fix-bg paramter can be used to set the fixed background image for "fixed" mode.   
For example, to set the image: /home/user/Pictures/1.jpg as fixed background image, you can execute:   
```bash
backman -i /home/user/Pictures/1.jpg   
```   
- The --add-dir and --rm-dir can be respectively used to add and remove directories from directories configuration.   
For example, to remove "/home/user/Pictures" directory and add "/usr/share/backgrounds" directory, you can execute:   
```bash
backman --add-dir /usr/share/backgrounds --rm-dir /home/user/Pictures   
```   
- The --list-dirs can be used to list all directories specified in the configuration.   

# Warnings
The program prints out warnings to sterr. So, if you want to pipe or use the output of the program's stdout, you would need to send the sterr to /dev/null   
Example:   
backman -r 2>/dev/null  

# Reminder and tip
The background set by this script (or swaybg) is not persistent across logout and logins in standalone window managers. It just disappears after quitting compositor/window manager. To have a persistent feel, add the following command to your autostart script (maybe in your window manager/compositor configuration):   
```bash
backman -s 2>/dev/null  
```  

# License
This program is licensed under MIT license

# Thanks
The project waves out a great thanks to sway team for developing swaybg and hsetroot developer Martin Hradil.  
The licenses of both the projects should be respected and followed.  
