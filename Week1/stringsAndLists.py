words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")
print words.replace("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2, 54,-2,7,12,98,"world"]
print y[0]
print y[7]

y = [y[0],y[7]]
print y

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
a = z[:len(z)/2]
b = z[len(z)/2:]
print a
print b
print z
z.append(a[0])
print z