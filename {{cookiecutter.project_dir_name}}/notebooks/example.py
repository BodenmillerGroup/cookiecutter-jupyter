# %%
# %matplotlib notebook
# %load_ext autoreload
# %autoreload 2

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

from pathlib import Path

module_path = Path().absolute()
if str(module_path) not in sys.path:
    sys.path.append(module_path)
    
import utils
