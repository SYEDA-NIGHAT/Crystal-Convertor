# import streamlit as st # type:ignore

# # Apply Custom CSS for Better Styling
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #1e1e1e;
#         color: #e0e0e0;
#     }
#     .stButton>button {
#         background-color: #6c5ce7;
#         color: white;
#         border-radius: 10px;
#         padding: 10px;
#         font-weight: bold;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #5a4fcf;
#         transform: scale(1.05);
#     }
#     .stSelectbox label, .stNumberInput label {
#         color: #ffffff !important;
#         font-weight: bold;
#         font-size: 16px;
#     }
#     .stSelectbox, .stNumberInput {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Conversion factors
# conversion_factors = {
#     "Length": {
#         "Meters to Kilometers": 0.001,
#         "Kilometers to Meters": 1000,
#         "Feet to Meters": 0.3048,
#         "Meters to Feet": 3.28084
#     },
#     "Weight": {
#         "Kilograms to Grams": 1000,
#         "Grams to Kilograms": 0.001,
#         "Pounds to Kilograms": 0.453592,
#         "Kilograms to Pounds": 2.20462
#     },
#     "Temperature": {
#         "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
#         "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
#     }
# }

# st.title("🌟 Unit Converter")

# # Select category
# category = st.selectbox("✏️ Choose a category:", list(conversion_factors.keys()))

# # Select conversion type
# conversion_type = st.selectbox("🔄 Choose conversion:", list(conversion_factors[category].keys()))

# # Input value
# value = st.number_input("🔢 Enter value to convert:", format="%.4f")

# # Convert Button
# if st.button("🚀 Convert"):
#     conversion = conversion_factors[category][conversion_type]
    
#     if callable(conversion):
#         result = conversion(value)
#     else:
#         result = value * conversion
    
#     st.success(f"✅ Converted value: {result:.4f}")


# import streamlit as st

# # Apply Custom CSS for Crystal/Glassmorphism Styling
# st.markdown(
#     """
#     <style>
#     /* Background */
#     .stApp {
#         background: linear-gradient(135deg, #1a1a2e, #16213e);
#         color: #ffffff;
#         font-family: 'Poppins', sans-serif;
#     }
    
#     /* Glassmorphism Effect */
#     .glass-box {
#         background: rgba(255, 255, 255, 0.1);
#         border-radius: 15px;
#         padding: 20px;
#         backdrop-filter: blur(10px);
#         -webkit-backdrop-filter: blur(10px);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
#     }
    
#     /* Dropdown & Input Fields */
#     .stSelectbox, .stNumberInput {
#         background: rgba(255, 255, 255, 0.2) !important;
#         color: white !important;
#         border-radius: 8px;
#     }

#     /* Labels */
#     .stSelectbox label, .stNumberInput label {
#         color: #ffffff !important;
#         font-weight: bold;
#         font-size: 16px;
#     }
    
#     /* Convert Button */
#     .stButton>button {
#         background: linear-gradient(135deg, #ff9a9e, #fad0c4);
#         color: black;
#         border-radius: 10px;
#         padding: 10px;
#         font-weight: bold;
#         transition: all 0.3s ease-in-out;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
#     }
#     .stButton>button:hover {
#         transform: scale(1.05);
#         box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Conversion factors
# conversion_factors = {
#     "Length": {
#         "Meters to Kilometers": 0.001,
#         "Kilometers to Meters": 1000,
#         "Feet to Meters": 0.3048,
#         "Meters to Feet": 3.28084
#     },
#     "Weight": {
#         "Kilograms to Grams": 1000,
#         "Grams to Kilograms": 0.001,
#         "Pounds to Kilograms": 0.453592,
#         "Kilograms to Pounds": 2.20462
#     },
#     "Temperature": {
#         "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
#         "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
#     }
# }

# # Title with Aesthetic Emoji
# st.markdown('<h1 style="text-align:center;">🌟 Crystal Unit Converter</h1>', unsafe_allow_html=True)

# # Centered Glass Box
# st.markdown('<div class="glass-box">', unsafe_allow_html=True)

# # Select category
# category = st.selectbox("✏️ Choose a category:", list(conversion_factors.keys()))

# # Select conversion type
# conversion_type = st.selectbox("🔄 Choose conversion:", list(conversion_factors[category].keys()))

# # Input value
# value = st.number_input("🔢 Enter value to convert:", format="%.4f")

# # Convert Button
# if st.button("🚀 Convert"):
#     conversion = conversion_factors[category][conversion_type]
    
#     if callable(conversion):
#         result = conversion(value)
#     else:
#         result = value * conversion
    
#     st.success(f"✅ Converted value: {result:.4f}")

# # End Glass Box
# st.markdown('</div>', unsafe_allow_html=True)



import streamlit as st

# Apply Custom CSS for Crystal/Glassmorphism Styling
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Glassmorphism Effect */
    .glass-box {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }

    /* Dropdown & Input Fields */
    .stSelectbox, .stNumberInput {
        background: rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Labels */
    .stSelectbox label, .stNumberInput label {
        color: #ffffff !important;
        font-weight: bold;
        font-size: 16px;
    }
    
    /* Convert Button */
    .stButton>button {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
        color: white;
        border-radius: 12px;
        padding: 12px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conversion factors
conversion_factors = {
    "Length": {
        "Meters to Kilometers": 0.001,
        "Kilometers to Meters": 1000,
        "Feet to Meters": 0.3048,
        "Meters to Feet": 3.28084
    },
    "Weight": {
        "Kilograms to Grams": 1000,
        "Grams to Kilograms": 0.001,
        "Pounds to Kilograms": 0.453592,
        "Kilograms to Pounds": 2.20462
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
    }
}

# Title with Aesthetic Emoji
st.markdown('<h1 style="text-align:center;">🌟 Crystal Unit Converter</h1>', unsafe_allow_html=True)

# Centered Glass Box
# st.markdown('<div class="glass-box">', unsafe_allow_html=True)

# Select category
category = st.selectbox("✏️ Choose a category:", list(conversion_factors.keys()))

# Select conversion type
conversion_type = st.selectbox("🔄 Choose conversion:", list(conversion_factors[category].keys()))

# Input value
value = st.number_input("🔢 Enter value to convert:", format="%.4f")

# Convert Button
if st.button("🚀 Convert"):
    conversion = conversion_factors[category][conversion_type]
    
    if callable(conversion):
        result = conversion(value)
    else:
        result = value * conversion
    
    st.success(f"✅ Converted value: {result:.4f}")

# End Glass Box
st.markdown('</div>', unsafe_allow_html=True)
