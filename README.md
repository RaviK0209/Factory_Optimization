# 🍭 Factory Reallocation & Shipping Optimization System

## 🌐 Live Demo

👉 [Click Here to View Dashboard](https://factoryoptimization-xuk5yd4ndtvxhpdcfo7n4u.streamlit.app/)

## 📌 Overview

This project presents an intelligent decision-support system for optimizing factory-product allocation for Nassau Candy Distributor. It replaces static assignment logic with a data-driven approach using predictive analytics and scenario simulation.

---

## 🚀 Problem Statement

Nassau Candy Distributor currently uses fixed rules to assign products to factories, leading to:

* High shipping lead times
* Increased logistics costs
* Reduced profitability

The goal is to:

* Predict shipping performance
* Simulate alternative factory assignments
* Recommend optimal configurations

---

## 🧠 Solution Approach

### 1. Data Processing

* Cleaned and preprocessed dataset
* Created new features:

  * Lead Time
  * Profit Margin
  * Distance (simulated)
* Encoded categorical variables

---

### 2. Predictive Modeling

* Built models to predict shipping lead time
* Models considered:

  * Linear Regression
  * Random Forest
  * Gradient Boosting

---

### 3. Scenario Simulation

* Simulated assigning products to different factories
* Calculated predicted lead times
* Compared performance across factories

---

### 4. Optimization Logic

* Ranked factories based on:

  * Lead time reduction
  * Profit stability
  * Risk

---

## 📊 Dashboard Features

### 🔹 Factory Optimization Simulator

* Select product, region, ship mode
* Compare factory performance

### 🔹 What-If Analysis

* Evaluate alternative assignments

### 🔹 Recommendation System

* Displays best factory options

### 🔹 KPI Panel

* Lead Time Reduction
* Profit Impact
* Confidence Score

---

## 🖥️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn

---


---

## 📂 Project Structure

```
factory-optimization/
│
├── app.py
├── requirements.txt
├── research_paper.pdf
└── README.md
```

---

## 📈 Key Outcomes

* Improved decision-making using data
* Reduced shipping inefficiencies
* Provided scalable optimization framework

---



---

## 👤 Author

Ravikant Kumar

---

## ⭐ Conclusion

This project demonstrates how predictive analytics and optimization can transform logistics operations from static decision-making to intelligent, dynamic systems.
