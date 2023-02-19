import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

triples=pd.read_csv("./dataset.csv")

# Need to find a good way to visualize
# Also more data variations, along with negative
# instances to make the data more interesting!

#sns.catplot(data=triples,kind='swarm', x='mew',y='total',hue='lam')
sns.relplot(
        alpha=.5, palette="muted",
       height=5, data=triples)
plt.savefig("Example-2.jpg")


sns.set_theme(style="ticks")
sns.pairplot(triples,hue="risk-assesment")