from lxml import etree as ET
from typing import List
from math import pi, sin, cos

# For visualiztion of urdf file
from urdfpy import URDF


class Joint:

    def __init__(self, name, type, parent_link_name, child_link_name, d, theta, alpha, a):
        self.name = name
        self.type = type
        joint_types = {"revolute", "prismatic"}
        if type not in joint_types:
            raise AttributeError(f"The type of the joint given, is {type}, but must be one of the following types: {joint_types}")
        self.parent_link_name = parent_link_name
        self.child_link_name = child_link_name
        self.d = d
        self.theta = theta
        self.alpha = alpha
        self.a = a


class Link:

    def __init__(self, name, visual_filename, visual_material_name, visual_rgba, collision_filename):
        self.name = name
        self.visual_filename = visual_filename
        self.visual_material_name = visual_material_name
        self.visual_rgba = visual_rgba
        self.collision_filename = collision_filename


class MDH_to_URDF:

    def __init__(self, component_name: str, links: List[Link], joints: List[Joint], output_file: str):
        
        if (len(links) - 1) != len(joints):
            raise AttributeError("The provided amount of Links must be one larger than the provided amount of Joints.")
        
        self.robot_name = component_name
        self.xml_robot = ET.Element("robot", name=component_name)
        self.urdf_doc = ET.ElementTree(self.xml_robot)

        link_names = [n.name for n in links] 

        i = 0
        for link in links:
            self._add_link(link.name, link.visual_filename, link.visual_material_name, link.visual_rgba, link.collision_filename)
            if i < len(joints):
                if joints[i].parent_link_name not in link_names or joints[i].child_link_name not in link_names:
                    raise ValueError("The link name included in the joint, does not exist!")
                self._add_joint(joints[i].name, 
                                joints[i].type, 
                                joints[i].parent_link_name, 
                                joints[i].child_link_name,
                                joints[i].d, 
                                joints[i].theta, 
                                joints[i].alpha, 
                                joints[i].a)
                i += 1
        
        self.urdf_doc.write(output_file, xml_declaration=True, encoding='utf-16', pretty_print=True) 


    def _add_link(self, link_name, visual_filename, visual_material_name, visual_rgba, collision_filename):
        link_elem = ET.SubElement(self.xml_robot, 'link', 
                                            name=link_name)

        link_sub_elems_visual = ET.SubElement(link_elem, "visual")
        link_sub_elems_visual_geometry = ET.SubElement(link_sub_elems_visual, "geometry")
        # link_sub_elems_visual_geometry_origin = ET.SubElement(link_sub_elems_visual_geometry, "origin", xyz="0 0 0", rpy="0 0 0")
        # link_sub_elems_visual_geometry_cylinder = ET.SubElement(link_sub_elems_visual_geometry, "cylinder", length="1.0", radius="0.0")
        # link_sub_elems_visual_material = ET.SubElement(link_sub_elems_visual, "material", name="blue")
        # link_sub_elems_visual_material_color = ET.SubElement(link_sub_elems_visual_material, "color", rgba="0 0 .8 1")

        # USING 3D mesh files
        link_sub_elems_visual_geometry_mesh = ET.SubElement(link_sub_elems_visual_geometry, "mesh", filename=visual_filename)
        link_sub_elems_visual_material = ET.SubElement(link_sub_elems_visual, "material", name=visual_material_name)
        link_sub_elems_visual_material_color = ET.SubElement(link_sub_elems_visual_material, "color", rgba=visual_rgba)
        # link_sub_elems_collision = ET.SubElement(link_elem, "collision")
        # link_sub_elems_collision_geometry = ET.SubElement(link_sub_elems_collision, "geometry")
        # link_sub_elems_collision_geometry_mesh = ET.SubElement(link_sub_elems_collision_geometry, "mesh", filename=collision_filename)
        # link_sub_elems_inertial = ET.SubElement(link_elem, "inertial")
        # link_sub_elems_inertial_mass = ET.SubElement(link_sub_elems_inertial, "mass", value="4.0")
        # link_sub_elems_inertial_origin = ET.SubElement(link_sub_elems_inertial, "origin", rpy="0 0 0", xyz="0.0 0.0 0.0")
        # link_sub_elems_inertial_inertia = ET.SubElement(link_sub_elems_inertial, "inertia", ixx="0.0", ixy="0.0", ixz="0.0", iyy="0.0",iyz="0.0",izz="0.0")


    def _add_joint(self, joint_name, joint_type, parent_link_name, child_link_name, d, theta, alpha, a):
        joint_elem = ET.SubElement(self.xml_robot,
                                    "joint", 
                                    name=joint_name,
                                    type=joint_type)
        joint_sub_elems_parent = ET.SubElement(joint_elem,
                                    "parent",
                                    link=parent_link_name)
        joint_sub_elems_child = ET.SubElement(joint_elem,
                                    "child",
                                    link=child_link_name)
        # From the book Introduction to Robotics by John Craig, on page 75, equation 3.6, the last column consists of:
        # [x, y, z] positions corresponding to: [a_{i-1}, -sin(alpha_{i-1}) * d_i, cos(alpha_{i-1} * d_i)]
        dy = -sin(alpha) * d
        dz = cos(alpha) * d 
        joint_sub_elems_origin = ET.SubElement(joint_elem,
                                        "origin",
                                        rpy=f"{alpha} 0.0 {theta}",
                                        xyz=f"{a} {dy} {dz}")

        joint_sub_elems_axis = ET.SubElement(joint_elem,
                                    "axis",
                                    xyz="0 0 1")
        joint_sub_elems_limit = ET.SubElement(joint_elem,
                                    "limit",
                                    effort="150.0",
                                    lower="-1.0",
                                    upper="1.0",
                                    velocity="3.15")

        # joint_sub_elems_dynamics = ET.SubElement(joint_elem,
        #                             "dynamics",
        #                             damping="0.0",
        #                             friction="0.0")

 

