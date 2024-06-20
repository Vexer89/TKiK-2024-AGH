from abc import ABC,abstractmethod 
class AbstractStaticTest:
	def main(self, ):
		Shape.display()
		myShape = Circle()
		myShape.draw()
class Shape(ABC):
	@abstractmethod 
	def draw(self, ):
		print("Rysujemy kształt")
	def display(self, ):
		print("Wyświetlamy kształty")
class Circle(Shape):
	def draw(self, ):
		print("Rysujemy koło")
