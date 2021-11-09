from __future__ import print_function
import logging

import grpc

import realsence_service_pb2
import realsence_service_pb2_grpc

import ocr_manager
import sys
from datetime import datetime

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = realsence_service_pb2_grpc.service_realsenceStub(channel)
        myimage = ocr_manager.Image_To_MyImage("C:/Users/design27/source/hello_py/resource/image333.jpg")
        print(sys.getsizeof(myimage.image_data))

        request =  realsence_service_pb2.RequestImage()
        request.width = 1
        request.height = 1
        request.image_data = myimage.image_data

        curTime_start = datetime.now()
        current_time = curTime_start.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        ###############
        response = stub.OcrImage(request)
        ###############
        curTime_end = datetime.now()
        current_time = curTime_end.strftime("%H:%M:%S")
        print("Current Time =", current_time)
    ####################
    characters =  response.characters  
    print("client received: ",sys.getsizeof(characters))
    for str in characters:
        print(str)


if __name__ == '__main__':
    logging.basicConfig()
    run()
