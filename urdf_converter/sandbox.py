from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF
from mdh_to_urdf import mdh, MDH_to_URDF


if __name__ == '__main__':
    
    
    #base_dir = "../models/eSeries_UR5e/"
    base_dir = ""
    #base_dir = "../../urdf/ur5e_test/"
    #base_dir ="../urdf/ur5_original/"

    default_meshes = True
    if default_meshes:
        #visual_meshes = ["cube.dae", "cube1.dae", "cube.dae", "cube1.dae", "cube.dae", "cube1.dae", "cube.dae"]
        visual_meshes = ["rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae", "rect.dae"]
        collision_meshes = None # ["cube1.stl" for _ in range(0,7)]
    else:
        visual_foldername = base_dir + "visual/"
        #visual_meshes = ["base.dae", "forearm.dae", "shoulder.dae", "upperarm.dae", "wrist1.dae", "wrist2.dae", "wrist3.dae"]
        visual_meshes = ["0_base.dae","1_shoulder.dae", "2_forearm.dae", "3_upperarm.dae", "4_wrist1.dae", "5_wrist2.dae", "6_wrist3.dae"]
        visual_meshes = [visual_foldername + f for f in visual_meshes]
        collision_foldername = base_dir + "collision/"
        #collision_meshes = ["base.stl","forearm.stl","shoulder.stl","upperarm.stl","wrist1.stl","wrist2.stl","wrist3.stl"]
        collision_meshes = ["0_base.stl","1_shoulder.stl","2_forearm.stl","3_upperarm.stl","4_wrist1.stl","5_wrist2.stl","6_wrist3.stl"]
        collision_meshes = [collision_foldername + f for f in collision_meshes]
        #collision_meshes = None
    
    # [cm]
    ur3e_mdh = [mdh(d=15.19),
                    mdh(alpha=pi/2),
                    mdh(a=-24.35),
                    mdh(a=-21.32,d=13.10),
                    mdh(alpha=pi/2, d=8.53),
                    mdh(alpha=-pi/2, d=9.21)]

    # [cm]
    # ur5e_mdh = [mdh(d=16.25),
    #                 mdh(alpha=pi/2),
    #                 mdh(a=-42.5),
    #                 mdh(a=-39.22,d=13.33),
    #                 mdh(alpha=pi/2, d=9.97),
    #                 mdh(alpha=-pi/2, d=9.96)]
    # [m]
    # ur5e_mdh = [mdh(d=0.1625),
    #             mdh(alpha=pi/2), # 
    #             mdh(a=-0.425), 
    #             mdh(a=-0.3922,d=0.1333),
    #             mdh(d=0.0997, alpha=pi/2), # 
    #             mdh(d=0.0996, alpha=-pi/2)] # 

    # MANUALLY MODIFIED PARAMS[m]
    ur5e_mdh = [mdh(d=0.1625),
                mdh(alpha=pi/2), # 
                mdh(a=-0.425), 
                mdh(a=-0.3922,d=0.1333),
                mdh(d=0.0997, alpha=pi/2), # 
                mdh(d=0.0996, alpha=-pi/2)] # 


    # ur5e_mdh = [mdh(),
    #             mdh(),
    #             mdh(),
    #             mdh(),
    #             mdh(),
    #             mdh()]


    #filename = 'models/ur5e_technicon/test2/test2_technicon_ur5e.urdf'
    filename = 'models/ur5e_technicon/test3/test3_technicon_ur5e.urdf'
    component_name = "my_ur_robot"
    #MDH_to_URDF(filename, component_name, ur5e_mdh, visual_meshes, collision_meshes)

    #filename = "urdf/ur5e_test/ur5.urdf"
    #filename = 'models/ur5e_technicon/test1_with_space_to_origin/technicon_ur5e_empty_dh.urdf'
    #filename = "models/ur5e_technicon/test2/test2_technicon_ur5e.urdf"
    robot = URDF.load(filename)

    robot.show(use_collision=False)
    #robot.animate()
