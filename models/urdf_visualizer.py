from urdfpy import URDF, Link, Joint, Transmission, Material


filename = "ur5e_technicon/test3/test3_technicon_ur5e.urdf"
filename = "ur5e_joint_test/ur5e_joint_test.urdf"
filename = "ur5e_screwdriver/ur5e_screwdriver.urdf"

robot = URDF.load(filename)

# print("----LINKS----")
# for link in robot.links:
#     print(link.name)

# print("----ACTUATED JOINTS----")
# for joint in robot.actuated_joints:
#     print(joint.name)


#robot.animate(use_collision=True)

robot.show(use_collision=False, cfg={'joint0': 0.0, 
                                    'joint1': 0.0,
                                    'joint2': 0.0,
                                    'joint3': 0.0,
                                    'joint4': 0.0,
                                    'joint5': 0.0,
                                    'joint7': 0.055,
                                    })
