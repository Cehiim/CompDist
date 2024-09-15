import grpc
from concurrent import futures
import time
# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
from calculator import *

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.ComplexCalculatorServicer):
    
    def Soma(self, request, context):
        resultado = soma(request.number1, request.number2)
        response = calculator_pb2.ComplexNumberReply(result= resultado)
        return response
    
    def Subtracao(self, request, context):
        resultado = subtracao(request.number1, request.number2)
        response = calculator_pb2.ComplexNumberReply(result= resultado)
        return response
    
    def Divisao(self, request, context):
        resultado = div(request.number1, request.number2)
        response = calculator_pb2.ComplexNumberReply(result= resultado)
        return response
    
    def Multiplicacao(self, request, context):
        resultado = mult(request.number1, request.number2)
        response = calculator_pb2.ComplexNumberReply(result= resultado)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calculator_pb2_grpc.add_ComplexCalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)