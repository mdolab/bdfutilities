# External modules
import numpy as np


def rotationMatrix(vx, vy, vz, theta):
    """
    Rotate the grid around an axis that passes through the origin.

    parameters
    ----------
    vx, vy, vz : float
        components of the rotation vector
    theta : float
        rotation angle, in degrees

    returns
    -------
    rotMat : ndarray
        the rotation matrix
    """

    # Normalize the components of the rotation vector
    normV = np.sqrt(vx**2 + vy**2 + vz**2)
    uu = vx / normV
    vv = vy / normV
    ww = vz / normV

    # Compute sines and cosines of the rotation angle
    ss = np.sin(theta * np.pi / 180.0)
    cc = np.cos(theta * np.pi / 180.0)

    # Build rotation matrix
    rotMat = np.zeros((3, 3))
    rotMat[0, 0] = uu * uu + (1.0 - uu * uu) * cc
    rotMat[0, 1] = uu * vv * (1.0 - cc) - ww * ss
    rotMat[0, 2] = uu * ww * (1.0 - cc) + vv * ss
    rotMat[1, 0] = uu * vv * (1.0 - cc) + ww * ss
    rotMat[1, 1] = vv * vv + (1.0 - vv * vv) * cc
    rotMat[1, 2] = vv * ww * (1.0 - cc) - uu * ss
    rotMat[2, 0] = uu * ww * (1.0 - cc) - vv * ss
    rotMat[2, 1] = vv * ww * (1.0 - cc) + uu * ss
    rotMat[2, 2] = ww * ww + (1.0 - ww * ww) * cc

    return rotMat
