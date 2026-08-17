import numpy as np
from src.transformations import rot_x, rot_y, rot_z, translation, extract_rpy

class Robot3DOF:
    def __init__(self, d1=0.30, a2=0.25, a3=0.15):
        self.d1 = d1
        self.a2 = a2
        self.a3 = a3

    def forward_kinematics(self, q, verbose=True):
        """
        Calcola la trasformazione dalla base all'end-effector per q = [q1, q2, q3].
        utilizzando la convenzione di Denavit-Hartenberg.
        """
        q1, q2, q3 = q

        # Joint 1: Rotazione attorno a Z0 (q1), traslazione lungo Z0 (d1),
        # e twist di 90 gradi (-pi/2) attorno a X per puntare l'asse Z1 correttamente.
        T_01 = rot_z(q1) @ translation(0, 0, self.d1) @ rot_x(-np.pi / 2)

        # Joint 2: Rotazione attorno a Z1 (q2), traslazione lungo X1 (a2).
        T_12 = rot_z(q2) @ translation(self.a2, 0, 0)

        # Joint 3: Rotazione attorno a Z2 (q3), traslazione lungo X2 (a3).
        T_23 = rot_z(q3) @ translation(self.a3, 0, 0)

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
