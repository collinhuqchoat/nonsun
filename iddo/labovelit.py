import sys
from pathlib import Path

# Assuming the script is invoked as: python script.py /path/to/file
infile = Path(sys.argv[1]).resolve()

# Now 'infile' contains the resolved absolute path of the file provided as a command-line argument
print(infile)
