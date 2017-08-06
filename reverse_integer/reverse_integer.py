def reverse_integer(x):
	y = 0
	sign = 1
	sign = -1 if x < 0 else 1
	x *= sign
	while 1:
		y = (y * 10 + x % 10)
		x /= 10
		if x == 0:
			return (y * sign)

print "Reverse of   12 = %s" % reverse_integer(12)
print "Reverse of -512 = %s" % reverse_integer(-512)
print "Reverse of    2 = %s" % reverse_integer(2)
