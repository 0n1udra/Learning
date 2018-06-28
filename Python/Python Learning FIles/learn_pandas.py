import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

webStats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 56, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]
             }

df_webStats = pd.DataFrame(webStats)
print(df_webStats)

