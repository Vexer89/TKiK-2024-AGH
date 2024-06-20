public class TryCatchTest {
    public static void main() {
        try {
            int result = 10 / 0;
            System.out.println("Wynik: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Dzielenie przez zero!");
        } finally {
            System.out.println("Koniec programu");
        }
    }
}
