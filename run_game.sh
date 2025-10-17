#!/bin/bash
# Launcher script for Minesweeper game

echo "Starting Minesweeper Game..."
echo "扫雷游戏启动中..."
echo ""

# Check if PyQt5 is installed
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo "PyQt5 is not installed. Installing dependencies..."
    echo "PyQt5 未安装。正在安装依赖..."
    pip install -r requirements.txt
fi

# Run the game
python3 minesweeper.py
