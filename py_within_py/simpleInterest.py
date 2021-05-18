import read

p = read.principal()
r = read.rate()
t = read.time_accrued()

s = (p * r * t)/100

print(s)