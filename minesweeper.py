#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyQt5 Minesweeper Game
扫雷游戏

A classic Minesweeper game implementation using PyQt5.
"""

import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                             QMessageBox, QComboBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon


class Cell(QPushButton):
    """Individual cell in the Minesweeper grid"""
    
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0
        
        self.setFixedSize(40, 40)
        self.setFont(QFont('Arial', 12, QFont.Bold))
        self.setStyleSheet("""
            QPushButton {
                background-color: #d0d0d0;
                border: 2px outset #f0f0f0;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
    
    def reveal(self):
        """Reveal the cell content"""
        if self.is_flagged or self.is_revealed:
            return False
        
        self.is_revealed = True
        
        if self.is_mine:
            self.setText('💣')
            self.setStyleSheet("""
                QPushButton {
                    background-color: #ff4444;
                    border: 1px solid #cc0000;
                }
            """)
            return True
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #f8f8f8;
                    border: 1px inset #c0c0c0;
                }
            """)
            if self.adjacent_mines > 0:
                self.setText(str(self.adjacent_mines))
                colors = ['', '#0000ff', '#008000', '#ff0000', '#000080',
                         '#800000', '#008080', '#000000', '#808080']
                self.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #f8f8f8;
                        border: 1px inset #c0c0c0;
                        color: {colors[self.adjacent_mines]};
                    }}
                """)
            return False
    
    def toggle_flag(self):
        """Toggle flag on the cell"""
        if self.is_revealed:
            return
        
        self.is_flagged = not self.is_flagged
        if self.is_flagged:
            self.setText('🚩')
        else:
            self.setText('')


