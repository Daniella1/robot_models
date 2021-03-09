import roboticstoolbox as rtb
from math import pi
import numpy as np


class EmilUR(rtb.DHRobot):

    def __init__(self):

        deg = pi/180

        L0 = rtb.RevoluteMDH(d=0.15185, a=0, alpha=0)
        L1 = rtb.RevoluteMDH(d=0, a=0, alpha=pi/2)
        L2 = rtb.RevoluteMDH(d=0, a=-0.24355, alpha=0)
        L3 = rtb.RevoluteMDH(d=0.13105, a=-0.2132, alpha=0)
        L4 = rtb.RevoluteMDH(d=0.08535, a=0, alpha=pi/2)
        L5 = rtb.RevoluteMDH(d=0.0921, a=0, alpha=-pi/2)

        super().__init__(
            [L0, L1, L2, L3, L4, L5],
            name="UR3e",
            manufacturer="Universal Robots")

        # zero angles, L shaped pose
        self._MYCONFIG = np.array([1, 2, 3, 4, 5, 6])  # create instance attribute

    @property
    def MYCONFIG(self):
        return self._MYCONFIG

# class DaniellaOldUR(rtb.DHRobot):

#     def __init__(self):

#         L0 = rtb.RevoluteMDH(d=0, a=0, alpha=0)
#         L1 = rtb.RevoluteMDH(d=0.15185, a=0, alpha=0)
#         L2 = rtb.RevoluteMDH(d=0.24355/2, a=0, alpha=-pi/2)
#         L3 = rtb.RevoluteMDH(d=0, a=0.13105, alpha=0)
#         L4 = rtb.RevoluteMDH(d=-0.24355/2, a=0, alpha=0)
#         L5 = rtb.RevoluteMDH(d=0, a=0.13105, alpha=0)
#         L6 = rtb.RevoluteMDH(d=0.24355/2, a=0, alpha=0)

#         super().__init__(
#             [L0, L1, L2, L3, L4, L5, L6],
#             name="UR3e",
#             manufacturer="Universal Robots")


class DaniellaUR(rtb.DHRobot):

    def __init__(self):

        # Correct, like emils 100%
        L0 = rtb.RevoluteMDH(d=0.1519, a=0, alpha=0)
        L1 = rtb.RevoluteMDH(d=0, a=0, alpha=pi/2)
        L2 = rtb.RevoluteMDH(d=0, a=-0.24355, alpha=0)
        L3 = rtb.RevoluteMDH(d=0.13105, a=-0.2132, alpha=0)
        L4 = rtb.RevoluteMDH(d=0.08535, a=0, alpha=pi/2)
        L5 = rtb.RevoluteMDH(d=0.0921, a=0, alpha=-pi/2)

        # 
        # L0 = rtb.RevoluteMDH(d=0.1519, a=0, alpha=0)
        # L1 = rtb.RevoluteMDH(d=0, a=0, alpha=pi/2)
        # L2 = rtb.RevoluteMDH(d=0, a=-0.24355, alpha=0)
        # L3 = rtb.RevoluteMDH(d=0, a=-0.2132, alpha=0)
        # L4 = rtb.RevoluteMDH(d=0.13105, a=0, alpha=pi/2) 
        # L5 = rtb.RevoluteMDH(d=0.08535, a=0, alpha=-pi/2)
        # L6 = rtb.RevoluteMDH(d=0.0921, a=0, alpha=0)

        super().__init__(
            [L0, L1, L2, L3, L4, L5],
            name="UR3e",
            manufacturer="Universal Robots")


class OnRobotScrewdriver(rtb.DHRobot):

    def __init__(self, l3):
        L0 = rtb.RevoluteMDH(d=0.0514, a=0, alpha=0)
        L1 = rtb.RevoluteMDH(d=0.1141, a=0, alpha=-pi/2)
        L2 = rtb.PrismaticMDH(theta=0, a=0, alpha=0)

        super().__init__(
            [L0, L1, L2],
            name="OnRobot Screwdriver",
            manufacturer="OnRobot")



if __name__ == '__main__':

    emilur = EmilUR()
    print("Emil UR")
    print(emilur)

    daniellaur = DaniellaUR()
    print("Daniella UR")
    print(daniellaur)

    ur = rtb.models.DH.UR3()
    print("UR")
    print(ur)

    l3 = 0.5
    sd = OnRobotScrewdriver(l3)
    print("Screwdriver")
    print(sd)

    

    # emilur.plot(emilur.q)
    daniellaur.plot(daniellaur.q)
    # ur.plot(ur.qr)
    #sd.plot(sd.q)

