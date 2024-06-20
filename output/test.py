class TryCatchTest:
	@staticmethod 
	def main(self, ):
		a = 10
		try:
			if (a == 10):
				raise Exception();
			else :
				print("a nie jest równe 10")
		except Exception:
			print("a jest równe 10")
		finally:
			print("Koniec programu")
