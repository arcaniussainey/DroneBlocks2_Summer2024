# Introduction to Tkinter

Tkinter (pronounced "T-K-inter") is Python's built-in library for creating graphical user interfaces (GUIs). Unlike command-line programs that only show text, Tkinter lets you create windows with buttons, text boxes, images, and other visual elements that users can click and interact with. Think of it as the tool that helps you build desktop applications that look and feel like the programs you use every day.

Tkinter comes pre-installed with Python, so you don't need to download anything extra. It's perfect for creating simple desktop applications, data visualization tools, or even control panels for hardware projects like drones. The name "Tkinter" stands for "Tk interface" - Tk is the underlying graphics toolkit that Tkinter uses to create windows and widgets.

In this tutorial, we'll start with simple GUI applications and gradually work up to more complex projects that combine Tkinter with computer vision and drone control. By the end, you'll be able to create professional-looking desktop applications with real functionality.

## Why Use Tkinter?

Tkinter offers several advantages for beginners:
- **Built-in**: No additional installations required
- **Cross-platform**: Works on Windows, Mac, and Linux
- **Simple syntax**: Easy to learn and understand
- **Flexible**: Can create everything from simple forms to complex applications
- **Great for prototyping**: Quick to test ideas and build working demos

# Basic GUI App

Let's start with the simplest possible Tkinter application - a window with a couple of buttons that actually do something when clicked.

## Your First Window

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("300x200")  # Width x Height in pixels

# Start the GUI event loop
root.mainloop()
```

This creates an empty window. The `mainloop()` function keeps the window open and responsive to user interactions. Without it, the window would appear and immediately close.

## Adding Interactive Buttons

Now let's add some buttons that respond when clicked:

```python
import tkinter as tk
from tkinter import messagebox

def button_click():
    """Function called when the button is clicked"""
    messagebox.showinfo("Button Clicked", "Hello! You clicked the button!")

def close_app():
    """Function to close the application"""
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

# Create buttons
hello_button = tk.Button(root, text="Click Me!", command=button_click)
hello_button.pack(pady=20)  # pady adds vertical padding

close_button = tk.Button(root, text="Close App", command=close_app, bg="red", fg="white")
close_button.pack(pady=10)

# Start the GUI
root.mainloop()
```

The key concepts here are:
- **Functions**: We define what happens when buttons are clicked
- **Commands**: The `command` parameter connects buttons to functions
- **Pack**: This arranges widgets in the window
- **Styling**: We can change colors with `bg` (background) and `fg` (foreground/text)

## Adding Text Input

Most applications need to get input from users. Let's create an app that takes text input and displays it:

```python
import tkinter as tk
from tkinter import messagebox

def process_text():
    """Get text from the input field and display it"""
    user_text = text_entry.get()  # Get text from the entry widget
    
    if user_text.strip():  # Check if text isn't empty
        messagebox.showinfo("Your Input", f"You entered: {user_text}")
        text_entry.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Empty Input", "Please enter some text!")

def clear_text():
    """Clear the input field"""
    text_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Text Input Example")
root.geometry("400x250")

# Create and pack widgets
tk.Label(root, text="Enter your text below:", font=("Arial", 12)).pack(pady=10)

text_entry = tk.Entry(root, width=30, font=("Arial", 11))
text_entry.pack(pady=10)

# Frame to hold buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

process_button = tk.Button(button_frame, text="Process Text", command=process_text, bg="green", fg="white")
process_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, bg="orange", fg="white")
clear_button.pack(side=tk.LEFT, padx=10)

# Focus on the text entry when the app starts
text_entry.focus()

root.mainloop()
```

New concepts introduced:
- **Entry widget**: For single-line text input
- **Label widget**: For displaying text
- **Frames**: Containers to group and organize widgets
- **Font styling**: Making text larger and changing fonts
- **Focus**: Making a widget active when the app starts

# Combining Tkinter with OpenCV

OpenCV is a powerful computer vision library, and combining it with Tkinter creates applications that can process and display images with a user-friendly interface. This is perfect for image analysis projects or computer vision demonstrations.

## File Selection and Image Display

Let's create an application that lets users select an image file and displays it in the GUI:

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer with OpenCV")
        self.root.geometry("800x600")
        
        self.current_image = None
        self.original_image = None
        
        self.setup_gui()
    
    def setup_gui(self):
        """Create the GUI elements"""
        # Control frame for buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="Select Image", command=self.select_image, 
                 bg="blue", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(control_frame, text="Convert to Grayscale", command=self.convert_grayscale,
                 bg="gray", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(control_frame, text="Reset to Original", command=self.reset_image,
                 bg="green", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        # Image display area
        self.image_label = tk.Label(self.root, text="No image selected", 
                                   bg="lightgray", width=60, height=20)
        self.image_label.pack(pady=20, expand=True, fill=tk.BOTH)
    
    def select_image(self):
        """Open file dialog to select an image"""
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Load image with OpenCV
                self.original_image = cv2.imread(file_path)
                self.current_image = self.original_image.copy()
                
                if self.original_image is not None:
                    self.display_image()
                else:
                    messagebox.showerror("Error", "Could not load the selected image!")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image(self):
        """Display the current image in the GUI"""
        if self.current_image is not None:
            # Resize image to fit in the display area
            display_image = self.resize_for_display(self.current_image)
            
            # Convert from BGR (OpenCV) to RGB (PIL/Tkinter)
            rgb_image = cv2.cvtColor(display_image, cv2.COLOR_BGR2RGB)
            
            # Convert to PIL Image and then to PhotoImage for Tkinter
            pil_image = Image.fromarray(rgb_image)
            photo = ImageTk.PhotoImage(pil_image)
            
            # Update the label
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
    
    def resize_for_display(self, image, max_width=600, max_height=400):
        """Resize image to fit in the display area while maintaining aspect ratio"""
        height, width = image.shape[:2]
        
        # Calculate scaling factor
        scale = min(max_width/width, max_height/height)
        
        if scale < 1:
            new_width = int(width * scale)
            new_height = int(height * scale)
            return cv2.resize(image, (new_width, new_height))
        
        return image
    
    def convert_grayscale(self):
        """Convert current image to grayscale"""
        if self.current_image is not None:
            gray = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
            # Convert back to 3-channel for consistent display
            self.current_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            self.display_image()
        else:
            messagebox.showwarning("No Image", "Please select an image first!")
    
    def reset_image(self):
        """Reset to the original image"""
        if self.original_image is not None:
            self.current_image = self.original_image.copy()
            self.display_image()
        else:
            messagebox.showwarning("No Image", "No original image to reset to!")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
```

This example demonstrates several important concepts:

**Class-based GUI**: Using a class to organize our code makes it easier to manage state (like the current image) and creates reusable components.

**File dialogs**: The `filedialog.askopenfilename()` function creates a standard file selection window that users are familiar with.

**Image format conversion**: OpenCV uses BGR color format, but Tkinter expects RGB, so we need to convert between them.

**Dynamic resizing**: Images are automatically resized to fit in the display area while maintaining their aspect ratio.

## Advanced Image Processing Example

Let's extend our image viewer with more OpenCV features:

