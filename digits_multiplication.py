def checkio(number):
	res = 1
	if number != 0:
		for i in str(number).replace('0',''):
			res*=int(i)
		return res
	return 1
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1