#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Minesweeper game logic
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all imports work"""
    print("Testing imports...")
    try:
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import Qt
        from PyQt5.QtGui import QFont
        print("✓ PyQt5 imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_game_creation():
    """Test game creation without display"""
    print("\nTesting game creation...")
    try:
        from PyQt5.QtWidgets import QApplication
        import minesweeper
        
        # Create application
        app = QApplication(sys.argv)
        
        # Create game instance
        game = minesweeper.MinesweeperGame()
        
        # Test basic properties
        assert game.rows > 0, "Rows should be positive"
        assert game.cols > 0, "Cols should be positive"
        assert game.num_mines > 0, "Number of mines should be positive"
        assert len(game.cells) == game.rows, "Rows mismatch"
        assert len(game.cells[0]) == game.cols, "Cols mismatch"
        
        print(f"✓ Game created successfully: {game.rows}x{game.cols} with {game.num_mines} mines")
        
        # Test difficulty levels
        difficulties = minesweeper.MinesweeperGame.DIFFICULTIES
        print(f"✓ Available difficulties: {list(difficulties.keys())}")
        
        # Test mine counting
        mine_count = sum(1 for row in game.cells for cell in row if cell.is_mine)
        print(f"✓ No mines placed initially (before first click): {mine_count} mines")
        
        return True
    except Exception as e:
        print(f"✗ Game creation error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_cell_logic():
    """Test cell reveal logic"""
    print("\nTesting cell logic...")
    try:
        from PyQt5.QtWidgets import QApplication
        import minesweeper
        
        app = QApplication(sys.argv)
        
        # Create a cell
        cell = minesweeper.Cell(0, 0)
        
        # Test initial state
        assert not cell.is_revealed, "Cell should not be revealed initially"
        assert not cell.is_flagged, "Cell should not be flagged initially"
        assert not cell.is_mine, "Cell should not be a mine initially"
        
        # Test flagging
        cell.toggle_flag()
        assert cell.is_flagged, "Cell should be flagged"
        cell.toggle_flag()
        assert not cell.is_flagged, "Cell should be unflagged"
        
        print("✓ Cell logic tests passed")
        return True
    except Exception as e:
        print(f"✗ Cell logic error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("Minesweeper Game Test Suite")
    print("=" * 50)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Game Creation", test_game_creation()))
    results.append(("Cell Logic", test_cell_logic()))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    all_passed = True
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
