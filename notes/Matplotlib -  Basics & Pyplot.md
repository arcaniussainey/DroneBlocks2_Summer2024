# MatPlotLib Data Visualization Tutorial for Python 3.13

## Visualizing Battery Life Over Time

Before we dive into what MatPlotLib is, let's start with an example that shows why data visualization is so powerful. Imagine you're tracking your phone's battery life throughout the day. You could just look at a list of numbers, but a graph makes patterns immediately obvious.

```python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Sample battery data - imagine this came from monitoring a device
# Time in hours since midnight
time_hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# Battery percentage at each time
battery_percent = [100, 95, 88, 82, 75, 65, 58, 45, 38, 25, 18, 12, 8, 5, 2]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_hours, battery_percent, 'b-o', linewidth=2, markersize=6)
plt.title('Phone Battery Life Throughout the Day', fontsize=16)
plt.xlabel('Time (24-hour format)', fontsize=12)
plt.ylabel('Battery Percentage (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim(0, 100)

# Add some annotations to highlight interesting points
plt.annotate('Lunch break - less usage', 
             xy=(12, 75), xytext=(10, 85),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, color='red')

plt.annotate('Heavy usage period', 
             xy=(16, 38), xytext=(17.5, 50),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, color='red')

plt.tight_layout()
plt.show()

print("Notice how the graph immediately shows:")
print("- Steady battery drain during normal use")
print("- Slower drain during lunch (less usage)")
print("- Faster drain in the afternoon (heavy usage)")
print("- Critical battery levels after 8 PM")
```

This single graph tells a story that would be hard to see in a table of numbers. That's the power of data visualization! (Note that the data isn't really super meaningful, I mainly wanted to show off it having annotation and visualization)

## What is MatPlotLib?

MatPlotLib is Python's most popular library for creating graphs, charts, and visualizations. Think of it as a digital graphing calculator that can create publication-quality figures. The name comes from "MATLAB plotting library" - it was originally designed to provide MATLAB-like plotting capabilities in Python.

MatPlotLib can create virtually any type of 2D plot you can imagine: line graphs, bar charts, scatter plots, histograms, pie charts, and much more. It's used everywhere from scientific research to business analytics to data journalism.

The library has two main interfaces:
1. **pyplot** - Similar to MATLAB, good for simple plots and interactive use
2. **Object-oriented interface** - More powerful and flexible for complex applications

For learning, we'll focus on pyplot since it's more intuitive for beginners.

## Why Would We Use It?

Data visualization serves several crucial purposes that make it indispensable in data analysis and scientific computing:

### 1. Pattern Recognition
Human brains are incredibly good at recognizing visual patterns. A trend that might be hidden in hundreds of numbers becomes immediately obvious when plotted. For example, seasonal patterns in temperature data or cyclical behavior in stock prices.

### 2. Communication
"A picture is worth a thousand words" is especially true in data science. A well-designed graph can communicate complex findings to any audience, regardless of their technical background. Instead of explaining statistics, you can show the story the data tells.

### 3. Quality Control
Visualizations help you spot problems in your data: outliers, missing values, measurement errors, or unexpected patterns. A scatter plot might reveal that your temperature sensor was giving impossible readings, or a time series might show gaps in your data collection.

### 4. Decision Making
Graphs help you make informed decisions by presenting data in context. Comparing different options, tracking progress toward goals, or identifying trends all become clearer with visualization.

### 5. Exploration
Often, you don't know what questions to ask until you see your data. Interactive plots let you explore relationships, test hypotheses, and discover unexpected insights.

## Intro to Plotting

Let's start with the fundamental concepts of plotting: axes, data, and how to put them together.

### Understanding Axes

Every plot has at least two axes:
- **X-axis (horizontal)**: Usually represents the independent variable - the thing you control or measure first
- **Y-axis (vertical)**: Usually represents the dependent variable - the thing that changes in response to X

Think of axes as the rulers on the edges of graph paper. They define the scale and units of measurement.

### Basic Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Simple example: How does a ball's height change when you drop it?
time_seconds = [0, 1, 2, 3, 4]  # Time in seconds
height_meters = [10, 8.1, 6.4, 4.9, 3.6]  # Height in meters (with air resistance)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(time_seconds, height_meters, 'ro-')  # 'ro-' means red circles connected by lines

# Add labels and title
plt.title('Falling Ball Height Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Height (meters)')

# Add a grid to make it easier to read values
plt.grid(True)

# Show the plot
plt.show()
```

### Bar Chart Example

Bar charts are great for comparing categories or showing discrete data:

```python
import matplotlib.pyplot as plt

# Example: Test scores in different subjects
subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores = [85, 92, 78, 88, 95]

plt.figure(figsize=(10, 6))
bars = plt.bar(subjects, scores, color=['blue', 'green', 'red', 'orange', 'purple'])

# Customize the chart
plt.title('Test Scores by Subject', fontsize=16)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Score (%)', fontsize=12)
plt.ylim(0, 100)  # Set Y-axis limits

