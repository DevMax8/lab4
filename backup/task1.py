import os
os.mkdir('lab_data')
if os.path.exists('lab_data'):
    print("lab_data directory already exists")
path = os.path.join('lab_data', 'logs')
os.mkdir(path)
print("subfolder created")
#version2
#version1 -- > main.py