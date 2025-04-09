# Medical Diagnostic Expert System - Decision Tree

This project implements a simple expert system using a decision tree approach for basic medical diagnostics. The system is built with Python and utilizes the **pygame** library to provide a graphical user interface that allows users to interactively answer questions and receive diagnostic recommendations.

## Overview

The expert system uses a transition table (implemented as a Python dictionary) to represent the decision tree. Each node in the tree contains either:
- A **question** along with "yes" and "no" options, or
- A **result** containing a diagnosis or recommendation.

Users navigate through the tree by answering questions via clickable buttons. The final node displays a diagnostic conclusion along with advice, all rendered through a customizable, multi-line text interface.

## Features

- **Interactive GUI:** Uses pygame to create a window with questions and buttons ("Yes" / "No").
- **Decision Tree Logic:** Implements the diagnostic flow using a transition table.
- **Multi-line Text Support:** Displays messages with newline characters (`\n`) to format the text over multiple lines.
- **User-Friendly Controls:** Supports exiting the application via the ESC key or closing the window.
  
## Requirements

- Python 3.x
- [pygame](https://www.pygame.org/) (Install via `pip install pygame`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ArtemZiablov/Introduction-to-AI.git
   cd expert-diagnosis
   ```
2. **Install Pygame:**
   ```bash
   pip install pygame
    ```
   
3. **Run the game:**
   ```bash
   python expert.py
    ```

## Code Structure

- **main.py**
  - Contains the complete implementation of the expert system.
    - Initializes pygame and sets up the display.
    - Implements a function (`draw_multiline_text`) to draw multi-line text on the screen.
    - Uses a transition table (`transition_table`) to guide the decision-making process.
    - Contains the main loop which manages event handling and graphical updates.

## How It Works

- **Initialization:**
  - The application initializes pygame, sets up the display window, defines colors, fonts, and button dimensions.

- **Displaying Content:**
  - The system checks the current node from the transition table:
    - If the node contains a `"question"`, it renders the question and displays "Yes" and "No" buttons.
    - If the node contains a `"result"`, it displays the diagnostic conclusion with instructions to exit.

- **User Interaction:**
  - The user selects an option by clicking one of the buttons. Based on the user's response, the system transitions to the next node in the tree.

- **Exiting the Application:**
  - When a final result is reached, the user can exit by pressing the ESC key or closing the window.

## Future Enhancements

- **Extended Diagnostic Questions:** Increase the depth of the decision tree to handle more complex diagnostics.
- **Visual Enhancements:** Improve the visual design and add animations to enhance user experience.
- **Data Persistence:** Save user responses or diagnostic logs for further analysis.
