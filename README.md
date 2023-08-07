# Tic Tac Toe

## Language
Python 3.9.6

## Task Requirements
1. Single-player
2. Written in Python 3.9
3. Can be a windowed or console based app.
4. AI can be as intelligent as you like.

## Features
1. GUI built with pygame
2. AI plays against you using minmax algorithm. You can toggle difficulty in code (see below)
3. Win/Lose/Draw text is show on game over
4. You can restart the game at any time by pressing the restart button.

## Future Additions
1. Optimize minmax with AB pruning
2. Add GUI option to select AI difficulty

## Install instructions
1. Download Repository and navigate to the directory that contains main.py
2. Run `python3 main.py`

## Toggle AI difficulty
1. Open `ai_player.py`
2. Uncomment the line that corresponds to the dificulty you want
```
    def doMove(self, gameBoard: GameBoard) -> bool:
        #NOTE: Only one of these two lines should be enabled
        return self.doNaiveMove(gameBoard) # This line enables easy difficulty for AI
        #return self.doExpertMove(gameBoard) # This line enables hard difficulty for AI
```
3. Save
4. Run `python3 main.py`

## Unit Tests
1. Download Repository and navigate to the directory that contains main.py
2. Run `python3 -m unittest tests/game_board_tests.py tests/cell_tests.py tests/game_tests.py tests/ai_player_tests.py`
> :warning: Do *not* run tests from test directory or else dependencies will fail to be found.

> :warning: `tests/ai_player_tests.py` is slow because it tests the expensive minmax function
