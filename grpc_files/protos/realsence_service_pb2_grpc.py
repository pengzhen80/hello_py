# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import realsence_service_pb2 as realsence__service__pb2


class service_realsenceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OcrImage = channel.unary_unary(
                '/ocr.service_realsence/OcrImage',
                request_serializer=realsence__service__pb2.RequestImage.SerializeToString,
                response_deserializer=realsence__service__pb2.ReplyCharacters.FromString,
                )


class service_realsenceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OcrImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_service_realsenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OcrImage': grpc.unary_unary_rpc_method_handler(
                    servicer.OcrImage,
                    request_deserializer=realsence__service__pb2.RequestImage.FromString,
                    response_serializer=realsence__service__pb2.ReplyCharacters.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ocr.service_realsence', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class service_realsence(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OcrImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ocr.service_realsence/OcrImage',
            realsence__service__pb2.RequestImage.SerializeToString,
            realsence__service__pb2.ReplyCharacters.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
