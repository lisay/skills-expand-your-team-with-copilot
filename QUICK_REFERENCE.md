# 扫雷游戏快速参考 / Minesweeper Quick Reference

## 🎮 快速开始 / Quick Start

```bash
python3 minesweeper.py
```

## 🎯 游戏目标 / Objective

找出所有不含地雷的格子
Find all cells that don't contain mines

## 🖱️ 控制方式 / Controls

| 操作 / Action | 按键 / Key | 效果 / Effect |
|--------------|-----------|--------------|
| 揭开格子 / Reveal cell | 左键 / Left click | 显示内容 / Show content |
| 标记旗帜 / Flag mine | 右键 / Right click | 放置/移除旗帜 / Toggle flag |
| 新游戏 / New game | 按钮 / Button | 重新开始 / Restart |
| 切换难度 / Change difficulty | 下拉菜单 / Dropdown | 选择关卡 / Select level |

## 📊 难度等级 / Difficulty Levels

| 级别 / Level | 大小 / Size | 地雷 / Mines | 格子 / Cells |
|-------------|------------|-------------|-------------|
| 简单 / Beginner | 9×9 | 10 | 81 |
| 中等 / Intermediate | 16×16 | 40 | 256 |
| 困难 / Expert | 16×30 | 99 | 480 |

## 🔢 数字含义 / Number Meanings

格子中的数字表示周围8个格子中有多少个地雷
Numbers show how many mines are in the 8 surrounding cells

| 数字 / Number | 颜色 / Color | 含义 / Meaning |
|--------------|-------------|---------------|
| 1 | 蓝色 / Blue | 1个相邻地雷 / 1 adjacent mine |
| 2 | 绿色 / Green | 2个相邻地雷 / 2 adjacent mines |
| 3 | 红色 / Red | 3个相邻地雷 / 3 adjacent mines |
| 4 | 深蓝 / Navy | 4个相邻地雷 / 4 adjacent mines |
| 5 | 深红 / Maroon | 5个相邻地雷 / 5 adjacent mines |
| 6 | 青色 / Teal | 6个相邻地雷 / 6 adjacent mines |
| 7 | 黑色 / Black | 7个相邻地雷 / 7 adjacent mines |
| 8 | 灰色 / Gray | 8个相邻地雷 / 8 adjacent mines |

## 🚩 符号说明 / Symbol Guide

| 符号 / Symbol | 含义 / Meaning |
|--------------|---------------|
| 💣 | 地雷 / Mine |
| 🚩 | 旗帜标记 / Flag marker |
| 空白 / Blank | 无相邻地雷 / No adjacent mines |
| 数字 / Number | 相邻地雷数 / Adjacent mine count |

## 💡 游戏提示 / Game Tips

### 基础技巧 / Basic Tips

1. **首次点击安全** / **First click is safe**
   - 第一次点击永远不会是地雷
   - The first click will never be a mine

2. **从数字推理** / **Use numbers to deduce**
   - 数字告诉你周围有多少地雷
   - Numbers tell you how many mines are nearby

3. **标记可疑位置** / **Flag suspicious cells**
   - 用右键标记你认为是地雷的格子
   - Right-click to mark cells you think are mines

4. **关注地雷计数** / **Watch mine counter**
   - 💣计数器显示剩余地雷数
   - The 💣 counter shows remaining mines

### 高级技巧 / Advanced Tips

1. **角落和边缘** / **Corners and edges**
   - 这些位置的选择更少，更容易推理
   - Fewer possibilities make them easier to solve

2. **1-2-1模式** / **1-2-1 pattern**
   - 常见的安全模式，中间两侧是地雷
   - Common safe pattern with mines on sides

3. **空格连锁** / **Empty cell chains**
   - 点击空格会自动揭开周围的安全格子
   - Clicking empty cells reveals safe neighbors

4. **计数验证** / **Count verification**
   - 用旗帜数量验证数字提示
   - Use flag count to verify number hints

## ⚠️ 常见错误 / Common Mistakes

1. ❌ **随意点击** / **Random clicking**
   - ✅ 总是基于数字推理 / Always use number logic

2. ❌ **忘记标记** / **Forgetting to flag**
   - ✅ 标记已知地雷以避免误点 / Flag known mines

3. ❌ **忽略边缘** / **Ignoring edges**
   - ✅ 边缘和角落容易解决 / Edges and corners are easier

4. ❌ **急于求成** / **Rushing**
   - ✅ 仔细思考每一步 / Think carefully about each move

## 🏆 胜利条件 / Win Conditions

✅ 揭开所有非地雷格子
✅ Reveal all non-mine cells

## 💥 失败条件 / Lose Conditions

❌ 点击到地雷格子
❌ Click on a mine cell

## 📈 进阶策略 / Advanced Strategy

### 概率计算 / Probability Calculation
- 使用已知信息计算未知格子含雷概率
- Calculate mine probability for unknown cells

### 模式识别 / Pattern Recognition
- 学习识别常见的地雷排列模式
- Learn to recognize common mine patterns

### 边界优先 / Border First Strategy
- 优先处理已知区域边界
- Work on borders of known areas first

## 📞 需要帮助？ / Need Help?

查看完整文档：
See full documentation:

- `README.md` - 完整说明 / Full instructions
- `VISUAL_GUIDE.md` - 可视化指南 / Visual guide
- `UI_STRUCTURE.md` - 界面说明 / UI details
- `PROJECT_SUMMARY.md` - 项目概览 / Project overview

## 🎮 开始游戏！ / Start Playing!

```bash
# 方法1 / Method 1
python3 minesweeper.py

# 方法2 / Method 2
./run_game.sh
```

**祝你好运！ / Good luck!** 🍀
**玩得开心！ / Have fun!** 🎉
