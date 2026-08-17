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
    Estrae gli angoli Roll, Pitch e Yaw dalla matrice omogenea T.
    """
    sy = np.sqrt(T[2, 1] ** 2 + T[2, 2] ** 2)

    singular = sy < 1e-6 #numero molto piccolo

    if not singular:
        # Soluzione normale per theta in (-pi/2, pi/2)
        roll_phi = np.arctan2(T[1, 0], T[0, 0])
        pitch_theta = np.arctan2(-T[2, 0], sy)
        yaw_psi = np.arctan2(T[2, 1], T[2, 2])
    else:
        # Singolarità: c_theta = 0.
        # Fissiamo arbitrariamente yaw (psi) a 0.
        yaw_psi = 0.0
        pitch_theta = np.arctan2(-T[2, 0], sy)  # Sarà +pi/2 o -pi/2

        # Con psi=0 e theta=pi/2, calcoliamo phi da -r12 e r22
        roll_phi = np.arctan2(-T[0, 1], T[1, 1])

    return np.array([roll_phi, pitch_theta, yaw_psi])