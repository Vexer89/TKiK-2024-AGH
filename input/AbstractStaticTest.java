public class AbstractStaticTest {

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
}

