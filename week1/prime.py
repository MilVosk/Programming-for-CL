def is_prime(n):
    if (n<=1):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2, n):
            if(n%i==0):
                return False
        return True

def is_twin_prime(i):
	if is_prime(i) and (is_prime(i + 2) or is_prime(i - 2)):
		return True
	return False

def twin_prime(j):
	if is_prime(j) and is_prime(j + 2):
		return (j, j + 2)
	elif is_prime(j) and is_prime(j - 2):
		return (j - 2, j)
	else:
		return 'not twin prime'
def twin_prime_range(x):
	b = [twin_prime(j) for j in range(x) if is_twin_prime(j)]
	return b