if __name__ == '__main__':
    filename = 'dh_to_urdf/my_urdf.urdf'
    component_name = "my_ur_robot"
    links = [Link("base_link", "cube.dae", "LightGrey", "0.7 0.7 0.7 1.0", "collision_filename"),
            Link("shoulder_link", "cube1.dae", "Piglet", "0.2 0.0 0.7 1.0", "collision_filename"),
            Link("upper_arm_link", "cube.dae", "LightGrey", "0.7 0.7 0.7 1.0", "collision_filename"),
            Link("forearm_link", "cube1.dae", "Piglet", "0.2 0.0 0.7 1.0", "collision_filename"),
            Link("wrist1_link", "cube.dae", "LightGrey", "0.7 0.7 0.7 1.0", "collision_filename"),
            Link("wrist2_link", "cube1.dae", "Piglet", "0.2 0.0 0.7 1.0", "collision_filename"),
            Link("wrist3_link", "cube.dae", "LightGrey", "0.7 0.7 0.7 1.0", "collision_filename")]
    joints = [Joint("joint1", "revolute", links[0].name, links[1].name, 15.19, 0, 0, 0),
                Joint("joint2", "revolute", links[1].name, links[2].name, 0, 0, pi/2, 0),
                Joint("joint3", "revolute", links[2].name, links[3].name, 0, 0, 0, -24.35),
                Joint("joint4", "revolute", links[3].name, links[4].name, 13.10, 0, 0, -21.32),
                Joint("joint5", "revolute", links[4].name, links[5].name, 8.53, 0, pi/2, 0),
                Joint("joint6", "revolute", links[5].name, links[6].name, 9.21, 0, -pi/2, 0)]
    MDH_to_URDF(component_name, links, joints, filename)


    # filename = "urdf/ur5e_test/ur5.urdf"
    #filename = "dh_to_urdf/generated_example.urdf"
    robot = URDF.load(filename)

    robot.show(use_collision=False)
