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

    public NumeroComplexo addNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException;

    // Method to subtract two numbers
    public NumeroComplexo subtractNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException;

    // Method to multiply two numbers
    public NumeroComplexo multiplyNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException;

    // Method to divide two numbers
    public NumeroComplexo divideNC(NumeroComplexo a, NumeroComplexo b) throws RemoteException;
}
