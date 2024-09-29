// CalculatorClient.java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {

    public static void main(String[] args) {
        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("172.19.48.1");

            // Lookup the Calculator object
            Calculator stub = (Calculator) registry.lookup("Calculator");

            // Invoke remote methods
            NumeroComplexo a = new NumeroComplexo(4, 8); // 4 + 8i
            NumeroComplexo b = new NumeroComplexo(3, 2); // 3 + 2i

            System.out.println("Addition: " + stub.addNC(a, b)); // Resultado: 7 + 10i
            System.out.println("Subtraction: " + stub.subtractNC(a, b)); // Resultado: 1 + 6i
            System.out.println("Multiplication: " + stub.multiplyNC(a, b)); // Resultado: 12 + 32i + (16 * -1) = -4 + 32i
            System.out.println("Division: " + stub.divideNC(a, b)); // Resultado: (28/13) + (16/13)i
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
