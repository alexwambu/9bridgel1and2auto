#!/bin/bash

echo "🔧 Setting up GBT Streamlit App Environment..."

# Step 1: Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip
pip install --upgrade pip

# Step 3: Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Step 4: Launch the Streamlit app
echo "🚀 Launching the app..."
streamlit run app.py
