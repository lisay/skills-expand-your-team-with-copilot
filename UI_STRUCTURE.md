# Minesweeper Game UI Structure

## Game Window Layout

```
+-----------------------------------------------------------------------+
|  扫雷游戏 - Minesweeper                                                |
+-----------------------------------------------------------------------+
| 难度: [简单▼] |          💣: 10          |  ⏱️: 000  | [新游戏]      |
+-----------------------------------------------------------------------+
|                                                                       |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   | 1 | 2 | 1 |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   | 1 |💣| 1 |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   | 1 | 1 | 1 |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   | 🚩|   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|   |   |   |   |   |   |   |   |   |   |                              |
|   +---+---+---+---+---+---+---+---+---+                              |
|                                                                       |
+-----------------------------------------------------------------------+
|     左键点击: 揭开格子 | 右键点击: 标记旗帜                           |
|     Left-click: Reveal | Right-click: Flag                           |
+-----------------------------------------------------------------------+
```

## Features Implemented

### Game Board
- Dynamic grid size based on difficulty level
- Each cell is a 40x40 pixel button
- Color-coded numbers (1-8) showing adjacent mine counts
- Empty cells reveal automatically in chain reaction
- Mines displayed with 💣 emoji
- Flags displayed with 🚩 emoji

### Top Control Panel
- **Difficulty Selector**: Choose between three levels
  - 简单 (Beginner): 9x9 grid, 10 mines
  - 中等 (Intermediate): 16x16 grid, 40 mines  
  - 困难 (Expert): 16x30 grid, 99 mines

- **Mine Counter** (💣): Shows remaining unflagged mines
  - Updates when flags are placed/removed
  - Helps track progress

- **Timer** (⏱️): Shows elapsed time
  - Starts on first click
  - Stops when game ends (win or lose)
  - Displays time in seconds (000-999)

- **New Game Button**: Restart the game
  - Clears the board
  - Resets all counters
  - Applies current difficulty setting

### Game Mechanics
- **First Click Safety**: First clicked cell is never a mine
- **Auto-Reveal**: Clicking empty cells reveals all adjacent empty areas
- **Flag System**: Right-click to mark suspected mines
- **Number Colors**: Each number (1-8) has distinct color for visibility
- **Win Detection**: Game ends when all non-mine cells are revealed
- **Lose Detection**: Clicking a mine reveals all mines and ends game

### Visual Design
- Clean, modern interface with hover effects
- 3D-style button borders (outset for unrevealed, inset for revealed)
- Red background for revealed mines
- Gray background for unrevealed cells
- Light background for revealed safe cells
- Bilingual labels (Chinese/English)

## Cell States

1. **Unrevealed** (Gray, raised border)
2. **Flagged** (Gray with 🚩, raised border)
3. **Revealed Empty** (White, flat border, blank)
4. **Revealed Number** (White, flat border, colored number 1-8)
5. **Revealed Mine** (Red, flat border, 💣)

## Color Coding for Numbers
- 1: Blue (#0000ff)
- 2: Green (#008000)
- 3: Red (#ff0000)
- 4: Dark Blue (#000080)
- 5: Dark Red (#800000)
- 6: Cyan (#008080)
- 7: Black (#000000)
- 8: Gray (#808080)
