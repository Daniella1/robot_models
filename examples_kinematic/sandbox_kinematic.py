from visual_kinematics import Robot
import numpy as np
from math import pi



def dh_params1(n_params):
    a = 0 # in meters
    alpha = 0
    d = 0
    theta = 0
    dh1 = [d,theta,a,alpha]

    a = 0.08 # in meters
    alpha = 0
    d = 0
    theta = 0
    dh2 = [d,theta,a,alpha]

    a = 0.20
    alpha = 0
    theta = pi/2
    d = 0.05
    dh3 = [d,theta,a,alpha]

    a = -0.15
    alpha = 0
    theta = 0
    d = 0.05
    dh4 = [d,theta,a,alpha]

    a = 0.08
    alpha = pi/2
    theta = pi/2
    d = 0
    dh5 = [d,theta,a,alpha]

    a = 0.05
    alpha = 0
    theta = 0
    d = 0
    dh6 = [d,theta,a,alpha]

    dh_params = np.empty([n_params, 4])
    for i in range(1,n_params+1):
        dh_params = np.vstack([dh_params, np.array(eval(f"dh{i}"))])
    return dh_params

def dh_params2(n_params):
    a = 0 # in meters
    alpha = 0
    d = 0
    theta = np.pi
    dh1 = [d,theta,a,alpha]

    a = 0
    alpha = 0
    d = 0
    theta = 0
    dh2 = [d,theta,a,alpha]

    a = 0.08 # in meters
    alpha = 0
    theta = pi/2
    d = 0.05
    dh3 = [d,theta,a,alpha]

    a = 0.20
    alpha = 0
    theta = 0
    d = 0.05
    dh4 = [d,theta,a,alpha]

    a = -0.15
    alpha = 0
    theta = pi/2
    d = 0
    dh5 = [d,theta,a,alpha]

    a = 0.08
    #a = 0.05
    alpha = pi/2
    theta = 0
    d = 0
    dh6 = [d,theta,a,alpha]

    dh_params = np.empty([n_params, 4])
    for i in range(1,n_params+1):
        dh_params = np.vstack([dh_params, np.array(eval(f"dh{i}"))])
    return dh_params


def dh_params3(n_params):
    a = 0 # in meters
    alpha = 0
    d = 0
    theta = 0
    dh1 = [d,theta,a,alpha]

    a = 0.08 # in meters
    alpha = 0
    d = 0
    theta = 0
    dh2 = [d,theta,a,alpha]

    a = 0.20
    alpha = 0
    theta = pi/2
    d = 0.05
    dh3 = [d,theta,a,alpha]

    a = 0.15
    alpha = 0
    theta = 0
    d = 0.05
    dh4 = [d,theta,a,alpha]

    a = 0
    alpha = pi/2
    theta = pi/2
    d = -0.08
    dh5 = [d,theta,a,alpha]

    a = 0
    alpha = 0
    theta = 0
    d = 0.1
    dh6 = [d,theta,a,alpha]

    dh_params = np.empty([n_params, 4])
    for i in range(1,n_params+1):
        dh_params = np.vstack([dh_params, np.array(eval(f"dh{i}"))])
    return dh_params


def dh_params4(n_params):
    a = 0 # in meters
    alpha = 0
    d = 0
    theta = np.pi
    dh0 = [d,theta,a,alpha]

    a = 0
    alpha = 0
    d = 0
    theta = 0
    dh1 = [d,theta,a,alpha]

    a = 0.08 # in meters
    alpha = 0
    theta = pi/2
    d = 0.05
    dh2 = [d,theta,a,alpha]

    a = 0.20
    alpha = 0
    theta = 0
    d = 0.05
    dh3 = [d,theta,a,alpha]

    a = -0.15
    alpha = 0
    theta = pi/2
    d = 0
    dh4 = [d,theta,a,alpha]

    a = 0.08
    #a = 0.05
    alpha = pi/2
    theta = 0
    d = 0
    dh5 = [d,theta,a,alpha]

    a = 0.08
    #a = 0.05
    alpha = pi/2
    theta = 0
    d = 0
    dh6 = [d,theta,a,alpha]

    dh_params = np.empty([n_params, 4])
    for i in range(0,n_params):
        dh_params = np.vstack([dh_params, np.array(eval(f"dh{i}"))])
    return dh_params


def emils_dhparams(n_params):
    a = 0 # in meters
    alpha = 0
    d = 0
    theta = 0
    dh0 = [d,theta,a,alpha]

    a = 0
    alpha = np.pi/2
    d = 0
    theta = 0
    dh1 = [d,theta,a,alpha]

    a = 0.2 # in meters
    alpha = 0
    theta = 0
    d = 0
    dh2 = [d,theta,a,alpha]

    a = 0.20
    alpha = 0
    theta = 0
    d = 0.05
    dh3 = [d,theta,a,alpha]

    a = 0
    alpha = np.pi/2
    theta = 0
    d = 0.05
    dh4 = [d,theta,a,alpha]

    a = 0
    alpha = np.pi/2
    theta = 0
    d = 0.05
    dh5 = [d,theta,a,alpha]

    dh_params = np.empty([n_params, 4])
    for i in range(0,n_params):
        dh_params = np.vstack([dh_params, np.array(eval(f"dh{i}"))])
    return dh_params

if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)

    # d, theta, a, alpha
  

    dh_params = dh_params4(7)
    dh_params = emils_dhparams(6)

    robot = Robot(dh_params, dh_type="modified")

    robot.show()


