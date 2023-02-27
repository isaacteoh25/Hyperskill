import re

# r =to cancel the backslashes' special meaning in Python's syntax
regex = r'^[\w][\d]\d?[^\s\w]$'
regex = r'\w\d\d?[^\w\s]'
regex = r'[\w]\d{1,2}[^\w\s]$'
regex = r'^[a-zA-Z0-9]\d{1,}[^\w\s]$'