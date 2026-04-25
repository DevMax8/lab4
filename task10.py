import os
import shutil
if not os.path.exists('backup'):
    os.mkdir('backup')
items = os.listdir()
for item in items:
    if os.path.isfile(item):
        shutil.copy(item, 'backup')