class MinesweeperGame(QMainWindow):
    """Main Minesweeper game window"""
    
    # Difficulty presets: (rows, cols, mines)
    DIFFICULTIES = {
        '简单 (Beginner)': (9, 9, 10),
        '中等 (Intermediate)': (16, 16, 40),
        '困难 (Expert)': (16, 30, 99)
    }
    
    def __init__(self):
        super().__init__()
        self.rows = 9
        self.cols = 9
        self.num_mines = 10
        self.cells = []
        self.game_over = False
        self.game_started = False
        self.flags_placed = 0
        self.cells_revealed = 0
        self.timer_seconds = 0
        
        self.init_ui()
        self.new_game()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('扫雷游戏 - Minesweeper')
        self.setStyleSheet("background-color: #e0e0e0;")
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Top panel with controls
        top_panel = QHBoxLayout()
        
        # Difficulty selector
        difficulty_label = QLabel('难度 (Difficulty):')
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(self.DIFFICULTIES.keys())
        self.difficulty_combo.currentTextChanged.connect(self.change_difficulty)
        
        # New game button
        self.new_game_btn = QPushButton('新游戏 (New Game)')
        self.new_game_btn.clicked.connect(self.new_game)
        self.new_game_btn.setFixedHeight(30)
        
        # Mines counter
        self.mines_label = QLabel(f'💣: {self.num_mines}')
        self.mines_label.setFont(QFont('Arial', 14, QFont.Bold))
        
        # Timer
        self.timer_label = QLabel('⏱️: 000')
        self.timer_label.setFont(QFont('Arial', 14, QFont.Bold))
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        top_panel.addWidget(difficulty_label)
        top_panel.addWidget(self.difficulty_combo)
        top_panel.addStretch()
        top_panel.addWidget(self.mines_label)
        top_panel.addStretch()
        top_panel.addWidget(self.timer_label)
        top_panel.addStretch()
        top_panel.addWidget(self.new_game_btn)
        
        main_layout.addLayout(top_panel)
        
        # Game grid
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(0)
        main_layout.addWidget(self.grid_widget)
        
        # Instructions
        instructions = QLabel('左键点击: 揭开格子 | 右键点击: 标记旗帜\nLeft-click: Reveal | Right-click: Flag')
        instructions.setAlignment(Qt.AlignCenter)
        instructions.setStyleSheet("color: #666; margin-top: 10px;")
        main_layout.addWidget(instructions)
        
        self.show()
    
    def change_difficulty(self, difficulty_name):
        """Change game difficulty"""
        self.rows, self.cols, self.num_mines = self.DIFFICULTIES[difficulty_name]
        self.new_game()
    
    def new_game(self):
        """Start a new game"""
        # Clear existing grid
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)
        
        # Reset game state
        self.cells = []
        self.game_over = False
        self.game_started = False
        self.flags_placed = 0
        self.cells_revealed = 0
        self.timer_seconds = 0
        self.timer.stop()
        self.update_timer_display()
        self.update_mines_display()
        
        # Create grid
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                cell = Cell(row, col)
                cell.clicked.connect(lambda checked, r=row, c=col: self.cell_left_clicked(r, c))
                cell.setContextMenuPolicy(Qt.CustomContextMenu)
                cell.customContextMenuRequested.connect(lambda pos, r=row, c=col: self.cell_right_clicked(r, c))
                self.grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)
        
        # Adjust window size
        self.adjustSize()
    
    def place_mines(self, first_row, first_col):
        """Place mines on the board, avoiding the first clicked cell"""
        mines_placed = 0
        available_positions = [(r, c) for r in range(self.rows) 
                              for c in range(self.cols) 
                              if r != first_row or c != first_col]
        
        mine_positions = random.sample(available_positions, self.num_mines)
        
        for row, col in mine_positions:
            self.cells[row][col].is_mine = True
        
        # Calculate adjacent mines for each cell
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.cells[row][col].is_mine:
                    count = self.count_adjacent_mines(row, col)
                    self.cells[row][col].adjacent_mines = count
    
    def count_adjacent_mines(self, row, col):
        """Count mines adjacent to a cell"""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    if self.cells[r][c].is_mine:
                        count += 1
        return count
    
    def cell_left_clicked(self, row, col):
        """Handle left click on a cell"""
        if self.game_over:
            return
        
        # Start timer on first click
        if not self.game_started:
            self.game_started = True
            self.place_mines(row, col)
            self.timer.start(1000)
        
        cell = self.cells[row][col]
        
        if cell.is_flagged or cell.is_revealed:
            return
        
        # Reveal the cell
        if cell.reveal():
            # Hit a mine - game over
            self.game_over = True
            self.timer.stop()
            self.reveal_all_mines()
            QMessageBox.information(self, '游戏结束 (Game Over)', 
                                   '你踩到地雷了！\nYou hit a mine!')
        else:
            self.cells_revealed += 1
            # If empty cell, reveal adjacent cells
            if cell.adjacent_mines == 0:
                self.reveal_adjacent(row, col)
            
            # Check for win
            if self.cells_revealed == self.rows * self.cols - self.num_mines:
                self.game_over = True
                self.timer.stop()
                QMessageBox.information(self, '恭喜 (Congratulations)', 
                                       f'你赢了！用时 {self.timer_seconds} 秒\n'
                                       f'You won in {self.timer_seconds} seconds!')
    
    def cell_right_clicked(self, row, col):
        """Handle right click on a cell (flag/unflag)"""
        if self.game_over or not self.game_started:
            return
        
        cell = self.cells[row][col]
        if cell.is_revealed:
            return
        
        was_flagged = cell.is_flagged
        cell.toggle_flag()
        
        if cell.is_flagged and not was_flagged:
            self.flags_placed += 1
        elif not cell.is_flagged and was_flagged:
            self.flags_placed -= 1
        
        self.update_mines_display()
    
    def reveal_adjacent(self, row, col):
        """Recursively reveal adjacent cells"""
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    cell = self.cells[r][c]
                    if not cell.is_revealed and not cell.is_flagged:
                        cell.reveal()
                        self.cells_revealed += 1
                        if cell.adjacent_mines == 0:
                            self.reveal_adjacent(r, c)
    
    def reveal_all_mines(self):
        """Reveal all mines when game is over"""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if cell.is_mine and not cell.is_revealed:
                    cell.reveal()
    
    def update_timer(self):
        """Update the game timer"""
        self.timer_seconds += 1
        self.update_timer_display()
    
    def update_timer_display(self):
        """Update timer display"""
        self.timer_label.setText(f'⏱️: {self.timer_seconds:03d}')
    
    def update_mines_display(self):
        """Update mines counter display"""
        remaining = self.num_mines - self.flags_placed
        self.mines_label.setText(f'💣: {remaining}')


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    game = MinesweeperGame()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
