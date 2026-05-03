# Use a lightweight Python image
FROM python:3.11-slim

# Install Tkinter and the X11 libraries needed for GUI
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Create the script directly inside the container
RUN echo 'import tkinter as tk; \
root = tk.Tk(); \
root.title("Spow"); \
root.geometry("300x200"); \
tk.Label(root, text="spow", font=("Arial", 30)).pack(expand=True); \
root.mainloop()' > /spow_app.py

# Run it automatically
CMD ["python", "/spow_app.py"]
