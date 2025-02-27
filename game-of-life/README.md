# Game of Life (Toroidal Field)

This project is an implementation of **Conway's Game of Life** using **Pygame**. The simulation runs on a **toroidal field**, meaning that the edges of the grid wrap around (the left side connects to the right, and the top connects to the bottom). This ensures that patterns can move continuously without disappearing at the borders.

## How the Game Works
Each cell on the grid has **8 neighbors** (including diagonal ones). The state of each cell in the next generation follows these simple rules:
- **Survival:** A live cell with **2 or 3 neighbors** remains alive.
- **Death:** A live cell with **fewer than 2** or **more than 3 neighbors** dies.
- **Birth:** A dead cell with **exactly 3 neighbors** becomes alive.

## Installation & Running the Game
### **Prerequisites**
- Python 3.x
- Pygame
- NumPy

### **Installation**
Run the following command to install dependencies:
```sh
pip install pygame numpy
```

### **Run the Game**
Execute the script:
```sh
python game_of_life.py
```

## Initial Configurations
You can choose different **starting patterns** by modifying the `pattern_name` variable inside `main()`:

```python
pattern_name = "random"  # Change this to any of the configurations below
```

### **Available Configurations**

| Pattern Name | Description |
|-------------|-------------|
| `random` | Randomly initializes the grid with live and dead cells |
| `block` | A **stable 2x2 block** that never changes |
| `blinker` | A **three-cell oscillator** that flips between vertical and horizontal states every step |
| `toad` | A **four-cell oscillator** with a period of 2 steps |
| `beacon` | A **four-cell oscillator** that alternates between two states |
| `glider` | A **small moving structure** that travels diagonally |
| `pulsar` | A **large periodic structure** with a cycle of 3 steps |

### **Examples of Configurations**

#### **Block (Stable Structure)**
```
11 11
11 11
```
This structure remains unchanged forever.

#### **Blinker (Oscillator, Period 2)**
Generation 1:
```
000
111
000
```
Generation 2:
```
010
010
010
```
This pattern oscillates every step.

#### **Glider (Moving Pattern)**
Step 1:
```
010
001
111
```
Step 2:
```
100
010
011
```
Step 3:
```
010
001
111
```
This structure moves diagonally across the grid.

## Additional Features
- **Toroidal Wrapping**: The grid behaves as if the edges are connected, allowing patterns to seamlessly reappear from the opposite side.
- **Adjustable Speed**: Modify `clock.tick(FPS)` in `main()` to change simulation speed.
- **Custom Patterns**: Add new patterns in `initial_pattern()` and modify their placement within the grid.

## Future Improvements
- User interface to dynamically select patterns.
- Support for larger grid sizes and zooming.
- Save/load feature for custom configurations.

