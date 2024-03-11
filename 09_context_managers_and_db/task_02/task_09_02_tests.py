import datetime
from task_09_02_load_data import salary_facts


subset = [x[3] for x in salary_facts
          if x[0] == 1 and x[2] == 'salary'
          and datetime.datetime.strptime(x[1], '%Y-%m-%d').year == 2020]
print(subset)
print(len(subset), sum(subset), sum(subset) / len(subset))
