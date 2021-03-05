from lxml import etree as ET
from typing import List


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

    def __init__(self, name, visual_filename, visual_material_name, visual_rgba):
        self.name = name
        self.visual_filename = visual_filename
        self.visual_material_name = visual_material_name
        self.visual_rgba = visual_rgba


class MDH_to_URDF:

    def __init__(self, component_name: str, links: List[Link], joints: List[Joint], output_file: str):
        
        if len(links) < len(joints): # todo: fix to be [len(links) - 1 == len(joints)]
            raise AttributeError("Length of Links is smaller than length of Joints provided.")
        
        self.robot_name = component_name
        self.xml_robot = ET.Element("robot", name=component_name)
        self.urdf_doc = ET.ElementTree(self.xml_robot)

        link_names = [n.name for n in links] 

        i = 0
        for link in links:
            self._add_link(link.name, link.visual_filename, link.visual_material_name, link.visual_rgba)
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


    def _add_link(self, link_name, visual_filename, visual_material_name, visual_rgba):
        link_elem = ET.SubElement(self.xml_robot, 'link', 
                                            name=link_name)

        link_sub_elems_visual = ET.SubElement(link_elem, "visual")
        link_sub_elems_visual_geometry = ET.SubElement(link_sub_elems_visual, "geometry")
        link_sub_elems_visual_geometry_mesh = ET.SubElement(link_sub_elems_visual_geometry, "mesh", filename=visual_filename)
        link_sub_elems_visual_material = ET.SubElement(link_sub_elems_visual, "material", name=visual_material_name)
        link_sub_elems_visual_material_color = ET.SubElement(link_sub_elems_visual_material, "color", rgba=visual_rgba)

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
        joint_sub_elems_origin = ET.SubElement(joint_elem,
                                    "origin",
                                    rpy="0.0 0.0 0.0",
                                    xyz="0.0 0.0 0.0") # TODO: make these values variables

        joint_sub_elems_axis = ET.SubElement(joint_elem,
                                    "axis",
                                    xyz="0 1 0")
        # joint_sub_elems_limit = ET.SubElement(joint_elem,
        #                             "limit",
        #                             effort="150.0",
        #                             lower="-1.0",
        #                             upper="1.0",
        #                             velocity="3.15")

        # joint_sub_elems_dynamics = ET.SubElement(joint_elem,
        #                             "dynamics",
        #                             damping="0.0",
        #                             friction="0.0")

 

if __name__ == '__main__':
    outfile_name = 'dh_to_urdf/my_urdf.urdf'
    component_name = "my_ur_robot"
    links = [Link("base_link", "visual_filename", "material_name", "0.7, 0.7, 0.7, 1.0"),
            Link("shoulder_link", "visual_filename", "material_name", "0.7, 0.7, 0.7, 1.0")]
    joints = [Joint("joint1", "revolute", links[0].name, links[1].name, 0, 0, 0, 0)]
    MDH_to_URDF(component_name, links, joints, outfile_name)
