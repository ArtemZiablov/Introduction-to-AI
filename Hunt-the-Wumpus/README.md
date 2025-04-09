# Hunt the Wumpus

A Python implementation of the classic "Hunt the Wumpus" game using Pygame. In this game, you explore interconnected rooms in a cave where dangers lurk around every corner. Watch out for pits, bats, and especially the fearsome Wumpus! Use your limited supply of arrows wisely to defeat the Wumpus.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Code Structure](#code-structure)
- [License](#license)
- [Credits](#credits)

## Overview

In this version of "Hunt the Wumpus", you navigate a cave consisting of interconnected rooms (represented as nodes on a circle). Each room is connected to three neighboring rooms. The game includes:
- **Wumpus**: A dangerous creature that will kill you if you enter its room.
- **Pits**: Falling into one of these rooms results in an instant loss.
- **Bats**: Entering a bat room will randomly transport you to another room.
- **Limited Arrows**: You have a maximum of 5 arrows to shoot at the Wumpus. A warning appears if the Wumpus is in an adjacent room.

## Features

- **Graphical Representation**: Simple and clear visualization using Pygame.
- **Room Connections**: Rooms are organized on a circle with preset neighbors.
- **Interactive Gameplay**: Move and shoot with mouse clicks.
- **Dynamic Messages**: Alerts when the Wumpus is nearby and when hazards are encountered.
- **Arrow Counter Display**: Shown in the bottom-left corner of the screen.

## Requirements

- Python 3.x
- Pygame

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ArtemZiablov/Introduction-to-AI.git
   cd Hunt-the-Wumpus
   ```
2. **Install Pygame:**
   ```bash
   pip install pygame
    ```
   
3. **Run the game:**
   ```bash
   python hunt-the-wumpus.py
    ```

### How to Play

- **Objective:**  
  Navigate through the cave, avoid hazards and defeat the Wumpus by shooting it with your arrows.
  
- **Warnings:**  
  If the Wumpus is in one of the adjacent rooms, you will see a message that "You smell a terrible stench!".

- **Losing Conditions:**  
  Entering a room with the Wumpus, falling into a pit, or running out of arrows without defeating the Wumpus.

### Controls

- **Left Mouse Button (LMB):**  
  Move to an adjacent room.

- **Right Mouse Button (RMB):**  
  Shoot an arrow into an adjacent room.

- **Arrow Counter:**  
  Displayed in the bottom-left corner of the screen. You start with 5 arrows.

### Code Structure

- **Initialization:**  
  Sets up the game window, fonts, colors, and room coordinates.

- **Hazard Initialization:**  
  Randomly selects rooms for the Wumpus, pits, and bats, ensuring the starting room is safe.

- **Game Loop:**  
  Handles events, updates screen, checks for hazards, and displays messages.

- **User Feedback:**  
  Displays real-time messages and warnings based on player actions and neighboring hazards.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Credits

- **Game Concept:**  
  [Hunt the Wumpus on Wikipedia](https://en.wikipedia.org/wiki/Hunt_the_Wumpus)

- **Implemented with:**  
  [Pygame](https://www.pygame.org/)

- Feel free to modify and extend this implementation for your own projects!
