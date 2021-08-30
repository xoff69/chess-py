# chess-py

Python tool to analyze chess at PGN Format.

https://github.com/niklasf/chess-openings


# TODO 
bug sur la reconnaissance des ouvertures

#### Author
- [Christophe PICHON] https://www.linkedin.com/in/christophe-pichon-25003b48/
Comments, suggestions and improvements are welcome and appreciated.


#### License

`chess-py` is licensed under the [GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007" license](./LICENSE.md).

#### Installation

Dependencies
You will need a UCI chess engine for analysis. stockfish is the default.https://stockfishchess.org/ 
and https://anaconda.org/hcc/stockfish

This tool needs the followings libs
- matplot (Python)
- python chess (Python)
- config parser  (Python)

 
 Information:
 - opening/openings.py is a lib to manage openings informations stored mainly in eco.txt (french names)
 - pgnstat.cfg contains configuration option, the player name mostly
 - <player>_game_analysis contains cache for analyzed game
 Before running:
 - setup engine in  pgnstat.cfg
 - player is set in pgnstat.cfg
 - setup path in pgnstat.cfg  for pgn where are your pgn files,
 - eco for opening path
 Running:
 - just run pgn.py, you can change settings in pgnstat.cfg before 
 the result is stored in a pdf file named <player>.pdf where player is set in pgnstat.cfg
 - 
 - 
 Todo/improvement:
 - add more internationalization
 - apparence of some arrays
 - improve table presentation
 - opening determination
 - remove graphs from console


#### Contributing

There are many ways to contribute to this package:

- Report an issue if you encounter some odd behavior, or if you have suggestions to improve the package.
- Contribute with code addressing some open issues, that add new functionality or that improve the performance.
- When contributing with code, add docstrings and comments, so others may understand the methods implemented.
- Contribute by updating and improving the documentation.
