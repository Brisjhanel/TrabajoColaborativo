import java.util.Scanner;

public class primo {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int numero;
        boolean esPrimo = true;

        System.out.print("Ingrese un numero: ");
        numero = sc.nextInt();

        if (numero <= 1) {
            esPrimo = false;
        } else {
            for (int i = 2; i < numero; i++) {
                if (numero % i == 0) {
                    esPrimo = false;
                    break;
                }
            }
        }

        if (esPrimo) {
            System.out.println("El numero es primo");
        } else {
            System.out.println("El numero no es primo");
        }
    }
}