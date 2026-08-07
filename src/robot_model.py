import numpy as np
from src.transformations import rot_y, rot_z, translation, extract_rpy

class Robot3DOF:
    def __init__(self, d1=0.30, a2=0.25, a3=0.15):
        self.d1 = d1
        self.a2 = a2
        self.a3 = a3

    def forward_kinematics(self, q, verbose=False):
        """
        Calcola la trasformazione dalla base all'end-effector per q = [q1, q2, q3].
        """
        q1, q2, q3 = q

        # Joint 1: rotazione base attorno a Z0
        T_01 = translation(0, 0, self.d1) @ rot_z(q1)

        # Joint 2: rotazione spalla attorno a Y1
        T_12 = rot_y(q2) @ translation(self.a2, 0, 0)

        # Joint 3: rotazione gomito attorno a Y2
        T_23 = rot_y(q3) @ translation(self.a3, 0, 0)

        # Trasformazione complessiva
        T_03 = T_01 @ T_12 @ T_23

        if verbose:
            print("\n--- TRASFORMAZIONI INTERMEDIE ---")
            print("T_01:\n", np.round(T_01, 4))
            print("T_12:\n", np.round(T_12, 4))
            print("T_23:\n", np.round(T_23, 4))
            print("T_03 = T_01 @ T_12 @ T_23:\n", np.round(T_03, 4))
            print("---------------------------------")

        # Estrazione Posizione e Orientamento
        position = T_03[0:3, 3]
        rpy = extract_rpy(T_03)

        return {
            "position": position,
            "orientation_rpy": rpy,
            "T_03": T_03
        }
