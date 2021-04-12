from urdfpy import URDF, Link, Joint, Transmission, Material


filename = "onrobot_screwdriver/onrobot_screwdriver.urdf"
robot = URDF.load(f'urdf/{filename}')

# print("----LINKS----")
# for link in robot.links:
#     print(link.name)

# print("----ACTUATED JOINTS----")
# for joint in robot.actuated_joints:
#     print(joint.name)


#robot.animate(use_collision=False)

robot.show(use_collision=True)
