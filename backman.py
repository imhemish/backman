#!/usr/bin/env python3
from subprocess import Popen as pp
from os import mkdir
from os.path import exists
from toml import load, dump
from os.path import expanduser as exp
import os
from argparse import ArgumentParser as argvp

template_config = {
        "mode": "random", # Other is fixed
        "directories": ["",],
        "fix_bg": ""
        }

# Dump configs if dont exist
def check_configs(template_config):
    if not exists(exp("~/.config/backman.toml")):
        filenew = open(exp("~/.config/backman.toml"), "a")
        dump(template_config, filenew)
        filenew.close()

# Read Configs
def read_configs():
    return load(exp("~/.config/backman.toml"))

def save_configs(config_dict):
    filenew = open(exp("~/.config/backman.toml"), "w")
    dump(config_dict, filenew)
    filenew.close()

def get_list_of_files(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        

def is_image(filepath):
    exts = ["png", "jpg", "jpeg"]
    for item in exts:
        if filepath.endswith("."+item):
            return True

def pick_random(directories_list):
    from random import choice

    imgs_list = []
    for item in directories_list:
        imgs = list(filter(is_image, get_list_of_files(item)))
        imgs_list = imgs_list + imgs

    return choice(imgs_list)

def set_bg(path):
    os.system("pkill swaybg")
    pp(["setsid", "swaybg", "-i", path])

def change_mode(mode):
    if mode in ["fixed", "random"]:
        config = read_configs()
        config["mode"] = mode
        save_configs(config)

def set_fix_bg(path):
    if exists(path):
        config = read_configs()
        config["fix_bg"] = path
        save_configs(config)

def add_directory(path):
    if exists(path):
        config = read_configs()
        config["directories"] = config["directories"] + [path,]
        save_configs(config)

def remove_directory(path):
    config = read_configs()
    if path in config["directories"]:
        list_directories = config["directories"]
        list.remove(path)
        config["directories"] = list_directories
        save_configs(config)

def return_img_to_set():
    config = read_configs()
    if config["mode"] == "fixed":
        return config["fix_bg"]
    elif config["mode"] == "random":
        return pick_random(config["directories"])

def set():
    set_bg(return_img_to_set)

def main():
    ap = argvp(description="Set backgrounds in sway and other wlroot based compositors, either random background image or fixed")
    ap.add_argument("--set", "-s", required=False, help="Set the background, either random or fixed (as specified in configuration)")
    ap.add_argument("--return", "-r", required=False, help="Return the path of background that would be set, either random or fixed")
    ap.add_argument("--change-mode", "-m", required=False, nargs=1)
    ap.add_argument("--set-fix-bg", "-i", required=False, nargs=1)
    ap.add_argument("--add-dir", required=False, nargs=1)
    ap.add_argument("--rm-dir", required=False, nargs=1)

if __name__ == "__main__":
    main()
