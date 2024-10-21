// CalculatorServer.java
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorServer implements Calculator {

    // Implement the add method
    public double add(double a, double b) throws RemoteException {
        return a + b;
    }

    // Implement the subtract method
    public double subtract(double a, double b) throws RemoteException {
        return a - b;
    }

    // Implement the multiply method
    public double multiply(double a, double b) throws RemoteException {
        return a * b;
    }

    // Implement the divide method
    public double divide(double a, double b) throws RemoteException {
        if (b == 0) throw new ArithmeticException("Division by zero");
        return a / b;
    }

    public NumeroComplexo addNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException
    {
        NumeroComplexo resposta;
        resposta = new NumeroComplexo(a.real+b.real, a.imaginario+b.imaginario);
        return resposta;
    }

    public NumeroComplexo subtractNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException
    {
        NumeroComplexo resposta;
        resposta = new NumeroComplexo(a.real-b.real, a.imaginario-b.imaginario);
        return resposta;
    }

    public NumeroComplexo multiplyNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException
    {
        NumeroComplexo resposta;
        float multi1 = a.real * b.real;
        float multi2 = (a.real*b.imaginario) + (a.imaginario*b.real);
        float multi3 = a.imaginario*b.imaginario;
        resposta = new NumeroComplexo(multi1-multi3, multi2);
        return resposta;
    }

    public NumeroComplexo divideNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException
    {
        NumeroComplexo conjugado;
        NumeroComplexo numerador;
        NumeroComplexo denominador;
        NumeroComplexo resposta;
        conjugado = new NumeroComplexo(b.real, b.imaginario*-1);
        numerador = multiplyNC(a, conjugado);
        denominador = multiplyNC(b, conjugado);
        resposta = new NumeroComplexo(numerador.real/denominador.real, numerador.imaginario/denominador.real);
        return resposta;
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
