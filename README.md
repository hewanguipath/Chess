[image1]:https://www.chess.com/bundles/web/images/offline-play/standardboard.6a504885.png

# Chess bot - Only for example inside UiPath!!!

This work flow is a demo that robot will be able to play chess
## Note: only for study purpose, if you using it play chess, you will broke the agreement with chess.com

This work flow is using Stockfish engine

# Setup Option 1, without Python:

0. download uipath community version from https://www.uipath.com/start-trial
1. download stockfish engine from https://stockfishchess.org/
3. open workflow Main_StdIO, modify In_EnginePath to the folder of your engine
4. open chess.com, login, start play, if play mode, change parameter In_PlayMode as true, false for puszzles
5. run workflow from Main_StdIO

# Setup Option 2: with Python 

0. download uipath community version from https://www.uipath.com/start-trial
1. download stockfish engine from https://stockfishchess.org/
2. modify engine.py, update the path of stockfish
3. get ready python 3.6, pip install python-chess
4. run engine.py to verify step 1-3
5. open workflow Main, modify In_Python_Path to the folder of your python
6. open chess.com, login, start play, if play mode, change parameter In_PlayMode as true, false for puszzles
7. run workflow from Main

Please be aware, your account and IP might be banned if keep playing for long.

TODO:
1. 2nd engine for Alpha-zero-chess in AI Fabric
2. Random delays to mimic human behavior  
3. Support https://www.chess.com/play/computer which has totally diffrent selectors
