"""
Literature used in the framework:
    - Description of URDF files: http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file 
    - The book Introduction to Robotics: Mechanics and Control by John Craig
"""
from lxml import etree as ET
from typing import List
from math import pi, sin, cos
from dataclasses import dataclass

from urdfpy import URDF # For visualiztion of urdf file


"""
@params: 
        alpha: float = 0.0,
        a: float = 0.0, 
        d: float = 0.0, 
        theta: float = 0.0, 
        joint_type: str = "revolute"   - can be one of the elements in the set: {"revolute","prismatic"}
"""
@dataclass
class mdh:
    alpha: float = 0.0
    a: float = 0.0
    d: float = 0.0
    theta: float = 0.0
    joint_type: str = "revolute"
        
    def aslist(self):
        return [self.alpha, self.a, self.d, self.theta, self.joint_type]


class MDH_to_URDF:

    def __init__(self, output_file: str, 
                    component_name:str, 
                    mdh_params: List[mdh], 
                    visual_mesh: List[str]=None, 
                    collision_mesh: List[str]=None):
        
        self._create_file(component_name)

        default_visual_mesh = "rect.dae"
        default_collision_mesh = "rect.stl"
        for i in range(len(mdh_params)):
            self._add_link(f"link{i}", 
                            visual_filename=visual_mesh[i] if visual_mesh != None else default_visual_mesh,
                            collision_filename=collision_mesh[i] if collision_mesh != None else default_collision_mesh)
            _mdh = mdh_params[i]
            self._add_joint(F"joint{i}", _mdh.joint_type,f"link{i}", f"link{i+1}", _mdh.d, _mdh.theta, _mdh.alpha, _mdh.a)

        i += 1
        self._add_link(f"link{i}", visual_filename=visual_mesh[i] if visual_mesh != None else default_visual_mesh)

        self.urdf_doc.write(output_file, xml_declaration=True, encoding='utf-16', pretty_print=True) 


    def _create_file(self, component_name):
        self.robot_name = component_name
        self.xml_robot = ET.Element("robot", name=component_name)
        self.urdf_doc = ET.ElementTree(self.xml_robot)

    def _add_link(self, 
                link_name, 
                visual_filename="cube1.dae", 
                visual_material_name="Mat", 
                visual_rgba="0.5 0.5 0.5 1", 
                collision_filename=None,
                calc_inertia=False):
        link_elem = ET.SubElement(self.xml_robot, 'link', name=link_name)

        link_sub_elems_visual = ET.SubElement(link_elem, "visual")
        link_sub_elems_visual_origin = ET.SubElement(link_sub_elems_visual, "origin", xyz="0.0 0.0 0.0", rpy="0.0 0.0 0.0")
        link_sub_elems_visual_geometry = ET.SubElement(link_sub_elems_visual, "geometry")

        # Using 3D mesh files
        link_sub_elems_visual_geometry_mesh = ET.SubElement(link_sub_elems_visual_geometry, "mesh", filename=visual_filename)
        link_sub_elems_visual_material = ET.SubElement(link_sub_elems_visual, "material", name=visual_material_name)
        link_sub_elems_visual_material_color = ET.SubElement(link_sub_elems_visual_material, "color", rgba=visual_rgba)

        if collision_filename != None:
            link_sub_elems_collision = ET.SubElement(link_elem, "collision")
            link_sub_elems_collision_origin = ET.SubElement(link_sub_elems_collision, "origin", xyz="0.0 0.0 0.0", rpy="0.0 0.0 0.0")
            link_sub_elems_collision_geometry = ET.SubElement(link_sub_elems_collision, "geometry")
            link_sub_elems_collision_geometry_mesh = ET.SubElement(link_sub_elems_collision_geometry, "mesh", filename=collision_filename)

        if calc_inertia:
            link_sub_elems_inertial = ET.SubElement(link_elem, "inertial")
            link_sub_elems_inertial_mass = ET.SubElement(link_sub_elems_inertial, "mass", value="4.0")
            link_sub_elems_inertial_origin = ET.SubElement(link_sub_elems_inertial, "origin", rpy="0 0 0", xyz="0.0 0.0 0.0")
            link_sub_elems_inertial_inertia = ET.SubElement(link_sub_elems_inertial, "inertia", ixx="0.0", ixy="0.0", ixz="0.0", iyy="0.0",iyz="0.0",izz="0.0")


    def _add_joint(self, joint_name, joint_type, parent_link_name, child_link_name, d, theta, alpha, a, calc_dynamics=False):
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
        """ 
        From the book Introduction to Robotics by John Craig, on page 75, equation 3.6, the last column consists of:
        [x, y, z] positions corresponding to: [a_{i-1}, -sin(alpha_{i-1}) * d_i, cos(alpha_{i-1} * d_i)] 
        """
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
        if calc_dynamics:
            joint_sub_elems_dynamics = ET.SubElement(joint_elem,
                                    "dynamics",
                                    damping="0.0",
                                    friction="0.0")
