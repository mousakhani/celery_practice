from proj.tasks import divide, add

r = add.delay(3, 4)
print(r.get())

r = divide.delay(100, 20)
print(r.get())


print('Finished')
