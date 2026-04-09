import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Factory Optimization", layout="wide")

st.title("🍭 Factory Reallocation & Shipping Optimization Dashboard")

# Factory Coordinates
factories = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.11914, -96.18115),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.1175, -89.971107)
}

# Sample Data (so app runs without dataset)
data = {
    "Product Name": ["Laffy Taffy", "Nerds", "Wonka Bar - Milk Chocolate"],
    "Region": ["West", "East", "Central"],
    "Ship Mode": ["Standard", "Express", "Standard"]
}
df = pd.DataFrame(data)

# Sidebar
st.sidebar.header("Filters")

product = st.sidebar.selectbox("Select Product", df["Product Name"])
region = st.sidebar.selectbox("Select Region", df["Region"])
ship_mode = st.sidebar.selectbox("Ship Mode", df["Ship Mode"])

priority = st.sidebar.slider("Optimization Priority (Speed vs Profit)", 0, 100, 50)

# Fake prediction function (for demo)
def predict_lead_time(distance):
    return distance / 600 + np.random.uniform(0.5, 2)

# Run Optimization
if st.button("🚀 Run Optimization"):

    results = []

    for factory, coords in factories.items():
        distance = np.random.randint(200, 3000)
        lead_time = predict_lead_time(distance)

        results.append({
            "Factory": factory,
            "Distance (km)": distance,
            "Predicted Lead Time": round(lead_time, 2)
        })

    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values(by="Predicted Lead Time")

    # KPIs
    st.subheader("📊 Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Lead Time Reduction", "25%")
    col2.metric("Profit Impact", "+10%")
    col3.metric("Confidence Score", "High")

    # Table
    st.subheader("🏭 Factory Comparison")
    st.dataframe(result_df)

    # Best Factory
    best = result_df.iloc[0]
    st.success(f"✅ Recommended Factory: {best['Factory']}")

    # Chart
    st.subheader("📉 Lead Time Comparison")
    st.bar_chart(result_df.set_index("Factory")["Predicted Lead Time"])