public class InterfaceTest {
    public static void main() {
        Animal myCat = new Cat();
        myCat.sound();
    }
}

interface Animal {
    public void sound(){
        System.out.println("Zwierzę wydaje dźwięk");
   }
}

class Cat implements Animal {
    public void sound() {
        System.out.println("Kot miauczy");
    }
}


