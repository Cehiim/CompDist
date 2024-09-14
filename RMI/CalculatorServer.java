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

    private int mdc(int a, int b)
    {
        while(b != 0)
        {
            a = b;
            b = a%b;
        }
        return a;
    }

    private int mmc(int a, int b)
    {
        return a * (b / mdc(a, b));
    }

    public Fracao addF(Fracao a, Fracao b) throws RemoteException
    {
        Fracao resposta;
        if(a.denominador == b.denominador)
        {
            resposta = new Fracao(a.numerador+b.numerador, a.denominador);
        }
        else
        {
            int multiplo_comum = mmc(a.denominador, b.denominador);
            resposta = new Fracao(a.numerador+b.numerador, multiplo_comum);
        }
        return resposta;
    }

    public Fracao subtractF(Fracao a, Fracao b) throws RemoteException
    {
        Fracao resposta;
        if(a.denominador == b.denominador)
        {
            resposta = new Fracao(a.numerador-b.numerador, a.denominador);
        }
        else
        {
            int multiplo_comum = mmc(a.denominador, b.denominador);
            resposta = new Fracao(a.numerador-b.numerador, multiplo_comum);
        }
        return resposta;
    }

    public Fracao multiplyF(Fracao a, Fracao b) throws RemoteException
    {
        Fracao resposta;
        resposta = new Fracao(a.numerador*b.numerador, a.denominador*b.denominador);
        return resposta;
    }

    public Fracao divideF(Fracao a, Fracao b) throws RemoteException
    {
        Fracao resposta;
        resposta = new Fracao(a.numerador*b.denominador, a.denominador*b.numerador);
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
