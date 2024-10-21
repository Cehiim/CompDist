// Calculator.java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
    
    public boolean ehMersenne(int n) throws RemoteException;

    public boolean ehPrimo(int n) throws RemoteException;
}