# Maze Generation and Pathfinding

This Python script demonstrates:
1. **Generating a maze** of size `N×N` using **Depth-First Search (DFS)**.
2. **Finding a path** from the top-left corner to the bottom-right corner using **Breadth-First Search (BFS)**.
3. **Visualizing** each step of both maze creation and pathfinding with **Pygame**.

---

## 📌 Features

- **DFS Maze Generation**  
  - Creates a *spanning tree* (no cycles) ensuring a single unique path between any two cells.  
  - Randomized choices produce unique mazes on each run.

- **BFS Pathfinding**  
  - Implements a step-by-step search from the start to the goal.  
  - Highlights visited cells and reconstructs the shortest path.

- **Visualization**  
  - Uses **Pygame** to draw the maze and highlight search progress.  
  - Adjustable **delay** allows controlling animation speed.

---

## ⚙️ Requirements

- **Python 3.x**  
- **Pygame library** (install via `pip install pygame`)

---

## 🚀 How to Run

1. Clone or download this repository.
2. Execute the script:
```sh
python labyrinth.py
```

---

## 🔑 Key Functions

### **1️⃣ `generate_maze_dfs(r, c)`**
   - 🏗️ Creates a maze by carving passages using **Depth-First Search (DFS)**.
   - 📌 Uses a **stack** to track the current path.
   - 🔗 Removes walls between the current cell and a **random unvisited neighbor**.

### **2️⃣ `find_path_bfs(start_r, start_c, end_r, end_c)`**
   - 🔍 Searches for the **shortest path** using **Breadth-First Search (BFS)**.
   - 🗂️ Keeps track of visited cells and a **parent dictionary** to reconstruct the path.
   - 🟥 Highlights **visited cells** step by step.

### **3️⃣ `draw_grid()`**
   - 🎨 Redraws the **entire grid**, including walls.

### **4️⃣ `highlight_cell(r, c, color)`**
   - ✨ Visually **highlights** a single cell on the screen.

---

## 🛠️ Main Execution Flow

1. **Initialize the grid** of `Cell` objects.
2. **Generate the maze** using `generate_maze_dfs(0, 0)`.
3. **Reset the visited flag** for each cell.
4. **Run BFS** to find the shortest path from `(0,0)` to `(N-1,N-1)`.
5. **Highlight the path** if found.
6. **Keep the window open** until the user closes it.

---

## 🎛️ Customization

- ✏️ **Modify `N`** → Change maze size.
- 🖌️ **Adjust `CELL_SIZE`** → Change cell rendering size.
- 🏎️ **Modify `SEARCH_DELAY`** → Speed up or slow down BFS visualization.

---

## 📜 License

This code is provided **as-is** for educational and demonstration purposes.  
Feel free to use or modify it in your own projects. 🎯
