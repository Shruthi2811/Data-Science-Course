import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
auto=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2008.csv')
sns.set_style("darkgrid")
bar_plot=sns.barplot(x=auto["Month"],y=auto["DepDelay"],palette="muted")
plt.xticks(rotation=90)
for p in bar_plot.patches:
    height = p.get_height()
    bar_plot.text(p.get_x()+ p.get_width()/2, height+0.5, '%d' % int(height))
bar_plot.set(xlabel='Months',ylabel='Mean Delay(mins)')
plt.title('Monthwise Delay for 2008')
plt.show()