
import subprocess
import sys
# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# List of packages to install
packages = ["streamlit==1.36.0",]

# Install each package
for package in packages:
    install(package)
import streamlit as st
import WebAppForCustomerSegmentation as WebApp

#create the menu
st.sidebar.title('Menu')
Page_user = st.sidebar.selectbox(

'Choice',['Prediction for Customer Segmentation'] 
 
)

#change the pages
if Page_user == 'Prediction for Customer Segmentation':
    WebApp.code()
