from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF
from mdh_to_urdf import mdh, MDH_to_URDF


if __name__ == '__main__':
    
    base_dir = ""

    default_meshes = True
    if default_meshes:
        visual_meshes = ["rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae"]
        collision_meshes = None # ["cube1.stl" for _ in range(0,7)]
    else:
        visual_foldername = base_dir + "visual/"
        visual_meshes = ["0_base.dae","1_shoulder.dae", "2_forearm.dae", "3_upperarm.dae", "4_wrist1.dae", "5_wrist2.dae", "6_wrist3.dae"]
        visual_meshes = [visual_foldername + f for f in visual_meshes]
        collision_foldername = base_dir + "collision/"
        collision_meshes = ["0_base.stl","1_shoulder.stl","2_forearm.stl","3_upperarm.stl","4_wrist1.stl","5_wrist2.stl","6_wrist3.stl"]
        collision_meshes = [collision_foldername + f for f in collision_meshes]



    ur5e_mdh = [mdh(),
                mdh(),
                mdh(),
                mdh(),
                mdh(),
                mdh()]


    filename = 'models/complete_ur5e_stl/complete_ur5e.urdf'
    component_name = "my_ur_robot"
    MDH_to_URDF(filename, component_name, ur5e_mdh, visual_meshes, collision_meshes)

    robot = URDF.load(filename)

    robot.show(use_collision=False)
    #robot.animate()
