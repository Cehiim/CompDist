import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorServer implements Calculator {

    // O valor é de Mersenne?
    public boolean ehMersenne(int n) throws RemoteException 
    {
        if (n <= 1) {
            return false;
        }
        int p = 1;
        while (Math.pow(2, p) - 1 < n) {
            p++;
        }
        return Math.pow(2, p) - 1 == n;
    }
    
    // Caso seja um primo de Mersenne
    public boolean ehPrimo(int n) throws RemoteException 
    {
        if (!ehMersenne(n)) 
        {
            return false;
        }
        // Check if n is prime
        for (int i = 2; i <= Math.sqrt(n); i++) 
        {
            if (n % i == 0) 
            {
                return false;
            }
        }
        return true;
    }
    

    public static void main(String[] args) {
        try {
            // Create and export the CalculatorServer object
            CalculatorServer server = new CalculatorServer();
            Calculator stub = (Calculator) UnicastRemoteObject.exportObject(server, 0);

            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.bind("Calculator", stub);

            System.out.println("CalculatorServer is running...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
