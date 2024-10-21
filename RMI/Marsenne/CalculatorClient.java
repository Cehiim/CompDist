// CalculatorClient.java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {

    public static void main(String[] args) {
        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("192.168.0.8");

            // Lookup the Calculator object
            Calculator stub = (Calculator) registry.lookup("Calculator");

            // Invoke remote methods
            int a = 3; // Valor: 7
            int b = 5; // Valor: 11
            int c = 4; // Valor: 15
            int d = 11; // Valor: 2047

            System.out.println(String.format("Valor: %d - Eh numero de Mersenne primo? %b%n", a, stub.ehPrimo(a)));
            System.out.println(String.format("Valor: %d - Eh numero de Mersenne primo? %b%n", b, stub.ehPrimo(b)));
            System.out.println(String.format("Valor: %d - Eh numero de Mersenne primo? %b%n", c, stub.ehPrimo(c)));
            System.out.println(String.format("Valor: %d - Eh numero de Mersenne primo? %b%n", d, stub.ehPrimo(d)));
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}