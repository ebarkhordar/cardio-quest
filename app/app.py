from flask import Flask, jsonify
import random

app = Flask(__name__)

# Initialize with default values
last_valid_state = {
    "direction": "Forward",
    "horizontal": 0.0,
    "brake": False,
    "accelerate": True
}


def get_head_direction():
    try:
        with open("head_direction.txt", "r") as file:
            content = file.read().strip()
            direction, x_angle, y_angle, z_angle = parse_head_data(content)
            # Update only if successful
            horizontal = normalize_y(float(y_angle.split(': ')[1]))
            brake = True if direction == "Looking Down" else False
            accelerate = True if direction == "Forward" else False
            # Store the last valid state
            last_valid_state.update({
                "direction": direction,
                "horizontal": horizontal,
                "brake": brake,
                "accelerate": accelerate
            })
            return direction, horizontal, brake, accelerate
    except (FileNotFoundError, ValueError):
        # Return last known good state if there's an error
        return (last_valid_state["direction"], last_valid_state["horizontal"],
                last_valid_state["brake"], last_valid_state["accelerate"])


def parse_head_data(content):
    parts = content.split(',')
    if len(parts) < 4:
        raise ValueError("Data is incomplete. Expected 4 parts separated by commas.")
    direction = parts[0].strip()
    x_angle = parts[1].strip()
    y_angle = parts[2].strip()
    z_angle = parts[3].strip()
    return direction, x_angle, y_angle, z_angle


def normalize_y(y_angle):
    y_scaled = y_angle / 5
    return max(min(y_scaled, 1), -1)


class Treadmill:
    def __init__(self):
        self.speed = 0
        self.increasing = True

    def update_speed(self):
        change = random.uniform(0, 2)
        if self.increasing and self.speed < 10:
            self.speed = min(self.speed + change, 10)
        elif not self.increasing and self.speed > 0:
            self.speed = max(self.speed - change, 0)
        if self.speed == 10 and random.random() < 0.3:
            self.increasing = False
        elif self.speed == 0:
            self.increasing = True
        return round(self.speed, 2)


treadmill = Treadmill()


@app.route('/')
def home():
    return "Treadmill Simulator Server is Running"


@app.route('/treadmill')
def treadmill_status():
    speed = treadmill.update_speed()
    direction, horizontal, brake, accelerate = get_head_direction()
    return jsonify({
        "Horizontal": horizontal,
        "Brake": brake,
        "Accelerate": accelerate,
        "Speed": speed
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
