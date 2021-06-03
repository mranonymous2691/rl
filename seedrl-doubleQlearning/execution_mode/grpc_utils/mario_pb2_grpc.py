# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mario_pb2 as mario__pb2


class GRPCMarioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_action = channel.unary_unary(
                '/mario.GRPCMario/get_action',
                request_serializer=mario__pb2.Request.SerializeToString,
                response_deserializer=mario__pb2.Response.FromString,
                )


class GRPCMarioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_action(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCMarioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_action': grpc.unary_unary_rpc_method_handler(
                    servicer.get_action,
                    request_deserializer=mario__pb2.Request.FromString,
                    response_serializer=mario__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mario.GRPCMario', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GRPCMario(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_action(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mario.GRPCMario/get_action',
            mario__pb2.Request.SerializeToString,
            mario__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
