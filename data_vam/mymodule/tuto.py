import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import skip_check
    from check import out_check
    from function_game import click_pos_2

    try:
        print("tuto_start")
        skip_check(cla)

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\tuto\\quest_check\\quest_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 780, 960, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_btn", imgs_)
            else:
                click_pos_2(800, 90, cla)


    except Exception as e:
        print(e)