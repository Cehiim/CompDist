# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import calc_pb2 as calc__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in calc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CalculatorStub(object):
    """The calculator service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Mult = channel.unary_unary(
                '/calculator.Calculator/Mult',
                request_serializer=calc__pb2.MultRequest.SerializeToString,
                response_deserializer=calc__pb2.MultResponse.FromString,
                _registered_method=True)


class CalculatorServicer(object):
    """The calculator service definition.
    """

    def Mult(self, request, context):
        """Sends a SumRequest and receives a SumResponse.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Mult': grpc.unary_unary_rpc_method_handler(
                    servicer.Mult,
                    request_deserializer=calc__pb2.MultRequest.FromString,
                    response_serializer=calc__pb2.MultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('calculator.Calculator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """The calculator service definition.
    """

    @staticmethod
    def Mult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/calculator.Calculator/Mult',
            calc__pb2.MultRequest.SerializeToString,
            calc__pb2.MultResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
