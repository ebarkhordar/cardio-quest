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

