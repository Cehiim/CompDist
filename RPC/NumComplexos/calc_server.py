import grpc
from concurrent import futures
import calc_pb2
import calc_pb2_grpc

class CalculatorServicer(calc_pb2_grpc.CalculatorServicer):
    def Mult(self, request, context):
        num_res = request.frac1.num * request.frac2.num
        den_res = request.frac1.den * request.frac2.den

        if (num_res % den_res == 0 or den_res % num_res == 0):
            mdc = CalculatorServicer.MDC(num_res, den_res)
            num_res /= mdc
            den_res /= mdc
            num_res = int(num_res)
            den_res = int(den_res)

        response = calc_pb2.Fraction(num= num_res, den= den_res)
        return calc_pb2.MultResponse(result= response)
    
    def MDC(a, b):
        while b != 0:
            a, b = b, a % b
        return a

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()