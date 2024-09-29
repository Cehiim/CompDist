import java.io.Serializable;

public class NumeroComplexo implements Serializable
{
    private static final long serialVersionUID = 1L;
    public float real;
    public float imaginario;

    public NumeroComplexo(float real, float imaginario)
    {
        this.real = real;
        this.imaginario = imaginario;
    }

    @Override
    public String toString() 
    {
        return String.format("%.2f + %.2fi", real, imaginario);
    }
}
