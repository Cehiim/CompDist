// CalculatorClient.java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {

    public static void main(String[] args) {
        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("192.168.176.1");

            // Lookup the Calculator object
            Calculator stub = (Calculator) registry.lookup("Calculator");

            // Invoke remote methods
            Fracao a = new Fracao(1, 2); // Fração: 1/2
            Fracao b = new Fracao(3, 10); // Fração: 3/10

            System.out.println("Addition: " + stub.addF(a, b)); // Resultado: 8/10
            System.out.println("Subtraction: " + stub.subtractF(a, b)); // Resultado: 2/10
            System.out.println("Multiplication: " + stub.multiplyF(a, b)); // Resultado: 3/20
            System.out.println("Division: " + stub.divideF(a, b)); // Resultado: 10/6
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
