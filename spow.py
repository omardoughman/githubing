import tkinter as tk
from tkinter import messagebox
import logging
import os
import sys

# 1. Setup Logging (So your .service file can record what happens)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("spow.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class SpowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spow System Tool")
        self.root.geometry("400x250")
        self.root.configure(bg="#2c3e50") # Dark professional theme

        # UI Elements
        self.label = tk.Label(
            root, 
            text="spow", 
            name="main_label",
            font=("Helvetica", 48, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        self.label.pack(expand=True)

        self.status_label = tk.Label(
            root, 
            text=f"Running on: {sys.platform}",
            font=("Arial", 10),
            fg="#bdc3c7",
            bg="#2c3e50"
        )
        self.status_label.pack(side="bottom", pady=10)

        # Log start
        logging.info("Spow GUI initialized successfully.")

        # Bind closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        logging.info("Closing Spow App...")
        self.root.destroy()

# 2. Main Execution Block
if __name__ == "__main__":
    # Check for DISPLAY environment variable (Critical for Linux Services)
    if os.name != 'nt' and 'DISPLAY' not in os.environ:
        logging.error("No DISPLAY found. If running as a service, check your .service file.")
        sys.exit(1)

    root = tk.Tk()
    app = SpowApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        logging.info("Spow stopped by user (Ctrl+C).")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
