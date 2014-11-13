import numpy as np
import sys


def find_roots(a, b, c):
	x1 = (-b + np.sqrt(b*b - 4*a*c))/2*a
	x2 = (-b - np.sqrt(b*b - 4*a*c))/2*a
	return (x1, x2)


if __name__ == "__main__":
	a, b, c = sys.argv[1:4]
	roots = find_roots(int(a), int(b), int(c))
	print(roots)