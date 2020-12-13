# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import support_pb2 as support__pb2


class customerSupportStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.userSupport = channel.unary_unary(
                '/customerSupport/userSupport',
                request_serializer=support__pb2.userQuery.SerializeToString,
                response_deserializer=support__pb2.systemResponse.FromString,
                )


class customerSupportServicer(object):
    """Missing associated documentation comment in .proto file."""

    def userSupport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_customerSupportServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'userSupport': grpc.unary_unary_rpc_method_handler(
                    servicer.userSupport,
                    request_deserializer=support__pb2.userQuery.FromString,
                    response_serializer=support__pb2.systemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customerSupport', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class customerSupport(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def userSupport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customerSupport/userSupport',
            support__pb2.userQuery.SerializeToString,
            support__pb2.systemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)