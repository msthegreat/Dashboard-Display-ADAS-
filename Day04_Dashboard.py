import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math

class AutonomousVehicleDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Autonomous Vehicle Dashboard")

        # Variables for simulated data
        self.battery_level = tk.DoubleVar()
        self.steering_angle = tk.DoubleVar()
        self.indicators = tk.StringVar()
        self.gear = tk.StringVar()
        self.speed = tk.DoubleVar()

        # Set initial values
        self.battery_level.set(50.0)
        self.steering_angle.set(0.0)
        self.indicators.set("Off")
        self.gear.set("Neutral")
        self.speed.set(0.0)

        # Load images
        self.car_image = ImageTk.PhotoImage(Image.open("2.jpg"))

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Battery Level
        battery_label = tk.Label(self.root, text="Battery Level:")
        battery_label.grid(row=0, column=0, padx=10, pady=10)
        battery_slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal", variable=self.battery_level)
        battery_slider.grid(row=0, column=1, padx=10, pady=10)

        # Steering Angle
        steering_label = tk.Label(self.root, text="Steering Angle:")
        steering_label.grid(row=1, column=0, padx=10, pady=10)
        steering_slider = tk.Scale(self.root, from_=-180, to=180, orient="horizontal", variable=self.steering_angle)
        steering_slider.grid(row=1, column=1, padx=10, pady=10)

        # Indicators
        indicators_label = tk.Label(self.root, text="Indicators:")
        indicators_label.grid(row=2, column=0, padx=10, pady=10)
        indicators_combobox = ttk.Combobox(self.root, values=["Left", "Right", "Off"], textvariable=self.indicators)
        indicators_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Gear
        gear_label = tk.Label(self.root, text="Gear:")
        gear_label.grid(row=3, column=0, padx=10, pady=10)
        gear_combobox = ttk.Combobox(self.root, values=["Reverse", "Neutral","drive"], textvariable=self.gear)
        gear_combobox.grid(row=3, column=1, padx=10, pady=10)

        # Speed
        speed_label = tk.Label(self.root, text="Speed:")
        speed_label.grid(row=4, column=0, padx=10, pady=10)
        speed_scale = tk.Scale(self.root, from_=0, to=120, orient="horizontal", variable=self.speed)
        speed_scale.grid(row=4, column=1, padx=10, pady=10)

        # Image
        car_image_label = tk.Label(self.root, image=self.car_image)
        car_image_label.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

        # Canvas for Speedometer
        self.speed_canvas = tk.Canvas(self.root, width=100, height=100)
        self.speed_canvas.grid(row=0, column=3, rowspan=5, padx=10, pady=10)

        # Update Button
        update_button = tk.Button(self.root, text="Update", command=self.update_dashboard)
        update_button.grid(row=5, column=0, columnspan=4, pady=10)

    def update_dashboard(self):
        # Display the input values
        self.draw_speed_odometer()

    def draw_speed_odometer(self):
        speed_value = self.speed.get()
        speed_angle = 180 - (speed_value / 120) * 180

        # Clear previous drawings
        self.speed_canvas.delete("all")

        # Draw speedometer circle
        self.speed_canvas.create_oval(10, 10, 90, 90, outline="black", width=2)

        # Draw speedometer needle
        speed_needle_x = 50 + 40 * math.cos(math.radians(speed_angle))
        speed_needle_y = 50 - 40 * math.sin(math.radians(speed_angle))
        self.speed_canvas.create_line(50, 50, speed_needle_x, speed_needle_y, width=2, arrow=tk.LAST)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutonomousVehicleDashboard(root)
    root.mainloop()
