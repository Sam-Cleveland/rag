import tkinter as tk
from tkinter import ttk
import colorsys

class DarkThemeGUI:
    def __init__(self, root, on_enter_callback=None):
        self.root = root
        self.root.title("Word Distance Viewer")
        
        # Configure dark theme colors
        self.bg_color = "#2b2b2b"
        self.fg_color = "#ffffff"
        self.input_bg = "#3b3b3b"
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create list display
        self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add a loading label
        self.loading_label = tk.Label(
            self.list_frame,
            text="Loading...",
            bg=self.bg_color,
            fg=self.fg_color,
            anchor='center'
        )
        self.loading_label.pack(expand=True)
        
        # Create text input at bottom
        self.input_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.text_input = tk.Entry(
            self.input_frame,
            bg=self.input_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,  # Cursor color
            relief=tk.FLAT
        )
        self.text_input.pack(fill=tk.X, pady=(10, 0))
        self.text_input.bind('<Return>', self.on_enter)
        
        # Sample data - replace with your actual data
        self.sample_data = []
        
        self.on_enter_callback = on_enter_callback  # Store the callback
    
    def get_color_for_distance(self, distance):
        """Convert distance (0.1-10) to a color between green and red"""
        # Normalize distance to 0-1 range
        normalized_distance = (distance - 0.1) / (2 - 0.1)
        # Convert to HSV color (120 is green, 0 is red)
        hue = 120 * (1 - normalized_distance)
        # Convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hue/360, 1, 0.8)
        # Convert to hex color
        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    
    def update_list(self):
        # Clear existing items
        for widget in self.list_frame.winfo_children():
            widget.destroy()
            
        # Add items
        for word, distance in self.sample_data:
            item_frame = tk.Frame(self.list_frame, bg=self.bg_color)
            item_frame.pack(fill=tk.X, pady=2)
            
            # Word label
            word_label = tk.Label(
                item_frame,
                text=word,
                bg=self.bg_color,
                fg=self.fg_color,
                anchor='w'
            )
            word_label.pack(side=tk.LEFT, padx=(10, 20))
            
            # Distance label with color
            distance_label = tk.Label(
                item_frame,
                text=f"{distance:.3f}",
                bg=self.bg_color,
                fg=self.get_color_for_distance(distance),
                anchor='e'
            )
            distance_label.pack(side=tk.RIGHT, padx=10)
    
    def show_loading(self):
        # Show loading message
        self.loading_label.pack(expand=True)
    
    def hide_loading_and_update_list(self):
        # Hide loading message and update list
        self.loading_label.pack_forget()
        self.update_list()
    
    def update_loading_text(self, new_text):
        """Update the loading label's text."""
        self.loading_label.config(text=new_text)
    
    def on_enter(self, event):
        # Handle text input - call the callback if provided
        text = self.text_input.get()
        if self.on_enter_callback:
            self.on_enter_callback(text)  # Call the custom callback
        else:
            print(f"Input received: {text}")