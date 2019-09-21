from django.test import TestCase

# Create your tests here.
from images2async import main

code_string = 'AAECAaoIAt6CA5ybAw7FA9sD/gPjBdAHpwiTCeKJA4yUA7WYA8aZA/SZA6+nA8qrAwA='
file_name = main(code_string)

print()
print()
print()
print(file_name)
print()
print()
print()

# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# TEMPLATE_PATH = os.path.join(BASE_DIR, "test.json")
# print(TEMPLATE_PATH)

# import json
# with open(TEMPLATE_PATH, 'rb') as f:
# 	data = json.load(f) #list of dicts
# 	ext = data[str(8)]
# 	print(ext)
