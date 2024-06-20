class LogicalExpressionsTest:
	@staticmethod 
	def main():
		isRaining = True
		isSunny = False
		if (isRaining and isSunny):
			print("Możliwe, że będzie tęcza.")
		elif (isRaining or isSunny):
			print("Jedna z tych rzeczy się dzieje.")
		else :
			print("Nie pada i nie świeci słońce.")
		a = 5
		b = 10
		if (a < 10 and b > 5):
			print("a jest mniejsze niż 10 i b jest większe niż 5")
		if (a > 0 or b < 0):
			print("a jest większe niż 0 lub b jest mniejsze niż 0")
		if (not (a == b)):
			print("a i b są różne")
		else :
			print("a i b są równe")
LogicalExpressionsTest.main()
