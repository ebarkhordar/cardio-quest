## Running the Application

0. **Go to app directory**:
   ```bash
   cd app/
   ```
1. **Start the server**:
   ```bash
   flask run --host=0.0.0.0
   ```

   This command will start the Flask server accessible on port 5000 across all network interfaces.

2. **Access the API**:
   - **Homepage**: Navigate to `http://<host-ip-address>:5000` to check if the server is running.
   - **Treadmill Status**: Visit `http://<host-ip-address>:5000/treadmill` to get the current treadmill settings based on the head direction data.

Ensure the `head_direction.txt` file is in the project directory with correct formatting for head directions.

## Running the Unity Game

To run the associated Unity game that connects with this Flask server:

1. **Open the Unity Editor**:
   - Launch Unity and open the project that corresponds to this server.

2. **Build and Run the Game**:
   - In the Unity Editor, go to `File > Build & Run`. This will compile the game and run it on your computer.
   - Ensure the game's configuration or script is set to connect to `http://localhost:5000` or the appropriate IP address if accessing over a network.

3. **Game Interaction**:
   - The game should automatically connect to the Flask server once started. Ensure the server is running before you start the game to fetch real-time treadmill data.
