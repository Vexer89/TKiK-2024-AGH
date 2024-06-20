public class LogicalExpressionsTest {
    public static void main() {
        boolean isRaining = true;
        boolean isSunny = false;

        if (isRaining && isSunny) {
            System.out.println("Możliwe, że będzie tęcza.");
        } else if (isRaining || isSunny) {
            System.out.println("Jedna z tych rzeczy się dzieje.");
        } else {
            System.out.println("Nie pada i nie świeci słońce.");
        }

        int a = 5;
        int b = 10;
        if (a < 10 && b > 5) {
            System.out.println("a jest mniejsze niż 10 i b jest większe niż 5");
        }
        if (a > 0 || b < 0) {
            System.out.println("a jest większe niż 0 lub b jest mniejsze niż 0");
        }
        if (!(a == b)) {
            System.out.println("a i b są różne");
        } else {
        System.out.println("a i b są równe");
        }
    }
}
