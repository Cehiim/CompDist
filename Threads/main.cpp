#include <iostream>
#include <thread>
#include <mutex>

class Conta
{
    public:
        float saldo;
        
        Conta(float valor) : saldo(valor) {}
        
        void imprimir()
        {
            std::cout << "Saldo: " << saldo << std::endl;
        }
        
        void depositos(float valor, int n)
        {
            for(int i=0; i<n; i++)
            {
                saldo+=valor;
            }
            std::cout << "Saldo após depósito: " << saldo << std::endl;
        }
        
        void saques(float valor, int n)
        {
            for(int i=0; i<n; i++)
            {
                if(saldo<valor)
                {
                    std::cout << "Saldo insuficiente." << std::endl;
                    return;
                }
                else
                {
                    saldo-=valor;
                }
            }
            std::cout << "Saldo após saque: " << saldo << std::endl;
        }
};


class ContaMutex
{
    public:
        float saldo;
        std::mutex bloqueio;
        
        ContaMutex(float valor) : saldo(valor) {}
        
        void imprimir()
        {
            std::cout << "Saldo: " << saldo << std::endl;
        }
        
        void depositos(float valor, int n)
        {
            for(int i=0; i<n; i++)
            {
                bloqueio.lock();
                saldo += valor;
                bloqueio.unlock();
            }
            std::cout << "Saldo após depósito: " << saldo << std::endl;
        }
        
        void saques(float valor, int n)
        {
            for(int i=0; i<n; i++)
            {
                bloqueio.lock();
                if(saldo < valor)
                {
                    std::cout << "Saldo insuficiente." << std::endl;
                    break;
                }
                else
                {
                    saldo -= valor;
                }
                bloqueio.unlock();
            }
            std::cout << "Saldo após saque: " << saldo << std::endl;
        }
};


int main() {
    
    // Sem threads
    std::cout << "Conta sem threads\n";
    Conta c(1000);
    c.imprimir();
    c.depositos(5.0, 100000);
    c.saques(2.0, 100000);
    c.imprimir();
    

    //Com threads
    std::cout << "\n\nConta com threads\n";
    Conta c2(1000);
    c2.imprimir();
    std::thread t3(&Conta::depositos, &c2, 5.0, 100000);
    std::thread t4(&Conta::saques, &c2, 2.0, 100000);
    t3.join();
    t4.join();
    c2.imprimir();

    
    //Com mutex
    std::cout << "\n\nConta com mutex\n";
    ContaMutex cm(1000);
    cm.imprimir();
    std::thread t5(&ContaMutex::depositos, &cm, 5.0, 100000);
    std::thread t6(&ContaMutex::saques, &cm, 2.0, 100000);
    t5.join();
    t6.join();
    cm.imprimir();
    
    return 0;
}
