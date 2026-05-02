# Copy and back up files using shutil
import shutil
shutil.copy('sample.txt', 'better_sample.txt')

# Delete files safely
import os
if os.path.exists('sample1.txt'):
    os.remove('sample1.txt')