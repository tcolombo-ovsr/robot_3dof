import numpy as np

def rot_x(theta):
    """Matrice 4x4 per rotazione attorno all'asse X."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]
    ])

def rot_y(theta):
    """Matrice 4x4 per rotazione attorno all'asse Y."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
    ])

def rot_z(theta):
    """Matrice 4x4 per rotazione attorno all'asse Z."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

def translation(x, y, z):
    """Matrice 4x4 per traslazione."""
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

def extract_rpy(T):
    """
    Estrae gli angoli Roll, Pitch e Yaw (convenzione XYZ) dalla matrice omogenea.
    """
    sy = np.sqrt(T[0,0]**2 + T[1,0]**2)
    singular = sy < 1e-6

    if not singular:
        roll = np.arctan2(T[2,1], T[2,2])
        pitch = np.arctan2(-T[2,0], sy)
        yaw = np.arctan2(T[1,0], T[0,0])
    else:
        roll = np.arctan2(-T[1,2], T[1,1])
        pitch = np.arctan2(-T[2,0], sy)
        yaw = 0

    return np.array([roll, pitch, yaw])
