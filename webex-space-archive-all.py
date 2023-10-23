# -*- coding: utf-8 -*-
import json
from os import path as osp
from subprocess import run
import configparser


CONFIG_FILE_IN = "webexspacearchive-config.ini"
CONFIG_FILE_OUT = "my_webexspacearchive-config.ini"
JSON_FILE = "rooms.json"
CURR_DIR = osp.dirname(__file__)

config = configparser.ConfigParser()
config.read(osp.join(CURR_DIR, CONFIG_FILE_IN))
section = config["Archive Settings"]

with open(osp.join(CURR_DIR, JSON_FILE), "r") as fin:
    rooms = json.load(fin)
    for room in rooms["items"]:
        section["myspaceid"] = room["id"]
        with open(osp.join(CURR_DIR, CONFIG_FILE_OUT), "w") as configfile:
            config.write(configfile)
        run(
            [
                "py",
                "-3",
                osp.join(CURR_DIR, "webex-space-archive.py"),
                osp.join(CURR_DIR, CONFIG_FILE_OUT),
            ]
        )
