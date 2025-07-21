#  deployment.py
import os
import subprocess
import streamlit as st

# === Embedded requirements.txt ===
requirements = """
streamlit==1.35.0
web3==6.15.1
"""

# === Embedded .streamlit/config.toml ===
config_toml = """
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
"""

# === Embedded app.py ===
app_code = '''
import streamlit as st
from web3 import Web3

# --- MetaMask and WalletConnect HTML ---
wallet_html = """
<iframe src="wallet_connect.html" width="100%" height="200px" frameborder="0"></iframe>
"""

# --- Load ABI Files ---
import json
with open("BridgeL1_ABI.json") as f:
    l1_abi = json.load(f)
with open("BridgeL2_ABI.json") as f:
    l2_abi = json.load(f)

# --- RPC Connections ---
rpc_l1 = "http://localhost:8545"
rpc_l2 = "http://GBTNetwork:8545"
web3_l1 = Web3(Web3.HTTPProvider(rpc_l1))
web3_l2 = Web3(Web3.HTTPProvider(rpc_l2))

# --- Contract Addresses (replace these with your deployed addresses) ---
bridge_l1_address = Web3.to_checksum_address("0xYourL1BridgeAddress")
bridge_l2_address = Web3.to_checksum_address("0xYourL2BridgeAddress")

bridge_l1 = web3_l1.eth.contract(address=bridge_l1_address, abi=l1_abi)
bridge_l2 = web3_l2.eth.contract(address=bridge_l2_address, abi=l2_abi)

# --- UI ---
st.title("🌉 GBT Layer1 ↔ Layer2 Bridge")

st.markdown("### 💼 Connect Your Wallet")
st.components.v1.html(wallet_html, height=250)

st.markdown("---")
st.markdown("### 🔁 Bridge Action")

option = st.selectbox("Choose action", ["Deposit to Layer2", "Withdraw to Layer1"])

wallet = st.text_input("Your Wallet Address")
amount = st.number_input("Amount (GBT)", min_value=0.0, value=0.0)

if st.button("Submit"):
    if option == "Deposit to Layer2":
        st.success(f"Would call L1.depositToL2({wallet}, {amount})")
    else:
        st.success(f"Would call L2.withdrawToL1({wallet}, {amount})")

st.markdown("---")
st.markdown("### 🔍 View Balances (Mocked)")
st.write("Layer 1: 1000 GBT")
st.write("Layer 2: 500 GBT")
'''

# === Save All Files ===

# Write requirements.txt
with open("requirements.txt", "w") as f:
    f.write(requirements.strip())

# Write .streamlit/config.toml
os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/config.toml", "w") as f:
    f.write(config_toml.strip())

# Write app.py
with open("app.py", "w") as f:
    f.write(app_code.strip())

# Run the app automatically
subprocess.run(["streamlit", "run", "app.py"])
