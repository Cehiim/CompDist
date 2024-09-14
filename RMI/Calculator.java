// Calculator.java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
    // Method to add two numbers
    public double add(double a, double b) throws RemoteException;

    // Method to subtract two numbers
    public double subtract(double a, double b) throws RemoteException;

    // Method to multiply two numbers
    public double multiply(double a, double b) throws RemoteException;

    // Method to divide two numbers
    public double divide(double a, double b) throws RemoteException;

    public Fracao addF(Fracao a, Fracao b) throws RemoteException;

    // Method to subtract two numbers
    public Fracao subtractF(Fracao a, Fracao b) throws RemoteException;

    // Method to multiply two numbers
    public Fracao multiplyF(Fracao a, Fracao b) throws RemoteException;

    // Method to divide two numbers
    public Fracao divideF(Fracao a, Fracao b) throws RemoteException;
}
