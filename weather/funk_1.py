import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import time

def weather(days, color):
    path = 'D:\\rabota\\university\\djangoProject1\\weather\\weather.csv'
    weather_data = pd.read_csv(path, index_col=0)
    weather_data.head()
    days = int(days)
    color = str(color)
    name_of_row = weather_data['MaxTemp'].values[:days]
    number_days = [i+1 for i in range(days)]

    sns.lineplot(x=number_days, y=name_of_row, color=color)
    ts = str(time.time()).replace('.', '_')
    image_path = f"images/weather_data_{ts}.png"
    plt.savefig(f'{image_path}')
    return image_path
