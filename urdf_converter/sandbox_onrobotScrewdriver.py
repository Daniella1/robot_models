from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF
from mdh_to_urdf import mdh, MDH_to_URDF


if __name__ == '__main__':
    
    base_dir = ""

    default_meshes = False
    if default_meshes:
        visual_meshes = ["rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae"]
        collision_meshes = None
    else:
        visual_foldername = base_dir + "visual/"
        visual_meshes = ["body.dae", "shank_bit.dae"]
        visual_meshes = [visual_foldername + f for f in visual_meshes]
        collision_foldername = base_dir + "collision/"
        collision_meshes = ["body.stl", "shank_bit.stl"]
        collision_meshes = [collision_foldername + f for f in collision_meshes]
    

    # [m]
    screwdriver_mdh = [mdh(joint_type="prismatic")] # 


    filename = 'models/onrobot_screwdriver/test2/onrobot_screwdriver.urdf'
    component_name = "my_onrobot_screwdriver"
    #MDH_to_URDF(filename, component_name, screwdriver_mdh, visual_meshes, collision_meshes)

    robot = URDF.load(filename)
    #robot.show(use_collision=False)
    robot.animate()
