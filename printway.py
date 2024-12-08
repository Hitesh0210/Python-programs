# print function -
x,y,z=10,20,20
print(x,y,z,sep=",") # Sep it is used for the separator.
id = 1
name = "hitesh"
salary = 38898.89
print("id=%d,name=%s,salary=%.2f" % (id,name,salary))
# print("id=%d,name=%-15s,salary=%.2f" % (id,name,salary))
print('id={},name={},salary={}'.format(id,name,salary))
print('id={:5d},name={:15s},salary={:10.2f}'.format(id,name,salary))

# {}- python place holder
# {{}} - jango place holder

