import tkinter as tk
from tkinter import font


def measure_text_width(text):
    # Create a temporary window
    root = tk.Tk()
    root.geometry("1x1")

    # Create a Label widget with the specified text
    label = tk.Label(root, text=text)
    label.pack()

    # Get the font used in the Label widget
    label_font = font.nametofont(label.cget("font"))

    # Measure the text width in pixels
    text_width = label_font.measure(text)

    # Count the characters in the text
    num_characters = len(text)

    # Close the temporary window
    root.destroy()

    return text_width, num_characters

# Enter 5 strings
texts_to_measure = [
    "A1B2CUL2OPW3C9D0E1F2G3H4I5J6K7L8M9N0O1P2Q3R4S5T6U7V8W9X0Y1Z2A3B4C5D6E7F8G9H0I1J2K3L4M5N6O7P8Q9R0S1T2U3V4W5X6Y7Z8A9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y3Z44Q5R6S7T8U9V0W1X2Y3Z4",
    "A1B2CUL2F2G3H4I5J6K7L8M9N0O1P2Q3R4S5T6U7V8W9X0Y1Z2A3B4C5D6E7F8G9H0I1J2K3L4M5N6O7P8Q9R0S1T2U3V4W5X6Y7Z8A9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y3Z44Q5R6S7T8U9V0W1X2Y3Z4",
    "A1B2CUL6K7L8M9N0O1P2Q3R4S5T6U7V8W9X0Y1Z2A3B4C5D6E7F8G9H0I1J2K3L4M5N6O7P8Q9R0S1T2U3V4W5X6Y7Z8A9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y3Z44Q5R6S7T8U9V0W1X2Y3Z4",
    "A1B2CUL6K7Q3R4S5T6U7V8W9X0Y1Z2A3B4C5D6E7F8G9H0I1J2K3L4M5N6O7P8Q9R0S1T2U3V4W5X6Y7Z8A9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y3Z44Q5R6S7T8U9V0W1X2Y3Z4",
    "A1B2CUL6K7V8W9X0Y1Z2A3B4C5D6E7F8G9H0I1J2K3L4M5N6O7P8Q9R0S1T2U3V4W5X6Y7Z8A9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y3Z44Q5R6S7T8U9V0W1X2Y3Z4"
]

# Measure and print the results for each entered string
for i, text in enumerate(texts_to_measure):
    width, num_chars = measure_text_width(text)
    print(f"String {i + 1}:")
    print(f"   Text: '{text}'")
    print(f"   Text width: {width} pixels")
    print(f"   Number of characters: {num_chars}\n")
