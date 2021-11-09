from concurrent import futures
import logging

import grpc

import realsence_service_pb2
import realsence_service_pb2_grpc

import ocr_manager
import sys

class RealSence_Service(realsence_service_pb2_grpc.service_realsence):

    def OcrImage(self, request, context):
        print(sys.getsizeof(request))
        #print(request)
        myimage = ocr_manager.MyImage(request.width,request.height,request.image_data)
        print(sys.getsizeof(myimage.image_data))
        #print(myimage.image_data)
        symbols = ocr_manager.ocr_image_content(myimage)
        print(symbols)
        return realsence_service_pb2.ReplyCharacters(characters=symbols)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    realsence_service_pb2_grpc.add_service_realsenceServicer_to_server(RealSence_Service(), server)
    server.add_insecure_port('[::]:50052')
    print("port is 50052")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()