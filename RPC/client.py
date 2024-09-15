import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.ComplexCalculatorStub(channel)

number1 = "0.1 + 0.2i"
number2 = "4.5 - 3.6i"

# create a valid request message
request = calculator_pb2.ComplexNumberRequest( #Os números complexos ficam no formato a + bi
    number1= number1,
    number2= number2) #OBS: é importante colocar espaço em branco entre os números e os sinais

# make the call
response_soma = stub.Soma(request)
response_sub = stub.Subtracao(request)
response_mult = stub.Multiplicacao(request)
response_div = stub.Divisao(request)

# et voilà
print("Número 1: 0.1 + 0.2i")
print("Número 2: 4.5 - 3.6i")
print()
print("Operações:")
print("Soma:", response_soma)
print("Subtração:", response_sub)
print("multiplicação:", response_mult)
print("Divisão:", response_div)