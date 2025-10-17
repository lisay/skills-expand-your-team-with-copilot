# Minesweeper Game - Visual Guide

## 🎮 Game Screenshots & Examples

### Main Game Window - Beginner Mode (9x9)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  扫雷游戏 - Minesweeper                                 [_][□][X] ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                                                  │
│  难度: [简单 (Beginner) ▼]     💣: 7     ⏱️: 045  [新游戏]      │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐                   │
│         │   │   │   │   │   │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │ 1 │ 1 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │ 1 │   │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │ 2 │ 2 │ 2 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │ 1 │🚩│ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │ 1 │ 1 │ 1 │   │   │ 1 │ 1 │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │   │   │ 1 │🚩│                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │   │   │ 1 │ 1 │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │🚩│   │   │   │   │   │   │   │   │                   │
│         └───┴───┴───┴───┴───┴───┴───┴───┴───┘                   │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│         左键点击: 揭开格子 | 右键点击: 标记旗帜                   │
│         Left-click: Reveal | Right-click: Flag                  │
└──────────────────────────────────────────────────────────────────┘
```

### Game Over - Hit a Mine! 💥

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  扫雷游戏 - Minesweeper                                 [_][□][X] ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                                                  │
│  难度: [简单 (Beginner) ▼]     💣: 7     ⏱️: 028  [新游戏]      │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐                   │
│         │💣│ 2 │ 1 │ 1 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │ 1 │ 2 │💣│ 1 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 2 │ 2 │ 2 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 1 │💣│ 2 │💣│ 1 │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 1 │ 1 │ 2 │ 1 │ 1 │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │ 1 │ 1 │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │💣│ 2 │ 1 │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │ 1 │💣│💣│  ← Hit this!       │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │💣│ 1 │   │   │   │   │   │ 2 │ 2 │                   │
│         └───┴───┴───┴───┴───┴───┴───┴───┴───┘                   │
│                                                                  │
│  ┌────────────────────────────────────────┐                     │
│  │  游戏结束 (Game Over)                  │                     │
│  │                                        │                     │
│  │  你踩到地雷了！                        │                     │
│  │  You hit a mine!                       │                     │
│  │                                        │                     │
│  │              [ 确定 (OK) ]             │                     │
│  └────────────────────────────────────────┘                     │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│         左键点击: 揭开格子 | 右键点击: 标记旗帜                   │
│         Left-click: Reveal | Right-click: Flag                  │
└──────────────────────────────────────────────────────────────────┘
```

### Victory! 🎉

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  扫雷游戏 - Minesweeper                                 [_][□][X] ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                                                  │
│  难度: [简单 (Beginner) ▼]     💣: 0     ⏱️: 112  [新游戏]      │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐                   │
│         │🚩│ 2 │ 1 │ 1 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │ 1 │ 2 │🚩│ 1 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 2 │ 2 │ 2 │ 1 │   │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 1 │🚩│ 2 │🚩│ 1 │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │ 1 │ 1 │ 2 │ 1 │ 1 │   │   │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │ 1 │ 1 │   │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │🚩│ 2 │ 1 │                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │   │   │   │   │   │ 1 │ 1 │🚩│🚩│                   │
│         ├───┼───┼───┼───┼───┼───┼───┼───┼───┤                   │
│         │🚩│ 1 │   │   │   │   │   │ 2 │ 2 │                   │
│         └───┴───┴───┴───┴───┴───┴───┴───┴───┘                   │
│                                                                  │
│  ┌────────────────────────────────────────┐                     │
│  │  恭喜 (Congratulations)                │                     │
│  │                                        │                     │
│  │  你赢了！用时 112 秒                   │                     │
│  │  You won in 112 seconds!               │                     │
│  │                                        │                     │
│  │              [ 确定 (OK) ]             │                     │
│  └────────────────────────────────────────┘                     │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│         左键点击: 揭开格子 | 右键点击: 标记旗帜                   │
│         Left-click: Reveal | Right-click: Flag                  │
└──────────────────────────────────────────────────────────────────┘
```

## 🎯 Key Features Demonstrated

### 1. **Three Difficulty Levels**
   - 简单 (Beginner): 9x9 grid, 10 mines - Perfect for learning
   - 中等 (Intermediate): 16x16 grid, 40 mines - Moderate challenge
   - 困难 (Expert): 16x30 grid, 99 mines - Expert level

### 2. **Visual Indicators**
   - **Numbers (1-8)**: Each color-coded to show adjacent mine count
     - Blue (1), Green (2), Red (3), Navy (4), Maroon (5), Teal (6), Black (7), Gray (8)
   - **Mines (💣)**: Shown when revealed or game ends
   - **Flags (🚩)**: Player-placed markers for suspected mines
   - **Empty cells**: Blank white squares (no adjacent mines)

### 3. **Game Stats**
   - **Mine Counter (💣)**: Shows mines remaining (total - flagged)
   - **Timer (⏱️)**: Counts seconds since first click
   - Both update in real-time during gameplay

### 4. **User Controls**
   - **Left Click**: Reveal a cell
   - **Right Click**: Place/remove flag
   - **Difficulty Dropdown**: Switch between difficulty levels
   - **New Game Button**: Start fresh game with current difficulty

### 5. **Game Flow**
   1. Start with all cells covered
   2. First click is always safe (no mine)
   3. Numbers reveal adjacent mine counts
   4. Empty cells cascade reveal neighbors
   5. Flag suspected mines
   6. Win by revealing all non-mine cells
   7. Lose by clicking a mine

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python3 minesweeper.py

# Or use the launcher script
./run_game.sh
```

## 🧪 Testing

```bash
# Run test suite
QT_QPA_PLATFORM=offscreen python3 test_minesweeper.py
```

## 📝 Technical Details

- **Framework**: PyQt5 5.15.0+
- **Language**: Python 3.7+
- **Cell Size**: 40x40 pixels
- **Grid Layout**: QGridLayout with zero spacing
- **Event Handling**: Mouse clicks (left/right) for interaction
- **Timer**: QTimer updating every 1000ms
- **Random Mine Placement**: Using Python's random.sample()
