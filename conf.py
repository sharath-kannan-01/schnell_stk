"""
Code Documentation for API Configuration

This script includes configurations for making API requests, specifying the API endpoint,
headers, and authentication data. Additionally, it defines a base URL for image paths in a production environment.

Author: Your Name
Date: Date of creation/modification
"""

# API endpoint URL
url = 'https://schnelliot.in/api'
# Alternative API endpoint URL (commented out)
# url = 'https://iotpro.io/api'

# Headers for API requests
header = {'content-type': 'application/json'}

# Authentication data for API requests
data = {'username': 'device_migration@sl.schnelliot.in', 'password': '$2@rt&Ten@1'}

# Additional authentication data for lamp-related requests (commented out)
# data = {'username': 'mohith.v@sl2.qa.iotpro', 'password': 'schnell123'}

# Base URL for image paths in a production environment
pic_base_url_prod = "https://schnell-s3-image.s3.ap-south-1.amazonaws.com/luminator/"
# pic_base_url_prod = "https://luminator-iotpro.s3.us-east-1.amazonaws.com/luminator/"


"helo"