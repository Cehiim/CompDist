// CalculatorClient.java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {

    public static void main(String[] args) {
        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("localhost");

            // Lookup the Calculator object
            Calculator stub = (Calculator) registry.lookup("Calculator");

            // Invoke remote methods
            Fracao a = new Fracao(1, 2);
            Fracao b = new Fracao(5, 7);

            System.out.println("Addition: " + stub.addF(a, b));
            System.out.println("Subtraction: " + stub.subtractF(a, b));
            System.out.println("Multiplication: " + stub.multiplyF(a, b));
            System.out.println("Division: " + stub.divideF(a, b));
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}