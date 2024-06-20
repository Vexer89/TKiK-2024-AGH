public class InheritanceTest {
    public static void main() {
        Animal myDog = new Dog();
        myDog.sound();
    }
}

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

