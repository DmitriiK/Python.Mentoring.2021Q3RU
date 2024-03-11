from task_08_01 import myzip

mz = myzip(['A', 'B', 'C'], [1, 2, 3])
print(list(mz))

print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3))))
