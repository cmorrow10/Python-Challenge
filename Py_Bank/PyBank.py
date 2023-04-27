#!/usr/bin/env python
# coding: utf-8

# In[36]:


import csv


# In[ ]:


file = open('budget_data.csv')

type(file)


# In[38]:


csvreader = csv.reader(file)


# In[39]:


csvreader = csv.reader(file, delimiter=',')
csvheader = next(csvreader)

total_months = 0
total = 0
second_row = 0
first_row = 0
month_change = 0
total_month_change = []
date = []


# In[40]:


for row in csvreader:

    total_months += 1
first_row = int(row[1])
total += int(row[1])


# In[41]:


if (total_months==1):
    second_row = first_row


# In[42]:


month_change = first_row - second_row
date.append(row[0])
total_month_change.append(month_change)
second_row = first_row
average = round(sum(total_month_change)/(total_months - 1), 2)


# In[43]:


greatest_increase = max(total_month_change)
greatest_decrease = min(total_month_change)
increase_date = date[total_month_change.index(greatest_increase)]
decrease_date = date[total_month_change.index(greatest_decrease)]


# In[ ]:


print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {increase_date}(${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date}(${greatest_decrease})")

