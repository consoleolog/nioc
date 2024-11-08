import os
from os.path import dirname, join

print(join(dirname(f"{os.getcwd()}/upbit_trader"), '.env'))