```python
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cv2
from PIL import Image, ImageTk
import numpy as np

class AdvancedImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Image Processor")
        self.root.geometry("900x700")
        
        self.current_image = None
        self.original_image = None
        
        self.setup_gui()
    
    def setup_gui(self):
        """Create the GUI with multiple processing options"""
        # Main control frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # File operations
        file_frame = tk.Frame(control_frame)
        file_frame.pack(pady=5)
        
        tk.Button(file_frame, text="Select Image", command=self.select_image,
                 bg="blue", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Save Image", command=self.save_image,
                 bg="purple", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Reset", command=self.reset_image,
                 bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        
        # Processing options
        process_frame = tk.Frame(control_frame)
        process_frame.pack(pady=5)
        
        tk.Button(process_frame, text="Blur", command=self.apply_blur,
                 bg="orange").pack(side=tk.LEFT, padx=3)
        tk.Button(process_frame, text="Edge Detection", command=self.detect_edges,
                 bg="green", fg="white").pack(side=tk.LEFT, padx=3)
        tk.Button(process_frame, text="Brighten", command=self.brighten_image,
                 bg="yellow").pack(side=tk.LEFT, padx=3)
        tk.Button(process_frame, text="Find Contours", command=self.find_contours,
                 bg="cyan").pack(side=tk.LEFT, padx=3)
        
        # Image display
        self.image_label = tk.Label(self.root, text="Select an image to begin",
                                   bg="lightgray", width=80, height=25)
        self.image_label.pack(pady=20, expand=True, fill=tk.BOTH)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                            relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def select_image(self):
        """Select and load an image file"""
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.original_image = cv2.imread(file_path)
                if self.original_image is not None:
                    self.current_image = self.original_image.copy()
                    self.display_image()
                    self.status_var.set(f"Loaded: {file_path.split('/')[-1]}")
                else:
                    messagebox.showerror("Error", "Could not load image!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def save_image(self):
        """Save the current processed image"""
        if self.current_image is not None:
            file_path = filedialog.asksaveasfilename(
                title="Save Image",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
            )
            
            if file_path:
                cv2.imwrite(file_path, self.current_image)
                self.status_var.set(f"Saved: {file_path.split('/')[-1]}")
        else:
            messagebox.showwarning("No Image", "No image to save!")
    
    def display_image(self):
        """Display the current image"""
        if self.current_image is not None:
            # Resize for display
            display_img = self.resize_for_display(self.current_image)
            
            # Handle both color and grayscale images
            if len(display_img.shape) == 3:
                rgb_image = cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)
            else:
                rgb_image = cv2.cvtColor(display_img, cv2.COLOR_GRAY2RGB)
            
            pil_image = Image.fromarray(rgb_image)
            photo = ImageTk.PhotoImage(pil_image)
            
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
    
    def resize_for_display(self, image, max_width=700, max_height=500):
        """Resize image while maintaining aspect ratio"""
        if len(image.shape) == 3:
            height, width = image.shape[:2]
        else:
            height, width = image.shape
        
        scale = min(max_width/width, max_height/height)
        
        if scale < 1:
            new_width = int(width * scale)
            new_height = int(height * scale)
            return cv2.resize(image, (new_width, new_height))
        
        return image
    
    def apply_blur(self):
        """Apply Gaussian blur to the image"""
        if self.current_image is not None:
            self.current_image = cv2.GaussianBlur(self.current_image, (15, 15), 0)
            self.display_image()
            self.status_var.set("Applied blur effect")
        else:
            messagebox.showwarning("No Image", "Please select an image first!")
    
    def detect_edges(self):
        """Apply edge detection using Canny algorithm"""
        if self.current_image is not None:
            gray = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            self.current_image = edges  # Store as grayscale
            self.display_image()
            self.status_var.set("Applied edge detection")
        else:
            messagebox.showwarning("No Image", "Please select an image first!")
    
    def brighten_image(self):
        """Increase image brightness"""
        if self.current_image is not None:
            # Add 30 to all pixel values, but cap at 255
            self.current_image = cv2.add(self.current_image, np.ones(self.current_image.shape, dtype=np.uint8) * 30)
            self.display_image()
            self.status_var.set("Brightened image")
        else:
            messagebox.showwarning("No Image", "Please select an image first!")
    
    def find_contours(self):
        """Find and draw contours on the image"""
        if self.current_image is not None:
            # Convert to grayscale for contour detection
            gray = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
            
            # Apply threshold to get binary image
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            
            # Find contours
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Draw contours on a copy of the original
            contour_image = self.current_image.copy()
            cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
            
            self.current_image = contour_image
            self.display_image()
            self.status_var.set(f"Found {len(contours)} contours")
        else:
            messagebox.showwarning("No Image", "Please select an image first!")
    
    def reset_image(self):
        """Reset to original image"""
        if self.original_image is not None:
            self.current_image = self.original_image.copy()
            self.display_image()
            self.status_var.set("Reset to original image")
        else:
            messagebox.showwarning("No Image", "No original image to reset to!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedImageProcessor(root)
    root.mainloop()
```

This advanced example introduces:
- **Multiple image processing techniques**: Blur, edge detection, brightness adjustment, and contour finding
- **Save functionality**: Users can save their processed images
- **Status bar**: Provides feedback about current operations
- **Better error handling**: More robust handling of different image types and edge cases

# Combining Tkinter with Matplotlib

Matplotlib is Python's main plotting library, and embedding plots in Tkinter applications creates powerful data visualization tools. Instead of showing plots in separate windows, we can integrate them directly into our GUI.

## Basic Chart Integration

Let's start with a simple example that creates different types of charts:

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import csv

class DataVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization Tool")
        self.root.geometry("1000x700")
        
        self.data = None
        self.figure = None
        self.canvas = None
        
        self.setup_gui()
        self.create_sample_data()
    
    def setup_gui(self):
        """Create the main GUI layout"""
        # Control panel on the left
        control_frame = tk.Frame(self.root, width=200, bg="lightgray")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        control_frame.pack_propagate(False)
        
        tk.Label(control_frame, text="Data Visualization", font=("Arial", 14, "bold"), 
                bg="lightgray").pack(pady=10)
        
        # Data source buttons
        tk.Button(control_frame, text="Load CSV File", command=self.load_csv_file,
                 bg="blue", fg="white", width=18).pack(pady=5)
        tk.Button(control_frame, text="Use Sample Data", command=self.create_sample_data,
                 bg="green", fg="white", width=18).pack(pady=5)
        
        tk.Label(control_frame, text="Chart Types:", font=("Arial", 12, "bold"),
                bg="lightgray").pack(pady=(20, 5))
        
        # Chart type buttons
        tk.Button(control_frame, text="Bar Chart", command=self.create_bar_chart,
                 width=18).pack(pady=2)
        tk.Button(control_frame, text="Line Chart", command=self.create_line_chart,
                 width=18).pack(pady=2)
        tk.Button(control_frame, text="Pie Chart", command=self.create_pie_chart,
                 width=18).pack(pady=2)
        tk.Button(control_frame, text="Scatter Plot", command=self.create_scatter_plot,
                 width=18).pack(pady=2)
        tk.Button(control_frame, text="Histogram", command=self.create_histogram,
                 width=18).pack(pady=2)
        
        # Chart area on the right
        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Initialize with empty chart area
        self.init_chart_area()
    
    def init_chart_area(self):
        """Initialize the matplotlib figure and canvas"""
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self.chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initial empty plot
        self.ax.text(0.5, 0.5, 'Select a chart type to begin', 
                    horizontalalignment='center', verticalalignment='center',
                    transform=self.ax.transAxes, fontsize=16)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()
    
    def create_sample_data(self):
        """Create sample data for demonstration"""
        self.data = {
            'categories': ['Category A', 'Category B', 'Category C', 'Category D', 'Category E'],
            'values': [23, 45, 56, 78, 32],
            'x_data': np.linspace(0, 10, 50),
            'y_data': np.sin(np.linspace(0, 10, 50)) * 50 + np.random.normal(0, 5, 50),
            'random_data': np.random.normal(100, 15, 1000)
        }
        messagebox.showinfo("Data Loaded", "Sample data has been created successfully!")
    
    def load_csv_file(self):
        """Load data from a CSV file"""
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                    
                    if len(rows) < 2:
                        messagebox.showerror("Error", "CSV file must have at least 2 rows (header + data)")
                        return
                    
                    headers = rows[0]
                    data_rows = rows[1:]
                    
                    # Try to convert numeric columns
                    self.data = {}
                    for i, header in enumerate(headers):
                        column_data = [row[i] for row in data_rows if i < len(row)]
                        
                        # Try to convert to numbers
                        try:
                            numeric_data = [float(val) for val in column_data if val.strip()]
                            self.data[header] = numeric_data
                        except ValueError:
                            # Keep as text if conversion fails
                            self.data[header] = column_data
                    
                    messagebox.showinfo("Success", f"Loaded data from {file_path.split('/')[-1]}")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV: {str(e)}")
    
    def clear_plot(self):
        """Clear the current plot"""
        self.ax.clear()
    
    def create_bar_chart(self):
        """Create a bar chart from the data"""
        if not self.data:
            messagebox.showwarning("No Data", "Please load data first!")
            return
        
        self.clear_plot()
        
        if 'categories' in self.data and 'values' in self.data:
            bars = self.ax.bar(self.data['categories'], self.data['values'], 
                              color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
            self.ax.set_title('Bar Chart', fontsize=16, fontweight='bold')
            self.ax.set_ylabel('Values')
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height}', ha='center', va='bottom')
        else:
            # Use first two numeric columns found
            numeric_cols = [(k, v) for k, v in self.data.items() if isinstance(v[0], (int, float))]
            if len(numeric_cols) >= 1:
                values = numeric_cols[0][1][:10]  # Limit to 10 items
                labels = [f'Item {i+1}' for i in range(len(values))]
                self.ax.bar(labels, values, color='skyblue')
                self.ax.set_title(f'Bar Chart - {numeric_cols[0][0]}', fontsize=16, fontweight='bold')
            else:
                self.ax.text(0.5, 0.5, 'No suitable data for bar chart', 
                           ha='center', va='center', transform=self.ax.transAxes)
        
        plt.setp(self.ax.get_xticklabels(), rotation=45, ha='right')
        self.figure.tight_layout()
        self.canvas.draw()
    
    def create_line_chart(self):
        """Create a line chart"""
        if not self.data:
            messagebox.showwarning("No Data", "Please load data first!")
            return
        
        self.clear_plot()
        
        if 'x_data' in self.data and 'y_data' in self.data:
            self.ax.plot(self.data['x_data'], self.data['y_data'], 
                        marker='o', linestyle='-', color='#FF6B6B', linewidth=2, markersize=4)
            self.ax.set_title('Line Chart - Sample Data', fontsize=16, fontweight='bold')
            self.ax.set_xlabel('X Values')
            self.ax.set_ylabel('Y Values')
            self.ax.grid(True, alpha=0.3)
        else:
            # Use first numeric column
            numeric_cols = [(k, v) for k, v in self.data.items() if isinstance(v[0], (int, float))]
            if numeric_cols:
                values = numeric_cols[0][1][:50]  # Limit to 50 points
                x_vals = list(range(len(values)))
                self.ax.plot(x_vals, values, marker='o', linestyle='-', linewidth=2)
                self.ax.set_title(f'Line Chart - {numeric_cols[0][0]}', fontsize=16, fontweight='bold')
                self.ax.grid(True, alpha=0.3)
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def create_pie_chart(self):
        """Create a pie chart"""
        if not self.data:
            messagebox.showwarning("No Data", "Please load data first!")
            return
        
        self.clear_plot()
        
        if 'categories' in self.data and 'values' in self.data:
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
            wedges, texts, autotexts = self.ax.pie(self.data['values'], labels=self.data['categories'], 
                                                  autopct='%1.1f%%', colors=colors, startangle=90)
            self.ax.set_title('Pie Chart', fontsize=16, fontweight='bold')
        else:
            # Use first numeric column
            numeric_cols = [(k, v) for k, v in self.data.items() if isinstance(v[0], (int, float))]
            if numeric_cols:
                values = numeric_cols[0][1][:8]  # Limit to 8 slices
                labels = [f'Item {i+1}' for i in range(len(values))]
                self.ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
                self.ax.set_title(f'Pie Chart - {numeric_cols[0][0]}', fontsize=16, fontweight='bold')
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def create_scatter_plot(self):
        """Create a scatter plot"""
        if not self.data:
            messagebox.showwarning("No Data", "Please load data first!")
            return
        
        self.clear_plot()
        
        if 'x_data' in self.data and 'y_data' in self.data:
            self.ax.scatter(self.data['x_data'], self.data['y_data'], 
                           c='#FF6B6B', alpha=0.6, s=50)
            self.ax.set_title('Scatter Plot', fontsize=16, fontweight='bold')
            self.ax.set_xlabel('X Values')
            self.ax.set_ylabel('Y Values')
            self.ax.grid(True, alpha=0.3)
        else:
            # Use first two numeric columns
            numeric_cols = [(k, v) for k, v in self.data.items() if isinstance(v[0], (int, float))]
            if len(numeric_cols) >= 2:
                x_vals = numeric_cols[0][1][:100]
                y_vals = numeric_cols[1][1][:100]
                self.ax.scatter(x_vals, y_vals, alpha=0.6, s=50)
                self.ax.set_title(f'Scatter: {numeric_cols[0][0]} vs {numeric_cols[1][0]}', 
                                fontsize=16, fontweight='bold')
                self.ax.set_xlabel(numeric_cols[0][0])
                self.ax.set_ylabel(numeric_cols[1][0])
                self.ax.grid(True, alpha=0.3)
            else:
                self.ax.text(0.5, 0.5, 'Need at least 2 numeric columns', 
                           ha='center', va='center', transform=self.ax.transAxes)
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def create_histogram(self):
        """Create a histogram"""
        if not self.data:
            messagebox.showwarning("No Data", "Please load data first!")
            return
        
        self.clear_plot()
        
        if 'random_data' in self.data:
            self.ax.hist(self.data['random_data'], bins=30, color='#4ECDC4', alpha=0.7, edgecolor='black')
            self.ax.set_title('Histogram - Random Data Distribution', fontsize=16, fontweight='bold')
            self.ax.set_xlabel('Value')
            self.ax.set_ylabel('Frequency')
            self.ax.grid(True, alpha=0.3)
        else:
            # Use first numeric column
            numeric_cols = [(k, v) for k, v in self.data.items() if isinstance(v[0], (int, float))]
            if numeric_cols:
                values = numeric_cols[0][1]
                self.ax.hist(values, bins=min(20, len(values)//5), alpha=0.7, edgecolor='black')
                self.ax.set_title(f'Histogram - {numeric_cols[0][0]}', fontsize=16, fontweight='bold')
                self.ax.set_xlabel(numeric_cols[0][0])
                self.ax.set_ylabel('Frequency')
                self.ax.grid(True, alpha=0.3)
        
        self.figure.tight_layout()
        self.canvas.draw()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizer(root)
    root.mainloop()
```

This comprehensive data visualization tool demonstrates:

**Canvas Integration**: The `FigureCanvasTkAgg` class embeds matplotlib plots directly in Tkinter windows, creating seamless integration between data visualization and GUI controls.

**Dynamic Chart Creation**: Users can switch between different chart types with the same data, showing how the same information can be presented in multiple ways.

**File I/O Integration**: The CSV loading functionality shows how to combine file dialogs with data processing, a common pattern in data analysis applications.

**Flexible Data Handling**: The application can work with both predefined sample data and user-loaded CSV files, automatically detecting numeric columns and adapting chart creation accordingly.

## Interactive Data Analysis Tool

Let's create a more advanced example that allows real-time data manipulation:

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class InteractiveAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Data Analyzer")
        self.root.geometry("1200x800")
        
        self.setup_gui()
        self.generate_sample_data()
    
    def setup_gui(self):
        """Create the interactive GUI"""
        # Left panel for controls
        left_panel = tk.Frame(self.root, width=300, bg="lightblue")
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        left_panel.pack_propagate(False)
        
        tk.Label(left_panel, text="Interactive Data Analyzer", 
                font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)
        
        # Data generation controls
        tk.Label(left_panel, text="Data Generation:", font=("Arial", 12, "bold"),
                bg="lightblue").pack(pady=(10, 5))
        
        # Number of points slider
        tk.Label(left_panel, text="Number of Points:", bg="lightblue").pack()
        self.points_var = tk.IntVar(value=100)
        self.points_scale = tk.Scale(left_panel, from_=50, to=500, orient=tk.HORIZONTAL,
                                   variable=self.points_var, command=self.update_data)
        self.points_scale.pack(pady=5)
        
        # Noise level slider
        tk.Label(left_panel, text="Noise Level:", bg="lightblue").pack()
        self.noise_var = tk.DoubleVar(value=0.5)
        self.noise_scale = tk.Scale(left_panel, from_=0.1, to=2.0, resolution=0.1,
                                  orient=tk.HORIZONTAL, variable=self.noise_var,
                                  command=self.update_data)
        self.noise_scale.pack(pady=5)
        
        # Function type selection
        tk.Label(left_panel, text="Function Type:", bg="lightblue").pack(pady=(10, 5))
        self.function_var = tk.StringVar(value="sine")
        functions = [("Sine Wave", "sine"), ("Cosine Wave", "cosine"), 
                    ("Linear", "linear"), ("Quadratic", "quadratic")]
        
        for text, value in functions:
            tk.Radiobutton(left_panel, text=text, variable=self.function_var,
                          value=value, bg="lightblue", command=self.update_data).pack(anchor=tk.W)
        
        # Analysis controls
        tk.Label(left_panel, text="Analysis Tools:", font=("Arial", 12, "bold"),
                bg="lightblue").pack(pady=(20, 5))
        
        tk.Button(left_panel, text="Show Statistics", command=self.show_statistics,
                 bg="green", fg="white", width=20).pack(pady=3)
        tk.Button(left_panel, text="Fit Trend Line", command=self.fit_trend_line,
                 bg="orange", fg="white", width=20).pack(pady=3)
        tk.Button(left_panel, text="Show Moving Average", command=self.show_moving_average,
                 bg="purple", fg="white", width=20).pack(pady=3)
        tk.Button(left_panel, text="Reset View", command=self.reset_view,
                 bg="red", fg="white", width=20).pack(pady=3)
        
        # Statistics display
        self.stats_frame = tk.Frame(left_panel, bg="white", relief=tk.SUNKEN, bd=1)
        self.stats_frame.pack(fill=tk.X, padx=5, pady=10)
        
        self.stats_text = tk.Text(self.stats_frame, height=8, width=30, font=("Courier", 9))
        self.stats_text.pack(padx=5, pady=5)
        
        # Right panel for plot
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create matplotlib figure
        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.figure, self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Add toolbar for zoom/pan
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        self.toolbar.update()
    
    def generate_sample_data(self):
        """Generate sample data based on current settings"""
        n_points = self.points_var.get()
        noise_level = self.noise_var.get()
        func_type = self.function_var.get()
        
        self.x_data = np.linspace(0, 4*np.pi, n_points)
        
        if func_type == "sine":
            self.y_data = np.sin(self.x_data) + np.random.normal(0, noise_level, n_points)
        elif func_type == "cosine":
            self.y_data = np.cos(self.x_data) + np.random.normal(0, noise_level, n_points)
        elif func_type == "linear":
            self.y_data = 0.5 * self.x_data + np.random.normal(0, noise_level, n_points)
        elif func_type == "quadratic":
            self.y_data = 0.1 * self.x_data**2 + np.random.normal(0, noise_level, n_points)
        
        self.plot_basic_data()
    
    def update_data(self, event=None):
        """Update data when sliders change"""
        self.generate_sample_data()
    
    def plot_basic_data(self):
        """Plot the basic data points"""
        self.ax.clear()
        self.ax.scatter(self.x_data, self.y_data, alpha=0.6, c='blue', s=20)
        self.ax.set_title(f'{self.function_var.get().title()} Function with Noise', 
                         fontsize=14, fontweight='bold')
        self.ax.set_xlabel('X Values')
        self.ax.set_ylabel('Y Values')
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()
    
    def show_statistics(self):
        """Calculate and display statistics"""
        mean_x = np.mean(self.x_data)
        mean_y = np.mean(self.y_data)
        std_x = np.std(self.x_data)
        std_y = np.std(self.y_data)
        correlation = np.corrcoef(self.x_data, self.y_data)[0, 1]
        
        stats_text = f"""Data Statistics:
        
Points: {len(self.x_data)}
        
X Statistics:
Mean: {mean_x:.3f}
Std Dev: {std_x:.3f}
Min: {np.min(self.x_data):.3f}
Max: {np.max(self.x_data):.3f}

Y Statistics:
Mean: {mean_y:.3f}
Std Dev: {std_y:.3f}
Min: {np.min(self.y_data):.3f}
Max: {np.max(self.y_data):.3f}

Correlation: {correlation:.3f}
"""
        
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, stats_text)
    
    def fit_trend_line(self):
        """Fit and display a trend line"""
        # Fit a polynomial (degree 1 for linear trend)
        coefficients = np.polyfit(self.x_data, self.y_data, 1)
        trend_line = np.polyval(coefficients, self.x_data)
        
        self.plot_basic_data()
        self.ax.plot(self.x_data, trend_line, 'r-', linewidth=2, label=f'Trend: y = {coefficients[0]:.3f}x + {coefficients[1]:.3f}')
        self.ax.legend()
        self.canvas.draw()
    
    def show_moving_average(self):
        """Calculate and display moving average"""
        window_size = max(5, len(self.x_data) // 20)  # Adaptive window size
        
        # Calculate moving average
        moving_avg = np.convolve(self.y_data, np.ones(window_size)/window_size, mode='valid')
        moving_avg_x = self.x_data[window_size-1:]
        
        self.plot_basic_data()
        self.ax.plot(moving_avg_x, moving_avg, 'g-', linewidth=2, 
                    label=f'Moving Average (window={window_size})')
        self.ax.legend()
        self.canvas.draw()
    
    def reset_view(self):
        """Reset to basic data view"""
        self.plot_basic_data()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveAnalyzer(root)
    root.mainloop()
```

This interactive analyzer demonstrates:

**Real-time Updates**: Sliders and radio buttons update the plot immediately as users interact with them, showing the power of combining GUI controls with data visualization.

**Statistical Analysis**: The application calculates and displays relevant statistics, teaching users about data analysis concepts like correlation and standard deviation.

**Multiple Analysis Tools**: Users can apply different analysis techniques (trend lines, moving averages) to the same data, helping them understand how different approaches reveal different aspects of data patterns.

# Using Tkinter with the Drones

Combining Tkinter with drone control creates powerful applications for aerial robotics. We can build control panels that provide both manual drone control and real-time camera feedback, making drone operation more intuitive and safer.

## Basic Drone Control Panel

Let's start with a simple control panel that provides basic drone movements and camera display:

```python
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import threading
import time

# Note: You'll need to install droneblocks for this to work
# pip install droneblocks

try:
    from droneblocks.DroneBlocksTello import DroneBlocksTello
    DRONE_AVAILABLE = True
except ImportError:
    DRONE_AVAILABLE = False
    print("DroneBlocks not available - running in simulation mode")

class DroneControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Control Panel")
        self.root.geometry("1000x700")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.drone = None
        self.camera_running = False
        self.camera_thread = None
        self.current_frame = None
        
        self.setup_gui()
        
        if DRONE_AVAILABLE:
            self.connect_drone()
    
    def setup_gui(self):
        """Create the drone control interface"""
        # Main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel for controls
        control_frame = tk.Frame(main_frame, width=300, bg="lightgray")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        control_frame.pack_propagate(False)
        
        # Connection status
        self.status_var = tk.StringVar()
        self.status_var.set("Disconnected" if not DRONE_AVAILABLE else "Connecting...")
        status_label = tk.Label(control_frame, textvariable=self.status_var, 
                               font=("Arial", 12, "bold"), bg="lightgray")
        status_label.pack(pady=10)
        
        # Battery display
        self.battery_var = tk.StringVar()
        self.battery_var.set("Battery: --")
        battery_label = tk.Label(control_frame, textvariable=self.battery_var,
                                font=("Arial", 11), bg="lightgray")
        battery_label.pack(pady=5)
        
        # Flight controls
        tk.Label(control_frame, text="Flight Controls", font=("Arial", 14, "bold"),
                bg="lightgray").pack(pady=(20, 10))
        
        # Takeoff/Land buttons
        flight_frame = tk.Frame(control_frame, bg="lightgray")
        flight_frame.pack(pady=10)
        
        self.takeoff_btn = tk.Button(flight_frame, text="TAKEOFF", command=self.takeoff,
                                    bg="green", fg="white", font=("Arial", 12, "bold"),
                                    width=10, height=2)
        self.takeoff_btn.pack(side=tk.LEFT, padx=5)
        
        self.land_btn = tk.Button(flight_frame, text="LAND", command=self.land,
                                 bg="red", fg="white", font=("Arial", 12, "bold"),
                                 width=10, height=2)
        self.land_btn.pack(side=tk.LEFT, padx=5)
        
        # Movement controls
        tk.Label(control_frame, text="Movement Controls", font=("Arial", 12, "bold"),
                bg="lightgray").pack(pady=(20, 10))
        
        # Create movement button grid
        move_frame = tk.Frame(control_frame, bg="lightgray")
        move_frame.pack(pady=10)
        
        # Forward/Back/Left/Right buttons in cross pattern
        tk.Button(move_frame, text="↑\nFORWARD", command=lambda: self.move_drone("forward"),
                 width=8, height=2).grid(row=0, column=1, padx=2, pady=2)
        
        tk.Button(move_frame, text="←\nLEFT", command=lambda: self.move_drone("left"),
                 width=8, height=2).grid(row=1, column=0, padx=2, pady=2)
        
        tk.Button(move_frame, text="→\nRIGHT", command=lambda: self.move_drone("right"),
                 width=8, height=2).grid(row=1, column=2, padx=2, pady=2)
        
        tk.Button(move_frame, text="↓\nBACK", command=lambda: self.move_drone("back"),
                 width=8, height=2).grid(row=2, column=1, padx=2, pady=2)
        
        # Up/Down controls
        vertical_frame = tk.Frame(control_frame, bg="lightgray")
        vertical_frame.pack(pady=10)
        
        tk.Button(vertical_frame, text="↑ UP", command=lambda: self.move_drone("up"),
                 bg="lightblue", width=8, height=2).pack(side=tk.LEFT, padx=5)
        tk.Button(vertical_frame, text="↓ DOWN", command=lambda: self.move_drone("down"),
                 bg="lightcoral", width=8, height=2).pack(side=tk.LEFT, padx=5)
        
        # Rotation controls
        rotation_frame = tk.Frame(control_frame, bg="lightgray")
        rotation_frame.pack(pady=10)
        
        tk.Button(rotation_frame, text="↺ CCW", command=lambda: self.move_drone("ccw"),
                 bg="yellow", width=8, height=2).pack(side=tk.LEFT, padx=5)
        tk.Button(rotation_frame, text="↻ CW", command=lambda: self.move_drone("cw"),
                 bg="orange", width=8, height=2).pack(side=tk.LEFT, padx=5)
        
        # Camera controls
        tk.Label(control_frame, text="Camera Controls", font=("Arial", 12, "bold"),
                bg="lightgray").pack(pady=(20, 10))
        
        self.camera_btn = tk.Button(control_frame, text="Start Camera", 
                                   command=self.toggle_camera, bg="blue", fg="white",
                                   width=20, height=2)
        self.camera_btn.pack(pady=10)
        
        # Emergency stop
        tk.Button(control_frame, text="EMERGENCY STOP", command=self.emergency_stop,
                 bg="darkred", fg="white", font=("Arial", 12, "bold"),
                 width=20, height=2).pack(pady=20)
        
        # Right panel for camera feed
        self.camera_frame = tk.Frame(main_frame, bg="black")
        self.camera_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.camera_label = tk.Label(self.camera_frame, text="Camera Feed\n(Start camera to view)",
                                    bg="black", fg="white", font=("Arial", 16))
        self.camera_label.pack(expand=True)
    
    def connect_drone(self):
        """Connect to the drone"""
        if not DRONE_AVAILABLE:
            self.status_var.set("Drone library not available")
            return
        
        try:
            self.drone = DroneBlocksTello()
            self.drone.connect(True)
            
            # Get battery level
            battery = self.drone.get_battery()
            self.battery_var.set(f"Battery: {battery}%")
            self.status_var.set("Connected")
            
            # Update battery every 30 seconds
            self.root.after(30000, self.update_battery)
            
        except Exception as e:
            self.status_var.set("Connection Failed")
            messagebox.showerror("Connection Error", f"Failed to connect to drone: {str(e)}")
    
    def update_battery(self):
        """Update battery level periodically"""
        if self.drone and DRONE_AVAILABLE:
            try:
                battery = self.drone.get_battery()
                self.battery_var.set(f"Battery: {battery}%")
                
                # Schedule next update
                self.root.after(30000, self.update_battery)
            except:
                self.battery_var.set("Battery: Error")
    
    def takeoff(self):
        """Make the drone take off"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.takeoff()
                messagebox.showinfo("Takeoff", "Drone taking off!")
            except Exception as e:
                messagebox.showerror("Takeoff Error", f"Failed to takeoff: {str(e)}")
        else:
            messagebox.showinfo("Simulation", "Takeoff command sent (simulation mode)")
    
    def land(self):
        """Make the drone land"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.land()
                messagebox.showinfo("Landing", "Drone landing!")
            except Exception as e:
                messagebox.showerror("Landing Error", f"Failed to land: {str(e)}")
        else:
            messagebox.showinfo("Simulation", "Land command sent (simulation mode)")
    
    def move_drone(self, direction):
        """Move the drone in the specified direction"""
        if self.drone and DRONE_AVAILABLE:
            try:
                distance = 30  # Move 30cm each time
                
                if direction == "forward":
                    self.drone.move_forward(distance)
                elif direction == "back":
                    self.drone.move_back(distance)
                elif direction == "left":
                    self.drone.move_left(distance)
                elif direction == "right":
                    self.drone.move_right(distance)
                elif direction == "up":
                    self.drone.move_up(distance)
                elif direction == "down":
                    self.drone.move_down(distance)
                elif direction == "cw":
                    self.drone.rotate_clockwise(45)  # 45 degree rotation
                elif direction == "ccw":
                    self.drone.rotate_counter_clockwise(45)
                    
            except Exception as e:
                messagebox.showerror("Movement Error", f"Failed to move {direction}: {str(e)}")
        else:
            print(f"Simulation: Moving {direction}")
    
    def toggle_camera(self):
        """Start or stop the camera feed"""
        if not self.camera_running:
            self.start_camera()
        else:
            self.stop_camera()
    
    def start_camera(self):
        """Start the camera feed"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.streamon()
                self.camera_running = True
                self.camera_btn.config(text="Stop Camera", bg="red")
                
                # Start camera thread
                self.camera_thread = threading.Thread(target=self.camera_loop, daemon=True)
                self.camera_thread.start()
                
            except Exception as e:
                messagebox.showerror("Camera Error", f"Failed to start camera: {str(e)}")
        else:
            # Simulation mode - show placeholder
            self.camera_running = True
            self.camera_btn.config(text="Stop Camera", bg="red")
            self.camera_label.config(text="Camera Active\n(Simulation Mode)")
    
    def camera_loop(self):
        """Main camera loop running in separate thread"""
        while self.camera_running and self.drone and DRONE_AVAILABLE:
            try:
                # Get frame from drone
                frame = self.drone.get_frame_read().frame
                
                if frame is not None:
                    # Resize frame for display
                    frame = cv2.resize(frame, (640, 480))
                    
                    # Convert BGR to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    # Convert to PIL Image
                    pil_image = Image.fromarray(frame_rgb)
                    photo = ImageTk.PhotoImage(pil_image)
                    
                    # Update GUI in main thread
                    self.root.after(0, self.update_camera_display, photo)
                    
                time.sleep(0.03)  # ~30 FPS
                
            except Exception as e:
                print(f"Camera error: {e}")
                break
    
    def update_camera_display(self, photo):
        """Update the camera display (called from main thread)"""
        if self.camera_running:
            self.camera_label.config(image=photo, text="")
            self.camera_label.image = photo  # Keep reference
    
    def stop_camera(self):
        """Stop the camera feed"""
        self.camera_running = False
        self.camera_btn.config(text="Start Camera", bg="blue")
        
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.streamoff()
            except:
                pass
        
        # Reset camera display
        self.camera_label.config(image="", text="Camera Feed\n(Start camera to view)")
        self.camera_label.image = None
    
    def emergency_stop(self):
        """Emergency stop - land immediately"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.emergency()
                messagebox.showwarning("Emergency Stop", "Emergency stop activated!")
            except Exception as e:
                messagebox.showerror("Emergency Error", f"Emergency stop failed: {str(e)}")
        else:
            messagebox.showwarning("Simulation", "Emergency stop activated (simulation mode)")
    
    def on_closing(self):
        """Handle window closing"""
        if self.camera_running:
            self.stop_camera()
        
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.land()  # Safety landing
                time.sleep(1)
            except:
                pass
        
        self.root.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DroneControlPanel(root)
    root.mainloop()
```

This drone control panel provides:

**Safety Features**: Emergency stop button and automatic landing when the application closes, ensuring safe drone operation.

**Real-time Camera**: Live video feed from the drone's camera, displayed directly in the GUI using threading to prevent interface freezing.

**Intuitive Controls**: Button layout that matches natural movement directions, making it easy for users to control the drone.

**Status Monitoring**: Battery level and connection status display, helping users monitor drone health.

## Advanced Drone Control with Computer Vision

Let's create a more advanced application that combines drone control with computer vision analysis:

```python
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import cv2
from PIL import Image, ImageTk
import threading
import time
import numpy as np

# Drone library (install with pip install droneblocks)
try:
    from droneblocks.DroneBlocksTello import DroneBlocksTello
    DRONE_AVAILABLE = True
except ImportError:
    DRONE_AVAILABLE = False

class AdvancedDroneInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Drone Control with Computer Vision")
        self.root.geometry("1400x900")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.drone = None
        self.camera_running = False
        self.camera_thread = None
        self.current_frame = None
        self.processed_frame = None
        
        # Computer vision settings
        self.cv_enabled = tk.BooleanVar()
        self.cv_mode = tk.StringVar(value="original")
        self.color_detection_enabled = tk.BooleanVar()
        
        # Color detection parameters (HSV values)
        self.hue_min = tk.IntVar(value=100)
        self.hue_max = tk.IntVar(value=130)
        self.sat_min = tk.IntVar(value=50)
        self.sat_max = tk.IntVar(value=255)
        self.val_min = tk.IntVar(value=50)
        self.val_max = tk.IntVar(value=255)
        
        self.setup_gui()
        
        if DRONE_AVAILABLE:
            self.connect_drone()
    
    def setup_gui(self):
        """Create the advanced interface"""
        # Create notebook for tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab 1: Drone Control
        self.control_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.control_tab, text="Drone Control")
        self.setup_control_tab()
        
        # Tab 2: Computer Vision
        self.vision_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.vision_tab, text="Computer Vision")
        self.setup_vision_tab()
        
        # Tab 3: Data Analysis
        self.analysis_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_tab, text="Flight Data")
        self.setup_analysis_tab()
    
    def setup_control_tab(self):
        """Setup the drone control interface"""
        # Left panel - controls
        control_frame = tk.Frame(self.control_tab, width=350, bg="lightgray")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        control_frame.pack_propagate(False)
        
        # Status section
        tk.Label(control_frame, text="Drone Status", font=("Arial", 14, "bold"),
                bg="lightgray").pack(pady=10)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Disconnected" if not DRONE_AVAILABLE else "Connecting...")
        tk.Label(control_frame, textvariable=self.status_var, font=("Arial", 12),
                bg="lightgray").pack()
        
        self.battery_var = tk.StringVar(value="Battery: --")
        tk.Label(control_frame, textvariable=self.battery_var, font=("Arial", 11),
                bg="lightgray").pack(pady=5)
        
        # Flight controls
        flight_frame = tk.LabelFrame(control_frame, text="Flight Controls", 
                                   font=("Arial", 12, "bold"), bg="lightgray")
        flight_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Main flight buttons
        button_frame = tk.Frame(flight_frame, bg="lightgray")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="TAKEOFF", command=self.takeoff,
                 bg="green", fg="white", font=("Arial", 11, "bold"),
                 width=12, height=2).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="LAND", command=self.land,
                 bg="red", fg="white", font=("Arial", 11, "bold"),
                 width=12, height=2).pack(side=tk.LEFT, padx=5)
        
        # Movement controls in a grid
        move_frame = tk.LabelFrame(control_frame, text="Movement", 
                                 font=("Arial", 12, "bold"), bg="lightgray")
        move_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Create movement grid
        grid_frame = tk.Frame(move_frame, bg="lightgray")
        grid_frame.pack(pady=10)
        
        # Movement buttons with improved layout
        movements = [
            ("↑", "forward", 0, 1),
            ("←", "left", 1, 0),
            ("•", "stop", 1, 1),  # Center stop button
            ("→", "right", 1, 2),
            ("↓", "back", 2, 1)
        ]
        
        for symbol, direction, row, col in movements:
            if direction == "stop":
                btn = tk.Button(grid_frame, text=symbol, command=self.stop_movement,
                               bg="gray", fg="white", width=4, height=2)
            else:
                btn = tk.Button(grid_frame, text=symbol, 
                               command=lambda d=direction: self.move_drone(d),
                               width=4, height=2)
            btn.grid(row=row, column=col, padx=2, pady=2)
        
        # Vertical controls
        vertical_frame = tk.Frame(move_frame, bg="lightgray")
        vertical_frame.pack(pady=5)
        
        tk.Button(vertical_frame, text="↑ UP", command=lambda: self.move_drone("up"),
                 bg="lightblue", width=8).pack(side=tk.LEFT, padx=5)
        tk.Button(vertical_frame, text="↓ DOWN", command=lambda: self.move_drone("down"),
                 bg="lightcoral", width=8).pack(side=tk.LEFT, padx=5)
        
        # Camera controls
        camera_frame = tk.LabelFrame(control_frame, text="Camera", 
                                   font=("Arial", 12, "bold"), bg="lightgray")
        camera_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.camera_btn = tk.Button(camera_frame, text="Start Camera", 
                                   command=self.toggle_camera, bg="blue", fg="white",
                                   width=25, height=2)
        self.camera_btn.pack(pady=10)
        
        tk.Button(camera_frame, text="Capture Image", command=self.capture_image,
                 bg="purple", fg="white", width=25).pack(pady=5)
        
        # Emergency stop
        tk.Button(control_frame, text="EMERGENCY STOP", command=self.emergency_stop,
                 bg="darkred", fg="white", font=("Arial", 12, "bold"),
                 width=25, height=3).pack(pady=20)
        
        # Right panel - camera feed
        self.camera_frame = tk.Frame(self.control_tab, bg="black")
        self.camera_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.camera_label = tk.Label(self.camera_frame, text="Camera Feed\n(Start camera to view)",
                                    bg="black", fg="white", font=("Arial", 18))
        self.camera_label.pack(expand=True)
    
    def setup_vision_tab(self):
        """Setup the computer vision analysis tab"""
        # Left panel - CV controls
        cv_control_frame = tk.Frame(self.vision_tab, width=400, bg="lightyellow")
        cv_control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        cv_control_frame.pack_propagate(False)
        
        tk.Label(cv_control_frame, text="Computer Vision Controls", 
                font=("Arial", 14, "bold"), bg="lightyellow").pack(pady=10)
        
        # CV mode selection
        mode_frame = tk.LabelFrame(cv_control_frame, text="Processing Mode", 
                                 font=("Arial", 12, "bold"), bg="lightyellow")
        mode_frame.pack(fill=tk.X, padx=10, pady=10)
        
        modes = [
            ("Original", "original"),
            ("Grayscale", "grayscale"),
            ("Edge Detection", "edges"),
            ("Blur", "blur"),
            ("Color Detection", "color")
        ]
        
        for text, value in modes:
            tk.Radiobutton(mode_frame, text=text, variable=self.cv_mode,
                          value=value, bg="lightyellow", 
                          command=self.update_cv_mode).pack(anchor=tk.W)
        
        # Color detection controls
        color_frame = tk.LabelFrame(cv_control_frame, text="Color Detection Settings", 
                                  font=("Arial", 12, "bold"), bg="lightyellow")
        color_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # HSV sliders
        self.create_hsv_slider(color_frame, "Hue Min", self.hue_min, 0, 179)
        self.create_hsv_slider(color_frame, "Hue Max", self.hue_max, 0, 179)
        self.create_hsv_slider(color_frame, "Sat Min", self.sat_min, 0, 255)
        self.create_hsv_slider(color_frame, "Sat Max", self.sat_max, 0, 255)
        self.create_hsv_slider(color_frame, "Val Min", self.val_min, 0, 255)
        self.create_hsv_slider(color_frame, "Val Max", self.val_max, 0, 255)
        
        # Preset color buttons
        preset_frame = tk.Frame(color_frame, bg="lightyellow")
        preset_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(preset_frame, text="Color Presets:", bg="lightyellow").pack()
        
        presets = [
            ("Blue", (100, 130, 50, 255, 50, 255)),
            ("Red", (0, 10, 120, 255, 70, 255)),
            ("Green", (40, 80, 50, 255, 50, 255)),
            ("Yellow", (20, 30, 100, 255, 100, 255))
        ]
        
        preset_btn_frame = tk.Frame(preset_frame, bg="lightyellow")
        preset_btn_frame.pack()
        
        for color_name, (h_min, h_max, s_min, s_max, v_min, v_max) in presets:
            tk.Button(preset_btn_frame, text=color_name, 
                     command=lambda p=(h_min, h_max, s_min, s_max, v_min, v_max): self.set_color_preset(p),
                     width=8).pack(side=tk.LEFT, padx=2)
        
        # Analysis results
        results_frame = tk.LabelFrame(cv_control_frame, text="Analysis Results", 
                                    font=("Arial", 12, "bold"), bg="lightyellow")
        results_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.results_text = tk.Text(results_frame, height=10, width=40, font=("Courier", 9))
        self.results_text.pack(padx=5, pady=5)
        
        # Right panel - processed image display
        self.vision_display_frame = tk.Frame(self.vision_tab, bg="black")
        self.vision_display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.vision_label = tk.Label(self.vision_display_frame, 
                                   text="Computer Vision Display\n(Start camera for live analysis)",
                                   bg="black", fg="white", font=("Arial", 16))
        self.vision_label.pack(expand=True)
    
    def setup_analysis_tab(self):
        """Setup the flight data analysis tab"""
        # This would contain flight data logging and analysis
        analysis_frame = tk.Frame(self.analysis_tab, bg="lightgreen")
        analysis_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(analysis_frame, text="Flight Data Analysis", 
                font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=20)
        
        tk.Label(analysis_frame, 
                text="This section would contain:\n\n" +
                     "• Flight path tracking\n" +
                     "• Battery usage analysis\n" +
                     "• Movement pattern visualization\n" +
                     "• Performance metrics\n" +
                     "• Data export functionality",
                font=("Arial", 12), bg="lightgreen", justify=tk.LEFT).pack(pady=20)
    
    def create_hsv_slider(self, parent, label, variable, min_val, max_val):
        """Create an HSV adjustment slider"""
        frame = tk.Frame(parent, bg="lightyellow")
        frame.pack(fill=tk.X, pady=2)
        
        tk.Label(frame, text=f"{label}:", bg="lightyellow", width=8).pack(side=tk.LEFT)
        scale = tk.Scale(frame, from_=min_val, to=max_val, orient=tk.HORIZONTAL,
                        variable=variable, command=self.update_color_detection)
        scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        value_label = tk.Label(frame, textvariable=variable, bg="lightyellow", width=4)
        value_label.pack(side=tk.RIGHT)
    
    def set_color_preset(self, preset_values):
        """Set HSV values to a color preset"""
        h_min, h_max, s_min, s_max, v_min, v_max = preset_values
        
        self.hue_min.set(h_min)
        self.hue_max.set(h_max)
        self.sat_min.set(s_min)
        self.sat_max.set(s_max)
        self.val_min.set(v_min)
        self.val_max.set(v_max)
    
    def update_cv_mode(self):
        """Update computer vision processing mode"""
        pass  # Processing happens in camera loop
    
    def update_color_detection(self, event=None):
        """Update color detection parameters"""
        pass  # Updates happen in camera loop
    
    def connect_drone(self):
        """Connect to the drone"""
        if not DRONE_AVAILABLE:
            print("Drone Lib Unavailable!")
            self.status_var.set("Drone library not available")
            return
        
        try:
            print("Attempting connection!")
            self.drone = DroneBlocksTello()
            self.drone.connect(True)
            
            battery = self.drone.get_battery()
            self.battery_var.set(f"Battery: {battery}%")
            self.status_var.set("Connected")
            
            self.root.after(30000, self.update_battery)
            
        except Exception as e:
            self.status_var.set("Connection Failed")
            messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
    
    def update_battery(self):
        """Update battery level"""
        if self.drone and DRONE_AVAILABLE:
            try:
                battery = self.drone.get_battery()
                self.battery_var.set(f"Battery: {battery}%")
                self.root.after(30000, self.update_battery)
            except:
                self.battery_var.set("Battery: Error")
    
    def takeoff(self):
        """Drone takeoff"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.takeoff()
                messagebox.showinfo("Takeoff", "Drone taking off!")
            except Exception as e:
                messagebox.showerror("Error", f"Takeoff failed: {str(e)}")
        else:
            messagebox.showinfo("Simulation", "Takeoff (simulation)")
    
    def land(self):
        """Drone landing"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.land()
                messagebox.showinfo("Landing", "Drone landing!")
            except Exception as e:
                messagebox.showerror("Error", f"Landing failed: {str(e)}")
        else:
            messagebox.showinfo("Simulation", "Landing (simulation)")
    
    def move_drone(self, direction):
        """Move drone in specified direction"""
        if self.drone and DRONE_AVAILABLE:
            try:
                distance = 30
                
                if direction == "forward":
                    self.drone.move_forward(distance)
                elif direction == "back":
                    self.drone.move_back(distance)
                elif direction == "left":
                    self.drone.move_left(distance)
                elif direction == "right":
                    self.drone.move_right(distance)
                elif direction == "up":
                    self.drone.move_up(distance)
                elif direction == "down":
                    self.drone.move_down(distance)
                    
            except Exception as e:
                messagebox.showerror("Movement Error", f"Failed to move {direction}: {str(e)}")
        else:
            print(f"Simulation: Moving {direction}")
    
    def stop_movement(self):
        """Stop all drone movement"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.send_rc_control(0, 0, 0, 0)  # Stop all movement
            except Exception as e:
                messagebox.showerror("Stop Error", f"Failed to stop: {str(e)}")
        else:
            print("Simulation: Stop movement")
    
    def emergency_stop(self):
        """Emergency stop"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.emergency()
                messagebox.showwarning("Emergency", "Emergency stop activated!")
            except Exception as e:
                messagebox.showerror("Emergency Error", f"Emergency failed: {str(e)}")
        else:
            messagebox.showwarning("Simulation", "Emergency stop (simulation)")
    
    def toggle_camera(self):
        """Start or stop camera"""
        if not self.camera_running:
            self.start_camera()
        else:
            self.stop_camera()
    
    def start_camera(self):
        """Start camera feed"""
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.streamon()
                self.camera_running = True
                self.camera_btn.config(text="Stop Camera", bg="red")
                
                self.camera_thread = threading.Thread(target=self.camera_loop, daemon=True)
                self.camera_thread.start()
                
            except Exception as e:
                messagebox.showerror("Camera Error", f"Failed to start camera: {str(e)}")
        else:
            # Simulation mode
            self.camera_running = True
            self.camera_btn.config(text="Stop Camera", bg="red")
            self.camera_label.config(text="Camera Active\n(Simulation Mode)")
            self.vision_label.config(text="CV Analysis Active\n(Simulation Mode)")
    
    def camera_loop(self):
        """Main camera processing loop"""
        while self.camera_running and self.drone and DRONE_AVAILABLE:
            try:
                frame = self.drone.get_frame_read().frame
                
                if frame is not None:
                    # Resize for processing
                    frame = cv2.resize(frame, (640, 480))
                    self.current_frame = frame.copy()
                    
                    # Apply computer vision processing
                    processed_frame = self.process_frame(frame)
                    
                    # Convert for display
                    display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    processed_display = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB) if len(processed_frame.shape) == 3 else cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2RGB)
                    
                    # Update displays
                    self.root.after(0, self.update_camera_displays, display_frame, processed_display)
                    
                time.sleep(0.03)  # ~30 FPS
                
            except Exception as e:
                print(f"Camera error: {e}")
                break
    
    def process_frame(self, frame):
        """Process frame based on selected CV mode"""
        mode = self.cv_mode.get()
        
        if mode == "original":
            return frame
        elif mode == "grayscale":
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif mode == "edges":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.Canny(gray, 100, 200)
        elif mode == "blur":
            return cv2.GaussianBlur(frame, (15, 15), 0)
        elif mode == "color":
            return self.detect_color(frame)
        
        return frame
    
    def detect_color(self, frame):
        """Detect specified color in frame"""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Get HSV range from sliders
        lower = np.array([self.hue_min.get(), self.sat_min.get(), self.val_min.get()])
        upper = np.array([self.hue_max.get(), self.sat_max.get(), self.val_max.get()])
        
        # Create mask
        mask = cv2.inRange(hsv, lower, upper)
        
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours on original frame
        result = frame.copy()
        cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
        
        # Calculate total area
        total_area = sum(cv2.contourArea(contour) for contour in contours)
        
        # Update analysis results
        self.root.after(0, self.update_analysis_results, len(contours), total_area)
        
        return result
    
    def update_analysis_results(self, contour_count, total_area):
        """Update the analysis results display"""
        results = f"""Color Detection Analysis:

Contours Found: {contour_count}
Total Area: {total_area:.0f} pixels

HSV Range:
Hue: {self.hue_min.get()} - {self.hue_max.get()}
Saturation: {self.sat_min.get()} - {self.sat_max.get()}
Value: {self.val_min.get()} - {self.val_max.get()}

Detection Quality: {"Good" if total_area > 1000 else "Poor"}
"""
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, results)
    
    def update_camera_displays(self, original_frame, processed_frame):
        """Update both camera displays"""
        if self.camera_running:
            # Update main camera display
            pil_original = Image.fromarray(original_frame)
            photo_original = ImageTk.PhotoImage(pil_original)
            self.camera_label.config(image=photo_original, text="")
            self.camera_label.image = photo_original
            
            # Update computer vision display
            pil_processed = Image.fromarray(processed_frame)
            photo_processed = ImageTk.PhotoImage(pil_processed)
            self.vision_label.config(image=photo_processed, text="")
            self.vision_label.image = photo_processed
    
    def capture_image(self):
        """Capture and save current frame"""
        if self.current_frame is not None:
            filename = filedialog.asksaveasfilename(
                title="Save Image",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
            )
            
            if filename:
                cv2.imwrite(filename, self.current_frame)
                messagebox.showinfo("Image Saved", f"Image saved as {filename}")
        else:
            messagebox.showwarning("No Image", "No image to capture!")
    
    def stop_camera(self):
        """Stop camera feed"""
        self.camera_running = False
        self.camera_btn.config(text="Start Camera", bg="blue")
        
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.streamoff()
            except:
                pass
        
        # Reset displays
        self.camera_label.config(image="", text="Camera Feed\n(Start camera to view)")
        self.camera_label.image = None
        self.vision_label.config(image="", text="Computer Vision Display\n(Start camera for live analysis)")
        self.vision_label.image = None
    
    def on_closing(self):
        """Handle application closing"""
        if self.camera_running:
            self.stop_camera()
        
        if self.drone and DRONE_AVAILABLE:
            try:
                self.drone.land()
                time.sleep(1)
            except:
                pass
        
        self.root.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedDroneInterface(root)
    root.mainloop()
```

This advanced drone interface demonstrates:

**Tabbed Interface**: Using `ttk.Notebook` to organize different functionalities into separate tabs, making the interface cleaner and more organized.

**Real-time Computer Vision**: Live processing of drone camera feed with multiple analysis modes including edge detection, color detection, and custom HSV filtering.

**Interactive Controls**: Sliders and controls for adjusting computer vision parameters in real-time, allowing users to tune detection algorithms on the fly.

**Safety Integration**: Proper shutdown procedures that ensure the drone lands safely when the application closes.

**Data Analysis Framework**: Structure for collecting and analyzing flight data, which could be extended to include flight path tracking, performance metrics, and data export capabilities.

The combination of Tkinter with drone control and computer vision creates powerful applications for educational robotics, research, and practical drone applications. Students can use these tools to explore concepts in robotics, computer vision, and human-computer interaction while working with real hardware.

This tutorial progression from basic GUI applications to advanced drone control systems demonstrates how Tkinter can scale from simple desktop applications to complex, multi-threaded applications that integrate with external hardware and advanced computer vision algorithms.
