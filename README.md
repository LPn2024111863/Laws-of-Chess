# Laws of Chess

Laws of Chess is a multiplayer, client-server chess game implemented in Python. This game bring special cards to the game to make it more thoughtfull and inovative.
The application features a robust server that handles matchmaking, game logic, and concurrent matches, along with separate clients for players and server administrators.


## Members of the group
* Gonçalo Arruda - 2024109624
* Hernâni Araújo - 2024111863

## Features

*   **Client-Server Architecture**: A dedicated server manages game state, connections, and matchmaking, allowing multiple games to run concurrently.
*   **Multiplayer Matchmaking**: Players can join a queue and be automatically matched with an opponent to start a game.
*   **Innovative Card System**: Adds a unique twist to classic chess with special abilities.
    *   **BlockRow**: Temporarily makes an entire row on the board impassable.
    *   **Impressment**: Provides a chance to steal an opponent's piece and convert it to your side.
    *   **Promotion**: Instantly upgrade one of your pieces (e.g., Pawn to Bishop/Knight, Rook to Queen).
*   **Card Acquisition Minigame**: During a match, players can compete in a quick minigame to acquire the cards.
*   **Administrator Client**: A separate terminal client for administrators to monitor the server's status, including the number of online players and active games.
*   **Complete Chess Logic**: Implements all standard chess rules, including piece movements, check, checkmate, and stalemate detection.
*   **Account System**: Players can log into accounts and the system tracks wins. **This is still under work**


## Project Structure

The repository is organized into three main components:

*   `jogo/servidor/`: Contains all the server-side logic.
    *   `maquina/`: The main server entry point that listens for and handles new connections.
    *   `matches/`: Manages the matchmaking queue (`MatchManager`) and individual game sessions (`Match`).
    *   `pieces/`: Defines the behavior and movement rules for each chess piece.
    *   `cards/`: Implements the logic for the special ability cards.
    *   `accounts/`: Handles user account creation and data storage.
    *   `processing_files/`: Manages communication threads for clients and administrators.
*   `jogo/cliente/`: The player client application.
    *   `interface/`: The command-line interface for players to interact with the game.
*   `jogo/administrator/`: The administrator client application.
    *   `interface/`: The command-line interface for administrators to query server stats.


## Thread Functionalities

The program is made with three main threads that can be created:

* `ProcessaCliente`: This thread is responsible to handle the client's messages and each thread holds one client, making available the possibility to have many at the same time.
    *   Started at: `maquina`, where the server checks for the client's ID and starts this thread if it corresponds to a client.
      
* `ProcessaAdministrador`: This thread is responsible to handle the administrator's messages and each thread holds one administrator, making available the possibility to have many  at the same time.
   *   Started at: `maquina`, where the server checks for the administrator's ID and starts this thread if ID corresponds to a administrator.   

*  `Start_game`: This thread is responsible to handle the game between two players.  
   *   Started at: `matchManager`, being accessed by `ProcessaCliente`. When a client selects `play`, it is redirected into the matchmaking queue. If it is possible to start a game (there are two players in the queue), the thread starts and the game can begin. If not, the client is prompted to wait and no input can be made until someone joins the queue and the game starts. 


## How to Play

### Player Client Commands

Once the client is running, you can use the following commands:

*   `login`: Prompts for a username to log into an account stored in `accounts.json`.
*   `play`: Enters the matchmaking queue. The server will pair you with the next available player.
*   `.`: Disconnects the client from the server.

**In-Game Commands:**

*   `select`: During your turn, use this command to choose a piece to move. You will be prompted to enter the piece's square (e.g., `e2`) and then the destination square (e.g., `e4`).
*   `cards`: During your turn, use this command to view your available cards and choose one to play.

### Administrator Client Commands

The administrator client provides a simple interface for monitoring the server:

*   `online`: Displays the current number of players connected to the server.
*   `games`: Displays the number of matches currently in progress.
*   `.`: Disconnects the administrator client.


## Next Features and Validations to be implemented

The next steps of this project include:
*   Validation: A revaluation of the code to check for more errors or missing areas that might trigger inconsistencies.
*   Progress Tracking: The accounts will be implemented in more detail so the players can check the wins, losses and win/lose ratio.
*   Cards: New cards will be implemented with new abilities to use during the game!
*   Timer: A timer will be implemented to limit the time the player has to play in a round.
*   Game Modes: Laws of Chess contains currently only the full board of pieces. Further down the project will include situations like mid game or end game so player can enjoy different scenarios.
*   Pygame: A graphic interface will be implemented so players have a more enjoyable experience
