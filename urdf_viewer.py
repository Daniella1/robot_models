from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF




if __name__ == '__main__':

    filename = 'models/ur5e_technicon/test3/test3_technicon_ur5e.urdf'

    robot = URDF.load(filename)

    #robot.show(use_collision=False)
    robot.animate()