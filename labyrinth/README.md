# Maze Generation and Pathfinding

This Python script demonstrates:
1. **Generating a maze** of size `N×N` using **Depth-First Search (DFS)**.
2. **Finding a path** from the top-left corner to the bottom-right corner using **Breadth-First Search (BFS)**.
3. **Visualizing** each step of both maze creation and pathfinding with Pygame.

## Features

- **DFS Maze Generation**  
  Creates a *spanning tree* (no cycles) ensuring a single unique path between any two cells.  
  Randomized choices produce unique mazes on each run.

- **BFS Pathfinding**  
  Shows a step-by-step search from the start to the goal.  
  Highlights visited cells and reconstructs the path once the goal is reached.

- **Visualization**  
  Uses Pygame to draw cells, walls, and highlight the progress.  
  Adjustable delay to slow down or speed up the search process.

## Requirements

- Python 3.x  
- Pygame library (`pip install pygame`)

## How to Run

1. Clone or download this repository.
2. Install Pygame (if you haven't already):
```bash
   pip install pygame
```

## Run the script:
```bash
    python maze.py
```
A window will appear, showing the maze being generated. Once generation finishes, BFS will begin and you will see the pathfinding process step by step. Finally, the discovered path is highlighted.

## Code Overview

- N: the number of cells in one dimension of the maze. (Maze is N×N.)
- CELL_SIZE: cell size in pixels.
- SEARCH_DELAY: delay in milliseconds to control BFS animation speed.

## Key Functions

- **generate_maze_dfs(r, c)**
        Creates a maze by carving passages using a DFS approach.
        Uses a stack to keep track of the current path.
        Removes walls between the current cell and a random unvisited neighbor until all cells are connected.

- **find_path_bfs(start_r, start_c, end_r, end_c)**
        Searches for the path using BFS. 
        Keeps track of visited cells and a parent dictionary to reconstruct the path after reaching the goal.
        Highlights visited cells as the search progresses.

- **draw_grid()**
        Redraws the entire grid (all cells), including the walls.

- **highlight_cell(r, c, color)**
        Visually highlights a single cell on the screen with a chosen color.

## Main Execution Flow

- Initialize the grid of Cell objects.
- Generate the maze via generate_maze_dfs(0, 0).
- Reset the visited flag for each cell.
- Run BFS to find a path from (0, 0) to (N-1, N-1).
- Highlight the path (if found).
- Keep the window open until the user closes it.

## Customization

- Change N to generate larger or smaller mazes.
- Modify CELL_SIZE to adjust cell rendering size in the window.
-  Tweak SEARCH_DELAY to speed up or slow down the BFS visualization.