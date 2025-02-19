"""
Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,

“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]
"""

import re

def tokenize_text(text):
    pattern = r'\b\w+\b|[\d,./]+|@\w+|https?://\S+|[\w.-]+@\w+\.\w+'
    tokens = re.findall(pattern, text)
    print("Tokens:", tokens)

def tokenizer_menu():
    text = input("Enter text: ")
    tokenize_text(text)

tokenizer_menu()
