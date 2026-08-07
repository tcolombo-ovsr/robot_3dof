# Cinematica Diretta: Robot 3DOF

Implementazione del modello cinematico per un manipolatore seriale 3DOF, calcolata senza l'ausilio di librerie robotiche dedicate.

## 1. Definizione dei Reference Frame
*   **Base (Frame 0):** Asse Z verticale verso l'alto, Asse X frontale, Asse Y laterale.
*   **Joint 1 (Base):** Rotazione attorno all'asse Z0. Il Frame 1 è traslato di `d1 = 0.30 m` lungo Z0.
*   **Joint 2 (Spalla):** Rotazione attorno all'asse Y1. Il Frame 2 è traslato di `a2 = 0.25 m` lungo X1.
*   **Joint 3 (Gomito):** Rotazione attorno all'asse Y2. L'End-Effector è traslato di `a3 = 0.15 m` lungo X2.

## 2. Convenzione per le rotazioni
I valori di output per l'orientamento finale seguono la convenzione degli angoli di Eulero (Roll, Pitch, Yaw) di tipo XYZ intrinseco. 

## 3. Struttura del Modello
*   `transformations.py`: Fornisce matrici di traslazione/rotazione omogenea base e le conversioni per gli angoli.
*   `robot_model.py`: Accetta gli input in radianti `q = [q1, q2, q3]` e restituisce la Posa dell'end-effector (Position e Orientation) basandosi sulla composizione delle matrici (T_03 = T_01 @ T_12 @ T_23).

## 4. Gestione Ambiente Conda
```bash
conda env create -f environment.yml
conda activate robot_3dof_env
