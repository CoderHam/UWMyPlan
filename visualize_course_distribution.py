import cPickle as pickle
from class_from_timing import find_classes_at_timings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv

num_c = []
c_sem = "AU 17"
daysofweek = ['M','T','W','Th','F','Sa']
for d in daysofweek:
    for h in range(0,24):
        for m in range(0,60,15):
            c_time=h*100+m
            cl = len(find_classes_at_timings(c_sem,d,c_time))
            cl_t = [d,c_time,cl]
            num_c.append(cl_t)
    print d
#
# pickle.dump(num_c,open("num_class_time.pkl","w"))
# num_c = pickle.load(open("num_class_time.pkl","r"))
#
with open("viz.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(num_c)

#Remember to add Day,Time and Classes label on csv header
pdn = pd.read_csv("viz.csv")
print pdn
result = pdn.pivot(index='Day', columns='Time', values='Classes')
result.index = pd.CategoricalIndex(result.index, categories= ['M','T','W','Th','F','Sa'])
result.sortlevel(level=0, ascending=False, inplace=True)
#
print result
sns.heatmap(result, xticklabels=4)

plt.show()
