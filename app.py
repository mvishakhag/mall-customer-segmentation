import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

st.set_page_config(page_title="Mall Customer Segmentation", layout="centered")
st.title("🛍️ Mall Customer Segmentation using KMeans")
st.markdown("Segment customers by **Annual Income** and **Spending Score**")

# Load dataset
df = pd.read_csv("mall_data.csv")

# Select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Sidebar - number of clusters
k = st.sidebar.slider("Select number of clusters", 2, 10, 5)

# Train model
kmeans = KMeans(n_clusters=k, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Plot clusters
st.subheader("📊 Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', 
                hue='Cluster', data=df, palette='tab10', ax=ax)
plt.title("Customer Segments")
st.pyplot(fig)

# Show cluster centers
st.subheader("📍 Cluster Centers")
centers = pd.DataFrame(kmeans.cluster_centers_, columns=X.columns)
st.dataframe(centers.round(2))

# Optional: Predict new customer segment
st.sidebar.subheader("🔍 Predict New Customer Segment")
income = st.sidebar.number_input("Annual Income (k$)", 0, 150, 50)
spending = st.sidebar.number_input("Spending Score (1-100)", 0, 100, 50)

if st.sidebar.button("Predict Cluster"):
    cluster = kmeans.predict([[income, spending]])[0]
    st.sidebar.success(f"Predicted Cluster: {cluster}")
