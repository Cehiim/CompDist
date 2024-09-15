import grpc
from concurrent import futures
import calc_pb2
import calc_pb2_grpc

class CalculatorServicer(calc_pb2_grpc.CalculatorServicer):
    def Mult(self, request, context):
        num = request.frac1.num * request.frac2.num
        den = request.frac1.den * request.frac2.den
        result.num=num
        result.den=den
        return calc_pb2.MultResponse(result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
