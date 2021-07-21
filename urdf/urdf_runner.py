from urdfpy import URDF, Link, Joint, Transmission, Material


#filename = "ur5_original/ur5.urdf"
#filename = "ur5e_test/ur5.urdf"
robot = URDF.load(f'urdf/{filename}')

# print("----LINKS----")
# for link in robot.links:
#     print(link.name)

# print("----ACTUATED JOINTS----")
# for joint in robot.actuated_joints:
#     print(joint.name)


#robot.animate(use_collision=True)

robot.show(use_collision=True)
