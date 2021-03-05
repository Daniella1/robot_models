import roboticstoolbox as rtb


if __name__ == '__main__':

    robot = rtb.models.DH.UR3()
    print(robot)
    robot.plot(robot.q)

    ur = rtb.models.UR3()
    ur.plot(q=ur.qr)