# Add value labels on top of each bar
for bar, score in zip(bars, scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             str(score), ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.show()
```

### Scatter Plot Example

Scatter plots show relationships between two continuous variables:

```python
import matplotlib.pyplot as plt
import numpy as np

# Example: Does study time affect test scores?
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [45, 55, 65, 70, 75, 85, 88, 92, 95, 98]

plt.figure(figsize=(8, 6))
plt.scatter(study_hours, test_scores, color='blue', s=100, alpha=0.7)

# Add a trend line
z = np.polyfit(study_hours, test_scores, 1)  # Linear fit
p = np.poly1d(z)
plt.plot(study_hours, p(study_hours), "r--", alpha=0.8, linewidth=2)

plt.title('Study Time vs Test Scores')
plt.xlabel('Study Hours')
plt.ylabel('Test Score (%)')
plt.grid(True, alpha=0.3)

# Add correlation information
correlation = np.corrcoef(study_hours, test_scores)[0,1]
plt.text(2, 90, f'Correlation: {correlation:.2f}', fontsize=12, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.show()
```

### Multiple Data Series

Often you want to compare multiple datasets on the same plot:

```python
import matplotlib.pyplot as plt
import numpy as np

# Example: Temperature comparison between two cities
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city_a_temps = [32, 38, 48, 58, 68, 78, 85, 83, 76, 65, 50, 38]
city_b_temps = [45, 48, 55, 62, 70, 78, 82, 80, 75, 68, 58, 50]

plt.figure(figsize=(12, 6))
plt.plot(months, city_a_temps, 'b-o', label='City A', linewidth=2, markersize=6)
plt.plot(months, city_b_temps, 'r-s', label='City B', linewidth=2, markersize=6)

plt.title('Monthly Temperature Comparison', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Temperature (°F)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Subplots - Multiple Charts in One Figure

Sometimes you want to show related charts side by side:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1
ax1.plot(x, y1, 'b-', linewidth=2)
ax1.set_title('sin(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)

# Plot 2
ax2.plot(x, y2, 'r-', linewidth=2)
ax2.set_title('cos(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)

# Plot 3
ax3.plot(x, y3, 'g-', linewidth=2)
ax3.set_title('sin(x) × cos(x)')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.grid(True)

plt.tight_layout()
plt.show()
```

## Collecting Data

Good data visualization starts with good data collection. Here are the key principles and practical techniques for gathering data that will create meaningful visualizations.

### Data Collection Best Practices

**1. Consistency**: Collect data at regular intervals and use consistent units and formats. If you're measuring temperature every hour, don't suddenly switch to every 30 minutes without noting the change.

**2. Completeness**: Missing data points can distort your visualizations. Plan for data collection failures and have strategies for handling gaps.

**3. Accuracy**: Ensure your measuring instruments are calibrated and your data entry is error-free. One bad data point can skew an entire analysis.

**4. Context**: Always record when, where, and how data was collected. This metadata helps you interpret results and identify potential issues.

**5. Real-time vs. Batch**: Decide whether you need live updating visualizations or if processing data in batches is sufficient.

### Non-blocking Data Collection

When collecting data from sensors, cameras, or other real-time sources, you don't want your data collection to stop while creating visualizations. Here's how to handle this:

```python
import matplotlib.pyplot as plt
import numpy as np
import time
import threading
from collections import deque
import random

class DataCollector:
    def __init__(self, max_points=100):
        self.data = deque(maxlen=max_points)  # Automatically limits size
        self.timestamps = deque(maxlen=max_points)
        self.collecting = False
        self.thread = None
    
    def start_collection(self):
        """Start collecting data in a separate thread"""
        self.collecting = True
        self.thread = threading.Thread(target=self._collect_data)
        self.thread.daemon = True  # Dies when main program exits
        self.thread.start()
        print("Data collection started...")
    
    def stop_collection(self):
        """Stop collecting data"""
        self.collecting = False
        if self.thread:
            self.thread.join()
        print("Data collection stopped.")
    
    def _collect_data(self):
        """Simulate collecting sensor data"""
        while self.collecting:
            # Simulate sensor reading (replace with actual sensor code)
            sensor_value = 50 + 10 * np.sin(time.time() / 5) + random.gauss(0, 2)
            
            # Store data with timestamp
            self.data.append(sensor_value)
            self.timestamps.append(time.time())
            
            time.sleep(0.1)  # Collect data every 100ms
    
    def get_data(self):
        """Get current data for plotting"""
        return list(self.timestamps), list(self.data)
    
    def plot_current_data(self):
        """Create a plot of current data"""
        if len(self.data) < 2:
            print("Not enough data to plot yet...")
            return
        
        times, values = self.get_data()
        
        # Convert timestamps to relative time in seconds
        start_time = times[0]
        relative_times = [(t - start_time) for t in times]
        
        plt.figure(figsize=(12, 6))
        plt.plot(relative_times, values, 'b-', linewidth=2, alpha=0.7)
        plt.title('Real-time Sensor Data')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Sensor Value')
        plt.grid(True, alpha=0.3)
        
        # Add statistics
        avg_value = np.mean(values)
        std_value = np.std(values)
        plt.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7, 
                   label=f'Average: {avg_value:.1f}')
        
        plt.legend()
        plt.tight_layout()
        plt.show()

# Example usage
def data_collection_example():
    collector = DataCollector(max_points=200)
    
    try:
        collector.start_collection()
        
        # Let it collect data for a while
        print("Collecting data for 10 seconds...")
        time.sleep(10)
        
        # Plot the collected data
        collector.plot_current_data()
        
        # Continue collecting and plot again
        print("Collecting for 10 more seconds...")
        time.sleep(10)
        collector.plot_current_data()
        
    finally:
        collector.stop_collection()

# Uncomment to run the example
# data_collection_example()
```

### Reading Data from Files

Often you'll want to load data from CSV files or other sources for visualization:

```python
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import csv

def plot_csv_data():
    """Load and plot data from a CSV file"""
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not file_path:
        return
    
    try:
        # Read the CSV file
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # First row is headers
            
            # Read all data
            data = []
            for row in csv_reader:
                data.append(row)
        
        # Convert to numpy array for easier manipulation
        data_array = np.array(data)
        
        print(f"Loaded data with shape: {data_array.shape}")
        print(f"Headers: {headers}")
        
        # If we have at least 2 columns, create a basic plot
        if len(headers) >= 2:
            try:
                # Try to convert to numbers
                x_data = [float(val) for val in data_array[:, 0]]
                y_data = [float(val) for val in data_array[:, 1]]
                
                plt.figure(figsize=(10, 6))
                plt.plot(x_data, y_data, 'bo-', markersize=4, linewidth=1)
                plt.title(f'Data from {file_path.split("/")[-1]}')
                plt.xlabel(headers[0])
                plt.ylabel(headers[1])
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.show()
                
            except ValueError:
                print("Could not convert data to numbers. Showing first few rows:")
                for i, row in enumerate(data[:5]):
                    print(f"Row {i+1}: {row}")
        
    except Exception as e:
        print(f"Error reading file: {e}")
    
    root.destroy()

# Example: Create sample CSV data
def create_sample_csv():
    """Create a sample CSV file for testing"""
    filename = "sample_temperature_data.csv"
    
    # Generate sample temperature data
    hours = range(24)
    temperatures = [65 + 15 * np.sin((h - 6) * np.pi / 12) + 
                   np.random.normal(0, 2) for h in hours]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Hour', 'Temperature_F'])  # Headers
        for hour, temp in zip(hours, temperatures):
            writer.writerow([hour, f"{temp:.1f}"])
    
    print(f"Created sample file: {filename}")
    return filename

# Uncomment these lines to test:
# create_sample_csv()
# plot_csv_data()
```

## Performing Statistical Analysis on Images

Images contain a wealth of statistical information that can be analyzed and visualized. By combining OpenCV for image processing with MatPlotLib for visualization, we can gain insights into image characteristics, quality, and content.

### Understanding Image Statistics

Every digital image can be analyzed statistically. The pixel values themselves are data points that can tell us about brightness, contrast, color distribution, and image quality.

### Histogram Analysis

A histogram shows the distribution of pixel intensities in an image. It's one of the most fundamental tools in image analysis:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def analyze_image_histogram():
    """Load an image and analyze its histogram"""
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select an Image for Histogram Analysis",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_path:
        root.destroy()
        return
    
    # Load the image
    image = cv2.imread(file_path)
    if image is None:
        print("Could not load image!")
        root.destroy()
        return
    
    # Convert BGR to RGB for matplotlib display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Display original image
    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Calculate and plot color histograms
    colors = ['red', 'green', 'blue']
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        axes[0, 1].plot(hist, color=color, alpha=0.7, linewidth=2)
    
    axes[0, 1].set_title('RGB Histogram')
    axes[0, 1].set_xlabel('Pixel Intensity')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend(['Red', 'Green', 'Blue'])
    axes[0, 1].grid(True, alpha=0.3)
    
    # Convert to grayscale and analyze
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Display grayscale image
    axes[1, 0].imshow(gray, cmap='gray')
    axes[1, 0].set_title('Grayscale Version')
    axes[1, 0].axis('off')
    
    # Grayscale histogram
    hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
    axes[1, 1].plot(hist_gray, color='black', linewidth=2)
    axes[1, 1].set_title('Grayscale Histogram')
    axes[1, 1].set_xlabel('Pixel Intensity')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].grid(True, alpha=0.3)
    
    # Add statistics
    mean_intensity = np.mean(gray)
    std_intensity = np.std(gray)
    axes[1, 1].axvline(x=mean_intensity, color='red', linestyle='--', 
                      label=f'Mean: {mean_intensity:.1f}')
    axes[1, 1].axvline(x=mean_intensity + std_intensity, color='orange', 
                      linestyle='--', alpha=0.7, label=f'+1 Std: {mean_intensity + std_intensity:.1f}')
    axes[1, 1].axvline(x=mean_intensity - std_intensity, color='orange', 
                      linestyle='--', alpha=0.7, label=f'-1 Std: {mean_intensity - std_intensity:.1f}')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
    # Print analysis
    print(f"\n=== Image Analysis ===")
    print(f"Image size: {image.shape[1]} x {image.shape[0]} pixels")
    print(f"Mean brightness: {mean_intensity:.2f}")
    print(f"Standard deviation: {std_intensity:.2f}")
    print(f"Brightness range: {np.min(gray)} to {np.max(gray)}")
    
    # Determine image characteristics
    if mean_intensity < 85:
        print("This appears to be a dark image")
    elif mean_intensity > 170:
        print("This appears to be a bright image")
    else:
        print("This appears to be a well-balanced image")
    
    if std_intensity < 30:
        print("Low contrast image (narrow intensity range)")
    elif std_intensity > 70:
        print("High contrast image (wide intensity range)")
    else:
        print("Moderate contrast image")
    
    root.destroy()

# Run the analysis
analyze_image_histogram()
```

### Edge Detection Analysis

Edge detection reveals the structure and features in an image. We can analyze and visualize edge information:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def analyze_image_edges():
    """Analyze edge information in an image"""
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select an Image for Edge Analysis",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_path:
        root.destroy()
        return
    
    # Load and process image
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply different edge detection methods
    edges_canny = cv2.Canny(gray, 50, 150)
    edges_sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    edges_sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges_sobel = np.sqrt(edges_sobel_x**2 + edges_sobel_y**2)
    
    # Create visualization
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Original image
    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Grayscale
    axes[0, 1].imshow(gray, cmap='gray')
    axes[0, 1].set_title('Grayscale')
    axes[0, 1].axis('off')
    
    # Canny edges
    axes[0, 2].imshow(edges_canny, cmap='gray')
    axes[0, 2].set_title('Canny Edge Detection')
    axes[0, 2].axis('off')
    
    # Sobel X
    axes[1, 0].imshow(np.abs(edges_sobel_x), cmap='gray')
    axes[1, 0].set_title('Sobel X (Vertical Edges)')
    axes[1, 0].axis('off')
    
    # Sobel Y
    axes[1, 1].imshow(np.abs(edges_sobel_y), cmap='gray')
    axes[1, 1].set_title('Sobel Y (Horizontal Edges)')
    axes[1, 1].axis('off')
    
    # Sobel Combined
    axes[1, 2].imshow(edges_sobel, cmap='gray')
    axes[1, 2].set_title('Sobel Combined')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Statistical analysis of edges
    total_pixels = gray.shape[0] * gray.shape[1]
    edge_pixels_canny = np.sum(edges_canny > 0)
    edge_percentage = (edge_pixels_canny / total_pixels) * 100
    
    print(f"\n=== Edge Analysis ===")
    print(f"Total pixels: {total_pixels}")
    print(f"Edge pixels (Canny): {edge_pixels_canny}")
    print(f"Edge percentage: {edge_percentage:.2f}%")
    
    if edge_percentage < 5:
        print("Low detail image (smooth textures, few edges)")
    elif edge_percentage > 15:
        print("High detail image (complex textures, many edges)")
    else:
        print("Moderate detail image")
    
    # Create edge density plot
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Edge density across rows
    plt.subplot(1, 2, 1)
    row_edges = np.sum(edges_canny, axis=1)
    plt.plot(row_edges)
    plt.title('Edge Density by Row')
    plt.xlabel('Row Number')
    plt.ylabel('Number of Edge Pixels')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Edge density across columns
    plt.subplot(1, 2, 2)
    col_edges = np.sum(edges_canny, axis=0)
    plt.plot(col_edges)
    plt.title('Edge Density by Column')
    plt.xlabel('Column Number')
    plt.ylabel('Number of Edge Pixels')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    root.destroy()

# Run the edge analysis
analyze_image_edges()
```

### Color Analysis and Visualization

Analyzing color distribution can reveal important characteristics about images:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def analyze_image_colors():
    """Comprehensive color analysis of an image"""
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select an Image for Color Analysis",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_path:
        root.destroy()
        return
    
    # Load image
    image = cv2.imread(file_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create comprehensive analysis
    fig = plt.figure(figsize=(20, 15))
    
    # Original image
    ax1 = plt.subplot(3, 4, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')
    
    # Individual RGB channels
    channels = ['Red', 'Green', 'Blue']
    colors = ['Reds', 'Greens', 'Blues']
    
    for i in range(3):
        ax = plt.subplot(3, 4, i + 2)
        channel = image_rgb[:, :, i]
        plt.imshow(channel, cmap=colors[i])
        plt.title(f'{channels[i]} Channel')
        plt.axis('off')
    
    # RGB Histogram
    ax5 = plt.subplot(3, 4, 5)
    for i, color in enumerate(['red', 'green', 'blue']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, alpha=0.7, linewidth=2)
    plt.title('RGB Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # HSV Analysis
    hue = image_hsv[:, :, 0]
    saturation = image_hsv[:, :, 1]
    value = image_hsv[:, :, 2]
    
    # Hue histogram (color wheel analysis)
    ax6 = plt.subplot(3, 4, 6)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
    plt.plot(hist_hue, color='purple', linewidth=2)
    plt.title('Hue Distribution')
    plt.xlabel('Hue Value (0-179)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Saturation histogram
    ax7 = plt.subplot(3, 4, 7)
    hist_sat = cv2.calcHist([image_hsv], [1], None, [256], [0, 256])
    plt.plot(hist_sat, color='orange', linewidth=2)
    plt.title('Saturation Distribution')
    plt.xlabel('Saturation Value (0-255)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Value/Brightness histogram
    ax8 = plt.subplot(3, 4, 8)
    hist_val = cv2.calcHist([image_hsv], [2], None, [256], [0, 256])
    plt.plot(hist_val, color='gray', linewidth=2)
    plt.title('Brightness Distribution')
    plt.xlabel('Brightness Value (0-255)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Color dominance pie chart
    ax9 = plt.subplot(3, 4, 9)
    
    # Calculate average color values
    avg_red = np.mean(image_rgb[:, :, 0])
    avg_green = np.mean(image_rgb[:, :, 1])
    avg_blue = np.mean(image_rgb[:, :, 2])
    
    colors_pie = [avg_red, avg_green, avg_blue]
    colors_names = ['Red', 'Green', 'Blue']
    colors_hex = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    plt.pie(colors_pie, labels=colors_names, colors=colors_hex, autopct='%1.1f%%', startangle=90)
    plt.title('Average Color Distribution')
    
    # 2D Histogram (Hue vs Saturation)
    ax10 = plt.subplot(3, 4, 10)
    plt.hist2d(hue.flatten(), saturation.flatten(), bins=50, cmap='viridis')
    plt.title('Hue vs Saturation')
    plt.xlabel('Hue')
    plt.ylabel('Saturation')
    plt.colorbar(label='Frequency')
    
    # Color temperature analysis
    ax11 = plt.subplot(3, 4, 11)
    
    # Calculate color temperature indicator
    blue_avg = np.mean(image_rgb[:, :, 2])
    red_avg = np.mean(image_rgb[:, :, 0])
    color_temp_ratio = blue_avg / (red_avg + 1)  # +1 to avoid division by zero
    
    temp_categories = ['Very Warm', 'Warm', 'Neutral', 'Cool', 'Very Cool']
    temp_values = [0.8, 0.9, 1.0, 1.1, 1.2]
    temp_colors = ['#FF4444', '#FF8844', '#FFFF44', '#44FFFF', '#4444FF']
    
    bars = plt.bar(temp_categories, temp_values, color=temp_colors, alpha=0.7)
    plt.axhline(y=color_temp_ratio, color='red', linestyle='--', linewidth=3, label=f'This image: {color_temp_ratio:.2f}')
    plt.title('Color Temperature Analysis')
    plt.ylabel('Blue/Red Ratio')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Dominant colors extraction
    ax12 = plt.subplot(3, 4, 12)
    
    # Reshape image for k-means clustering
    pixel_data = image_rgb.reshape(-1, 3)
    
    # Simple dominant color extraction (top 5 colors)
    from collections import Counter
    
    # Reduce color space for easier analysis
    reduced_pixels = pixel_data // 32 * 32  # Quantize to reduce similar colors
    pixel_tuples = [tuple(pixel) for pixel in reduced_pixels]
    color_counts = Counter(pixel_tuples)
    
    # Get top 5 most common colors
    top_colors = color_counts.most_common(5)
    
    # Create color palette
    colors_palette = [color[0] for color in top_colors]
    counts_palette = [color[1] for color in top_colors]
    
    # Normalize colors for display
    colors_normalized = [[c/255.0 for c in color] for color in colors_palette]
    
    bars = plt.bar(range(len(colors_palette)), counts_palette, color=colors_normalized)
    plt.title('Top 5 Dominant Colors')
    plt.xlabel('Color Rank')
    plt.ylabel('Pixel Count')
    
    # Add color values as text
    for i, (bar, color) in enumerate(zip(bars, colors_palette)):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(counts_palette)*0.01,
                f'RGB({color[0]},{color[1]},{color[2]})', 
                ha='center', va='bottom', fontsize=8, rotation=90)
    
    plt.tight_layout()
    plt.show()
    
    # Print comprehensive analysis
    print(f"\n=== Comprehensive Color Analysis ===")
    print(f"Image dimensions: {image_rgb.shape[1]} x {image_rgb.shape[0]} pixels")
    print(f"Total pixels: {image_rgb.shape[0] * image_rgb.shape[1]}")
    
    print(f"\n--- RGB Statistics ---")
    print(f"Average Red: {avg_red:.1f}")
    print(f"Average Green: {avg_green:.1f}")
    print(f"Average Blue: {avg_blue:.1f}")
    
    print(f"\n--- HSV Statistics ---")
    print(f"Average Hue: {np.mean(hue):.1f}")
    print(f"Average Saturation: {np.mean(saturation):.1f}")
    print(f"Average Brightness: {np.mean(value):.1f}")
    
    # Color temperature analysis
    if color_temp_ratio < 0.9:
        print(f"\n--- Color Temperature: WARM ---")
        print("This image has warm tones (more red/yellow)")
    elif color_temp_ratio > 1.1:
        print(f"\n--- Color Temperature: COOL ---")
        print("This image has cool tones (more blue)")
    else:
        print(f"\n--- Color Temperature: NEUTRAL ---")
        print("This image has balanced color temperature")
    
    # Saturation analysis
    avg_saturation = np.mean(saturation)
    if avg_saturation < 100:
        print(f"\n--- Saturation: LOW ---")
        print("This image appears muted or desaturated")
    elif avg_saturation > 180:
        print(f"\n--- Saturation: HIGH ---")
        print("This image has very vibrant, saturated colors")
    else:
        print(f"\n--- Saturation: MODERATE ---")
        print("This image has normal color saturation")
    
    print(f"\n--- Dominant Colors ---")
    for i, (color, count) in enumerate(top_colors):
        percentage = (count / (image_rgb.shape[0] * image_rgb.shape[1])) * 100
        print(f"#{i+1}: RGB{color} - {percentage:.1f}% of image")
    
    root.destroy()

# Run the comprehensive color analysis
analyze_image_colors()
```

### Image Quality Assessment

We can also analyze images to assess their technical quality:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def assess_image_quality():
    """Assess various quality metrics of an image"""
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select an Image for Quality Assessment",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_path:
        root.destroy()
        return
    
    # Load image
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Calculate various quality metrics
    
    # 1. Sharpness (using Laplacian variance)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    # 2. Contrast (standard deviation of pixel intensities)
    contrast = np.std(gray)
    
    # 3. Brightness (mean pixel intensity)
    brightness = np.mean(gray)
    
    # 4. Noise estimation (using high-frequency components)
    # Apply Gaussian blur and subtract from original
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    noise_estimate = np.std(gray.astype(np.float64) - blurred.astype(np.float64))
    
    # 5. Dynamic range
    dynamic_range = np.max(gray) - np.min(gray)
    
    # 6. Histogram analysis for exposure
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # Check for clipping (overexposure/underexposure)
    underexposed_pixels = hist[0:10].sum()
    overexposed_pixels = hist[246:256].sum()
    total_pixels = gray.shape[0] * gray.shape[1]
    
    underexposed_percent = (underexposed_pixels / total_pixels) * 100
    overexposed_percent = (overexposed_pixels / total_pixels) * 100
    
    # Create quality assessment visualization
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Original image
    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Sharpness visualization (Laplacian)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    axes[0, 1].imshow(np.abs(laplacian), cmap='gray')
    axes[0, 1].set_title(f'Sharpness Map\n(Laplacian Variance: {laplacian_var:.0f})')
    axes[0, 1].axis('off')
    
    # Histogram with quality indicators
    axes[0, 2].plot(hist, color='black', linewidth=2)
    axes[0, 2].axvline(x=brightness, color='blue', linestyle='--', linewidth=2, label=f'Mean: {brightness:.1f}')
    axes[0, 2].axvspan(0, 10, alpha=0.3, color='red', label=f'Underexposed: {underexposed_percent:.1f}%')
    axes[0, 2].axvspan(246, 255, alpha=0.3, color='yellow', label=f'Overexposed: {overexposed_percent:.1f}%')
    axes[0, 2].set_title('Exposure Analysis')
    axes[0, 2].set_xlabel('Pixel Intensity')
    axes[0, 2].set_ylabel('Frequency')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)
    
    # Noise visualization
    noise_map = np.abs(gray.astype(np.float64) - blurred.astype(np.float64))
    axes[1, 0].imshow(noise_map, cmap='hot')
    axes[1, 0].set_title(f'Noise Estimation\n(Std Dev: {noise_estimate:.2f})')
    axes[1, 0].axis('off')
    
    # Quality metrics bar chart
    metrics = ['Sharpness', 'Contrast', 'Brightness', 'Dynamic Range', 'Noise Level']
    values = [laplacian_var/100, contrast, brightness, dynamic_range, noise_estimate*10]  # Normalized for display
    colors = ['green', 'blue', 'orange', 'purple', 'red']
    
    bars = axes[1, 1].bar(metrics, values, color=colors, alpha=0.7)
    axes[1, 1].set_title('Quality Metrics Overview')
    axes[1, 1].set_ylabel('Normalized Values')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, value in zip(bars, [laplacian_var, contrast, brightness, dynamic_range, noise_estimate]):
        axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.01,
                       f'{value:.1f}', ha='center', va='bottom', fontsize=10)
    
    # Overall quality score
    axes[1, 2].axis('off')
    
    # Calculate overall quality score (0-100)
    sharpness_score = min(100, laplacian_var / 5)  # Good if > 500
    contrast_score = min(100, contrast / 0.8)  # Good if > 80
    brightness_score = 100 - abs(brightness - 128) / 1.28  # Best around 128
    exposure_score = 100 - (underexposed_percent + overexposed_percent) * 2  # Penalize clipping
    noise_score = max(0, 100 - noise_estimate * 10)  # Lower noise is better
    
    overall_score = (sharpness_score + contrast_score + brightness_score + exposure_score + noise_score) / 5
    
    # Create quality gauge
    quality_text = f"""
    OVERALL QUALITY SCORE: {overall_score:.1f}/100
    
    Individual Scores:
    • Sharpness: {sharpness_score:.1f}/100
    • Contrast: {contrast_score:.1f}/100
    • Brightness: {brightness_score:.1f}/100
    • Exposure: {exposure_score:.1f}/100
    • Noise: {noise_score:.1f}/100
    
    Technical Details:
    • Laplacian Variance: {laplacian_var:.0f}
    • Contrast (StdDev): {contrast:.1f}
    • Mean Brightness: {brightness:.1f}
    • Dynamic Range: {dynamic_range}
    • Noise Level: {noise_estimate:.2f}
    """
    
    axes[1, 2].text(0.1, 0.9, quality_text, transform=axes[1, 2].transAxes, 
                   fontsize=12, verticalalignment='top', fontfamily='monospace',
                   bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # Print detailed assessment
    print(f"\n=== IMAGE QUALITY ASSESSMENT ===")
    print(f"File: {file_path.split('/')[-1]}")
    print(f"Dimensions: {image.shape[1]} x {image.shape[0]} pixels")
    
    print(f"\n--- Sharpness Analysis ---")
    if laplacian_var > 500:
        print(f"✓ SHARP: Laplacian variance = {laplacian_var:.0f} (Good: >500)")
    elif laplacian_var > 100:
        print(f"~ MODERATE: Laplacian variance = {laplacian_var:.0f} (Acceptable: 100-500)")
    else:
        print(f"✗ BLURRY: Laplacian variance = {laplacian_var:.0f} (Poor: <100)")
    
    print(f"\n--- Contrast Analysis ---")
    if contrast > 80:
        print(f"✓ HIGH CONTRAST: Standard deviation = {contrast:.1f} (Good: >80)")
    elif contrast > 40:
        print(f"~ MODERATE CONTRAST: Standard deviation = {contrast:.1f} (Acceptable: 40-80)")
    else:
        print(f"✗ LOW CONTRAST: Standard deviation = {contrast:.1f} (Poor: <40)")
    
    print(f"\n--- Exposure Analysis ---")
    if underexposed_percent > 5:
        print(f"⚠ UNDEREXPOSED: {underexposed_percent:.1f}% of pixels are very dark")
    if overexposed_percent > 5:
        print(f"⚠ OVEREXPOSED: {overexposed_percent:.1f}% of pixels are blown out")
    if underexposed_percent <= 5 and overexposed_percent <= 5:
        print(f"✓ WELL EXPOSED: Minimal clipping in shadows and highlights")
    
    print(f"\n--- Noise Analysis ---")
    if noise_estimate < 5:
        print(f"✓ LOW NOISE: Noise level = {noise_estimate:.2f} (Good: <5)")
    elif noise_estimate < 15:
        print(f"~ MODERATE NOISE: Noise level = {noise_estimate:.2f} (Acceptable: 5-15)")
    else:
        print(f"✗ HIGH NOISE: Noise level = {noise_estimate:.2f} (Poor: >15)")
    
    print(f"\n--- Overall Assessment ---")
    if overall_score >= 80:
        print(f"✓ EXCELLENT QUALITY: Score = {overall_score:.1f}/100")
    elif overall_score >= 60:
        print(f"✓ GOOD QUALITY: Score = {overall_score:.1f}/100")
    elif overall_score >= 40:
        print(f"~ FAIR QUALITY: Score = {overall_score:.1f}/100")
    else:
        print(f"✗ POOR QUALITY: Score = {overall_score:.1f}/100")
    
    root.destroy()

# Run the quality assessment
assess_image_quality()
```

### Batch Analysis for Multiple Images

Sometimes you want to analyze multiple images and compare their characteristics:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def batch_image_analysis():
    """Analyze multiple images and create comparison charts"""
    root = tk.Tk()
    root.withdraw()
    
    # Select multiple image files
    file_paths = filedialog.askopenfilenames(
        title="Select Multiple Images for Batch Analysis",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_paths:
        root.destroy()
        return
    
    # Store results for all images
    results = []
    
    print(f"Analyzing {len(file_paths)} images...")
    
    for i, file_path in enumerate(file_paths):
        print(f"Processing image {i+1}/{len(file_paths)}: {os.path.basename(file_path)}")
        
        # Load and analyze image
        image = cv2.imread(file_path)
        if image is None:
            print(f"Could not load {file_path}, skipping...")
            continue
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Calculate metrics
        brightness = np.mean(gray)
        contrast = np.std(gray)
        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # Color analysis
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        avg_red = np.mean(image_rgb[:, :, 0])
        avg_green = np.mean(image_rgb[:, :, 1])
        avg_blue = np.mean(image_rgb[:, :, 2])
        
        # File size
        file_size = os.path.getsize(file_path) / 1024  # KB
        
        results.append({
            'filename': os.path.basename(file_path),
            'brightness': brightness,
            'contrast': contrast,
            'sharpness': sharpness,
            'red': avg_red,
            'green': avg_green,
            'blue': avg_blue,
            'file_size': file_size,
            'width': image.shape[1],
            'height': image.shape[0]
        })
    
    if not results:
        print("No images could be processed!")
        root.destroy()
        return
    
    # Create comparison visualizations
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    
    filenames = [r['filename'] for r in results]
    
    # Brightness comparison
    brightness_values = [r['brightness'] for r in results]
    axes[0, 0].bar(range(len(results)), brightness_values, color='orange', alpha=0.7)
    axes[0, 0].set_title('Brightness Comparison')
    axes[0, 0].set_ylabel('Average Brightness')
    axes[0, 0].set_xticks(range(len(results)))
    axes[0, 0].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    
    # Contrast comparison
    contrast_values = [r['contrast'] for r in results]
    axes[0, 1].bar(range(len(results)), contrast_values, color='blue', alpha=0.7)
    axes[0, 1].set_title('Contrast Comparison')
    axes[0, 1].set_ylabel('Contrast (Std Dev)')
    axes[0, 1].set_xticks(range(len(results)))
    axes[0, 1].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    
    # Sharpness comparison
    sharpness_values = [r['sharpness'] for r in results]
    axes[0, 2].bar(range(len(results)), sharpness_values, color='green', alpha=0.7)
    axes[0, 2].set_title('Sharpness Comparison')
    axes[0, 2].set_ylabel('Sharpness (Laplacian Var)')
    axes[0, 2].set_xticks(range(len(results)))
    axes[0, 2].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    
    # Color comparison
    red_values = [r['red'] for r in results]
    green_values = [r['green'] for r in results]
    blue_values = [r['blue'] for r in results]
    
    x = np.arange(len(results))
    width = 0.25
    
    axes[1, 0].bar(x - width, red_values, width, label='Red', color='red', alpha=0.7)
    axes[1, 0].bar(x, green_values, width, label='Green', color='green', alpha=0.7)
    axes[1, 0].bar(x + width, blue_values, width, label='Blue', color='blue', alpha=0.7)
    axes[1, 0].set_title('Average Color Values')
    axes[1, 0].set_ylabel('Average Channel Value')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    axes[1, 0].legend()
    
    # File size comparison
    file_sizes = [r['file_size'] for r in results]
    axes[1, 1].bar(range(len(results)), file_sizes, color='purple', alpha=0.7)
    axes[1, 1].set_title('File Size Comparison')
    axes[1, 1].set_ylabel('File Size (KB)')
    axes[1, 1].set_xticks(range(len(results)))
    axes[1, 1].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    
    # Resolution comparison
    resolutions = [r['width'] * r['height'] / 1000000 for r in results]  # Megapixels
    axes[1, 2].bar(range(len(results)), resolutions, color='brown', alpha=0.7)
    axes[1, 2].set_title('Resolution Comparison')
    axes[1, 2].set_ylabel('Resolution (Megapixels)')
    axes[1, 2].set_xticks(range(len(results)))
    axes[1, 2].set_xticklabels([f[:10] + '...' if len(f) > 10 else f for f in filenames], rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    print(f"\n=== BATCH ANALYSIS SUMMARY ===")
    print(f"Total images analyzed: {len(results)}")
    
    print(f"\n--- Brightness Statistics ---")
    print(f"Brightest image: {filenames[brightness_values.index(max(brightness_values))]} ({max(brightness_values):.1f})")
    print(f"Darkest image: {filenames[brightness_values.index(min(brightness_values))]} ({min(brightness_values):.1f})")
    print(f"Average brightness: {np.mean(brightness_values):.1f}")
    
    print(f"\n--- Contrast Statistics ---")
    print(f"Highest contrast: {filenames[contrast_values.index(max(contrast_values))]} ({max(contrast_values):.1f})")
    print(f"Lowest contrast: {filenames[contrast_values.index(min(contrast_values))]} ({min(contrast_values):.1f})")
    print(f"Average contrast: {np.mean(contrast_values):.1f}")
    
    print(f"\n--- Sharpness Statistics ---")
    print(f"Sharpest image: {filenames[sharpness_values.index(max(sharpness_values))]} ({max(sharpness_values):.0f})")
    print(f"Blurriest image: {filenames[sharpness_values.index(min(sharpness_values))]} ({min(sharpness_values):.0f})")
    print(f"Average sharpness: {np.mean(sharpness_values):.0f}")
    
    print(f"\n--- File Size Statistics ---")
    print(f"Largest file: {filenames[file_sizes.index(max(file_sizes))]} ({max(file_sizes):.1f} KB)")
    print(f"Smallest file: {filenames[file_sizes.index(min(file_sizes))]} ({min(file_sizes):.1f} KB)")
    print(f"Average file size: {np.mean(file_sizes):.1f} KB")
    
    root.destroy()

# Run the batch analysis
batch_image_analysis()
```

## Summary and Next Steps

MatPlotLib is an incredibly powerful tool for data visualization that becomes even more useful when combined with image processing libraries like OpenCV. Through this tutorial, you've learned:

1. **Basic Plotting Concepts**: Understanding axes, data relationships, and different chart types
2. **Data Collection Strategies**: How to gather data effectively without blocking your main program
3. **Image Statistical Analysis**: Extracting meaningful numerical data from images
4. **Quality Assessment**: Using statistical methods to evaluate image characteristics
5. **Batch Processing**: Analyzing multiple images for comparison and pattern detection

### Key Takeaways

- **Visualization reveals patterns** that are invisible in raw data
- **Different chart types** serve different purposes - choose the right tool for your data
- **Statistical analysis of images** can reveal technical quality, artistic characteristics, and content information
- **Batch processing** allows for comprehensive analysis and comparison across multiple images
- **Good data collection practices** are essential for meaningful visualizations

### Practical Applications

These techniques have real-world applications in:
- **Photography**: Analyzing image quality, exposure, and composition
- **Security Systems**: Monitoring image quality from surveillance cameras
- **Medical Imaging**: Assessing image quality for diagnostic purposes
- **Scientific Research**: Analyzing experimental data and research imagery
- **Quality Control**: Automated inspection of manufactured products
- **Social Media**: Analyzing image characteristics for content optimization

### Links and Further Reading

- **MatPlotLib Official Tutorial**: https://matplotlib.org/stable/tutorials/pyplot.html
- **MatPlotLib Gallery**: https://matplotlib.org/stable/gallery/index.html
- **OpenCV Documentation**: https://docs.opencv.org/
- **NumPy Statistical Functions**: https://numpy.org/doc/stable/reference/routines.statistics.html
- **Image Processing Fundamentals**: https://opencv-python-tutroals.readthedocs.io/

Remember: the best way to learn data visualization is through practice. Start with your own images and data, experiment with different chart types, and don't be afraid to try new approaches. Every dataset has a story to tell - your job is to find the best way to visualize that story!
