def are_collinear(x1, y1, x2, y2, x3, y3, eps=1e-9):
	"""Return True if the three points are collinear (area == 0 within eps)."""
	area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
	return abs(area) < eps


def main():
	print("Enter coordinates for three points (numbers).")
	try:
		x1 = float(input("x1: "))
		y1 = float(input("y1: "))
		x2 = float(input("x2: "))
		y2 = float(input("y2: "))
		x3 = float(input("x3: "))
		y3 = float(input("y3: "))
	except ValueError:
		print("Invalid input — please enter numeric values.")
		return

	if are_collinear(x1, y1, x2, y2, x3, y3):
		print("The points are collinear (lie on a straight line).")
	else:
		print("The points are not collinear.")


if __name__ == "__main__":
	main()

