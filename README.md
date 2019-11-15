# Chess bot - Only for internal example inside UiPath!!!

This work flow depends on Stockfish and python-chess 

How to setup:
1. download stockfish engine from https://stockfishchess.org/
2. modify engine.py, update the path of stockfish
3. get ready python 3.6, pip install python-chess
4. run engine.py to verify step 1-3
5. open workflow, modify In_Python_Path to the folder of your python
6. open chess.com, login, start play, if play mode, change parameter In_PlayMode as true, false for puszzles
7. run
Note, your account and IP might be banned if keep playing for a while.

TODO:
1. 2nd engine for Alpha-zero-chess in AI Fab
2. Random delays to Mimic human behavior  
