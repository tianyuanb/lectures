import sqlite3, pandas as pd
from matplotlib import pyplot as plt

con = sqlite3.connect("atus.sqlite")

with open("ex/direct_engagement.sql") as f:
  query = f.read()

df = pd.read_sql_query(query, con)
ax = df.boxplot("Direct Engagement", "Parental Education")

plt.suptitle("")
ax.set(title = "", ylim = (0, 7),
       xlabel = "Parental Education [Years]", 
       ylabel = "Direct Engagement [Hours]")
ax.get_figure().savefig("engagement.pdf", bbox_inches='tight')
