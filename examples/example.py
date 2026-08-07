import numpy as np
import sys
import os

# Consente l'importazione dalla cartella src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.robot_model import Robot3DOF

def run_examples():
    robot = Robot3DOF()

    print("\n=== ESEMPIO 1: Robot esteso in avanti (q = [0, 0, 0]) ===")
    res_1 = robot.forward_kinematics([0.0, 0.0, 0.0], verbose=True)
    print(f"Position (x,y,z): {np.round(res_1['position'], 4)}")
    print(f"Orientation (roll, pitch, yaw): {np.round(res_1['orientation_rpy'], 4)}")

    print("\n=== ESEMPIO 2: Rotazione base di 90° (q = [pi/2, 0, 0]) ===")
    res_2 = robot.forward_kinematics([np.pi/2, 0.0, 0.0], verbose=False)
    print(f"Position (x,y,z): {np.round(res_2['position'], 4)}")

if __name__ == "__main__":
    run_examples()
