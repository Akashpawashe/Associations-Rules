import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt

movies = []
with open("D:\\excelR\\Data science notes\\association rules\\asgmnt\\my_movies.csv") as f:
    movies= f.read()

movies =movies.split("\n")
movies_list=[]
for i in movies:
    movies_list.append(i.split(","))
    
all_movies_list = [i for item in movies_list for i in item]
from collections import Counter

item_frequencies = Counter(all_movies_list)

item_frequencies = sorted(item_frequencies.items(),key = lambda x:x[1])

frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

plt.bar(height = frequencies[0:11],x = list(range(0,11)),color='rgbkymc');plt.xticks(list(range(0,11),),items[0:11]);plt.xlabel("items")
plt.ylabel("Count")

movies_series  = pd.DataFrame(pd.Series(movies_list))
movies_series = movies_series.iloc[:9835,:] # removing the last empty transaction

movies_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = movies_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')

frequent_itemsets = apriori(X, min_support=0.005, max_len=3,use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets');plt.ylabel('support')


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head(20)
rules.sort_values('lift',ascending = False,inplace=True)


########################## To eliminate Redudancy in Rules #################################### 
def to_list(i):
    return (sorted(list(i)))


ma_X = rules.antecedents.apply(to_list)+rules.consequents.apply(to_list)


ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
index_rules = []
for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))


# getting rules without any redudancy 
rules_no_redudancy  = rules.iloc[index_rules,:]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift',ascending=False).head(10)


