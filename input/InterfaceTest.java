public class InterfaceTest {
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
}




