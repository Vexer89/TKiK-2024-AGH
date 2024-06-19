public class Test {
    private int a;
    private int metoda() {
        for (int i = 0; i < 10; i++) {
            a++;
            if (a == 5) {
                break;
            }
        }
        while (a < 10) {
            a++;
        }
        if (a == 10) {
            if (a == 10) {
                return 1;
            } else {
                return 0;
            }
            return 1;
        } else {
            return 0;
        }
    }
}