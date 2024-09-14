public class Fracao
{
    public int numerador;
    public int denominador;

    public Fracao(int n, int d)
    {
        this.numerador = n;
        this.denominador = d;
    }

    private int mdc()
    {
        int a = numerador;
        int b = denominador;
        while(b != 0)
        {
            a = b;
            b = a%b;
        }
        return a;
    }

    public void Simplificar()
    {
        int divisor_comum = mdc();
        numerador /= divisor_comum;
        denominador /= divisor_comum;
    }
}
