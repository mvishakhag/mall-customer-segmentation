# mall-customer-segmentation
# 🛍️ Mall Customer Segmentation - KMeans Clustering App

This is a Streamlit web app that performs **customer segmentation** using **KMeans clustering** on a mall dataset. It visually groups customers based on their **Annual Income** and **Spending Score**, helping businesses understand customer behavior and target them effectively.

---

## 🌐 Live App

👉 [Click here to open the app](https://mall-customer-segmentation-cvcebmgwdm3k6jtubuuygi.streamlit.app/)

---

## 📌 Features

- 📊 Interactive cluster visualization using KMeans
- 🎯 Choose number of clusters with a slider
- 🔍 Predict segment for a new customer
- 🧮 Shows cluster centers
- 📁 Simple UI built using Streamlit

---

## 📁 Folder Structure

kmean/
├── app.py # Streamlit app file
├── mall_data.csv # Dataset file
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)

yaml
Copy
Edit

---

## 🚀 How to Run Locally

### 1. Clone this repository or download the folder
```bash
git clone <your-repo-url>
cd kmean
2. Install required libraries
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
📊 Dataset
The dataset contains mall customer information with the following columns:

CustomerID

Gender

Age

Annual Income (k$)

Spending Score (1-100)

Only Annual Income and Spending Score are used for clustering in this app.

💡 Example Use Case
Marketers and mall management teams can use this app to:

Identify high spenders

Understand spending patterns across income levels

Design targeted campaigns

🛠 Technologies Used
Python

Streamlit

Pandas

Matplotlib

Seaborn

Scikit-learn

📬 Contact
Made with ❤️ by Vishakha Mishra
