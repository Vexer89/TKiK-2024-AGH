public class TryCatchTest {
    public static void main() {
        int a = 10;
        try {
            if(a == 10) {
                throw new Exception();
            } else {
                System.out.println("a nie jest równe 10");
            }

        } catch (Exception e) {
            System.out.println("a jest równe 10");
        } finally {
            System.out.println("Koniec programu");
        }
    }
}
