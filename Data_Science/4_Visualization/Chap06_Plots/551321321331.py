import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

tips = sns.load_dataset("tips")
#sns.lmplot(x="total_bill", y="tip",#  data=tips)
sns.lmplot(x="size", y="tip", data=tips, x_jitter=.15, ci=None)
#sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean, ci=None)
plt.show()