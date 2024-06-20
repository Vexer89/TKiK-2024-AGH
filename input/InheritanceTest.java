public class InheritanceTest {
    class Animal {
        void sound() {
            System.out.println("Zwierzę wydaje dźwięk");
        }
    }

    class Dog extends Animal {
        void sound() {
            System.out.println("Pies szczeka");
        }
    }
}



