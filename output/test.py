from abc import ABC 
class InterfaceTest:
	class Animal(ABC):
		def sound(self, ):
			print("Zwierzę wydaje dźwięk")
	class Cat(Animal):
		def sound(self, ):
			print("Kot miauczy")
