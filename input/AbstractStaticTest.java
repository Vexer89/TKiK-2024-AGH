public class AbstractStaticTest {
    public static void main() {
        Shape.display();
        Shape myShape = new Circle();
        myShape.draw();
    }
}

abstract class Shape {
    abstract void draw(){
        System.out.println("Rysujemy kształt");
    }

    static void display() {
        System.out.println("Wyświetlamy kształty");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Rysujemy koło");
    }
}


