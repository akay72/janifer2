import streamlit as st
import re

# Streamlit UI
st.title("Dynamic Math Equation Highlighter")

# Input field for the equation
equation = st.text_area(
    "Enter your math equation (supports both LaTeX and Unicode):",
    r"y_i = β_1 x_{i1} + β_2 x_{i2} + ⋯ + β_p x_{ip} + ε_i",
)

# Sidebar for color options
st.sidebar.title("Customize Variable Colors")

# Color pickers in the sidebar
x_color = st.sidebar.color_picker("Choose color for x:", "#FF0000")
y_color = st.sidebar.color_picker("Choose color for y:", "#00FF00")
b_color = st.sidebar.color_picker("Choose color for β (beta):", "#0000FF")
e_color = st.sidebar.color_picker("Choose color for ε (epsilon):", "#800080")

# Map variables to user-selected colors
color_map = {
    r"x": x_color,
    r"y": y_color,
    r"β": b_color,       # Unicode beta
    r"ε": e_color,       # Unicode epsilon
    r"\\beta": b_color,  # LaTeX beta
    r"\\epsilon": e_color,  # LaTeX epsilon
}

# Function to apply colors to variables in the equation
def colorize_variables(equation, color_map):
    for var, color in color_map.items():
        # Match variables and apply LaTeX \textcolor command
        equation = re.sub(fr"({var})", rf"\\textcolor{{{color}}}{{{var}}}", equation)
    return equation

# Apply coloring to the equation
colored_equation = colorize_variables(equation, color_map)

# Display the colored equation
st.markdown("### Highlighted Equation")
st.latex(colored_equation)
