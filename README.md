# skills-expand-your-team-with-copilot
Exercise: Expand your team with GitHub Copilot coding agent

## 扫雷游戏 (Minesweeper Game)

A classic Minesweeper game implemented with PyQt5.

### Features

- 🎮 Three difficulty levels: Beginner (9x9), Intermediate (16x16), Expert (16x30)
- 💣 Classic Minesweeper gameplay
- 🚩 Flag mines with right-click
- ⏱️ Timer to track your solving speed
- 🎯 Mine counter showing remaining mines
- 🌏 Bilingual interface (Chinese/English)

### Installation

1. Make sure you have Python 3.7+ installed

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### How to Play

Run the game:
```bash
python minesweeper.py
```

**Game Controls:**
- **Left Click**: Reveal a cell
- **Right Click**: Place/remove a flag
- **New Game Button**: Start a new game
- **Difficulty Dropdown**: Change difficulty level

**Objective:**
Reveal all cells that don't contain mines. Use the numbers to deduce where mines are located. The number in each cell indicates how many mines are adjacent to it.

**Win Condition:**
Reveal all non-mine cells.

**Lose Condition:**
Click on a cell containing a mine.

### Game Rules

1. The board is divided into cells, with mines randomly distributed
2. Click a cell to reveal it
3. If you reveal a mine, you lose the game
4. If you reveal a cell without a mine, a number appears showing how many adjacent cells contain mines
5. Use this information to deduce which cells are safe to click
6. Right-click to flag cells you believe contain mines
7. Win by revealing all cells that don't contain mines

### Screenshots

The game features:
- A clean, intuitive interface
- Color-coded numbers for better visibility
- Mine and flag emojis (💣 🚩)
- Real-time timer and mine counter

Enjoy playing! 祝你玩得愉快！
