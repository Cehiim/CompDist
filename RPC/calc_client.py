import grpc
import calc_pb2
import calc_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50054') as channel:
		stub = calc_pb2_grpc.CalculatorStub(channel)
		frac1 = Fraction(1,2)
		frac2 = Fraction(2,3)
		response = stub.Mult(calc_pb2.MultRequest(frac1, frac2))
		print("Mult result:", response.result)

if __name__ == '__main__':
	run()
