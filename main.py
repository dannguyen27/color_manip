import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches

print("Imports are working!")

# Load and display an image
img_path = 'DSC00442.jpg'
try:
    img = Image.open(img_path)
    img_array = np.array(img)

    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.title('Click on the image to get the RGB value')

    # Create an axis for displaying selected colors
    color_fig, color_ax = plt.subplots(figsize=(2, 5))
    color_ax.set_title("Selected Colors")
    color_ax.axis('off')  # Hide the axis for cleaner display

    # Define the on_click event handler
    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            x = int(event.xdata)
            y = int(event.ydata)
            print(f"Coordinates selected: x={x}, y={y}")

            # Get the RGB value at the selected coordinates
            if x < img_array.shape[1] and y < img_array.shape[0]:
                rgb_value = img_array[y, x]  # Note: img_array is indexed [y, x]
                print(f"RGB value at ({x}, {y}): {rgb_value}")

                # Normalize RGB values for display in the range [0, 1]
                rgb_normalized = rgb_value / 255.0

                # Create a rectangle patch filled with the selected color
                color_rect = patches.Rectangle((0, len(color_ax.patches) * 0.2), 1, 0.2, 
                                               color=rgb_normalized, transform=color_ax.transAxes)

                color_ax.add_patch(color_rect)  # Add the patch to the color display
                color_fig.canvas.draw()  # Update the color figure with new patches
            else:
                print("Coordinates are out of bounds.")

    # Connect the click event to the event handler
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    # Show both the image and the color display plot
    plt.show()

except FileNotFoundError:
    print(f"Image file {img_path} not found.")
