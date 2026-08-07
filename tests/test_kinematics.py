import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.robot_model import Robot3DOF

def test_home_position():
    robot = Robot3DOF(d1=0.30, a2=0.25, a3=0.15)
    res = robot.forward_kinematics([0, 0, 0])
    
    # Braccio esteso lungo X (a2+a3 = 0.40) e traslato su Z (d1 = 0.30)
    expected_pos = np.array([0.40, 0.0, 0.30])
    np.testing.assert_array_almost_equal(res["position"], expected_pos)

def test_base_rotation():
    robot = Robot3DOF(d1=0.30, a2=0.25, a3=0.15)
    res = robot.forward_kinematics([np.pi/2, 0, 0])
    
    # Ruotando la base di 90°, il braccio si sposta lungo l'asse Y
    expected_pos = np.array([0.0, 0.40, 0.30])
    np.testing.assert_array_almost_equal(res["position"], expected_pos)
