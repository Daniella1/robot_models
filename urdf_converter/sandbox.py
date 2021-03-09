from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF
from mdh_to_urdf import mdh, MDH_to_URDF


if __name__ == '__main__':
    filename = 'urdf_converter/my_new_urdf.urdf'
    component_name = "my_ur_robot"
    
    base_dir = "../urdf/ur5_original/"

    default_meshes = True
    if default_meshes:
        visual_meshes = ["cube.dae", "cube1.dae", "cube.dae", "cube1.dae", "cube.dae", "cube1.dae", "cube.dae"]
        collision_meshes = None # ["cube1.stl" for _ in range(0,7)]
    else:
        visual_foldername = base_dir + "visual/"
        visual_meshes = ["base.dae", "forearm.dae", "shoulder.dae", "upperarm.dae", "wrist1.dae", "wrist2.dae", "wrist3.dae"]
        visual_meshes = [visual_foldername + f for f in visual_meshes]
        collision_foldername = base_dir + "collision/"
        collision_meshes = ["base.stl","forearm.stl","shoulder.stl","upperarm.stl","wrist1.stl","wrist2.stl","wrist3.stl"]
        collision_meshes = [collision_foldername + f for f in collision_meshes]
    
    my_mdh_params = [mdh(d=15.19),
                    mdh(alpha=pi/2),
                    mdh(a=-24.35),
                    mdh(a=-21.32,d=13.10),
                    mdh(alpha=pi/2, d=8.53),
                    mdh(alpha=-pi/2, d=9.21)]

    MDH_to_URDF(filename, component_name, my_mdh_params, visual_meshes, collision_meshes)

    #filename = "urdf/ur5_original/ur5.urdf"
    robot = URDF.load(filename)

    robot.show(use_collision=False)

