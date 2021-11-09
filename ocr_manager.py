#!/usr/bin/env python
import argparse
from enum import Enum
import io

import PIL

from google.cloud import vision
from PIL import Image, ImageDraw

from datetime import datetime

from google.cloud.vision_v1.services.image_annotator import client
# [END vision_document_text_tutorial_imports]


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


class Ocr_Manager:
    image_files = []
    documents = []
    symbols = []

    def __init__(self):
        #self.client = vision.ImageAnnotationContext()
        print("init")

    def add_image(self, image_file):
        self.image_files.append(Image.open(image_file))
        print("add image")

    def make_documents(self):
        print("make_documents")
        for image_file in self.image_files:
            with io.open(image_file, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = self.client.document_text_detection(image=image)
            document = response.full_text_annotation
            self.documents.append(document)

    def make_symbols(self):
        print("make_symbols")
        for page in self.documents.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            print(symbol.text, end=' ')
                            self.symbols.append(symbol.text)

    def make_documents_symbols(self):
        print("make_documents_symbols")
        self.make_documents()
        self.make_symbols()

    def get_symbols(self, symbols=[]):
        print("get_symbols")
        for symbol in self.symbols:
            symbols.appen(symbol)

    def image_ocr(self, file, symbols):
        client = vision.ImageAnnotatorClient()

        with io.open(file, 'rb') as image_file:
            content = image_file.read()
        # image = Image.open(file)
        # print(image.format,image.size,image.mode)
        # image.show()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        #response = self.client.document_text_detection(image=image)
        document = response.full_text_annotation
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            print(symbol.text, end=' ')
                            symbols.append(symbol.text)


class MyImage:
    def __init__(self, width, height, image_data):
        self.width = width    # 名稱
        self.height = height     # 尺寸
        self.image_data = image_data     # 列表


def Image_To_MyImage(image_file):
    image = Image.open(image_file)
    with io.open(image_file, 'rb') as im:
        myimage = MyImage(image.width, image.height, im.read())
    return myimage


def ocr_image_content(image):
    client = vision.ImageAnnotatorClient()
    content = image.image_data
    #print(content)
    ocr_image = vision.Image(content=content)
    print("start ask google")
    response = client.document_text_detection(image=ocr_image)
    print("has a response")
    document = response.full_text_annotation
    symbols = []
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        print(symbol.text, end=' ')
                        symbols.append(symbol.text)
    return symbols
# def MyImage_To_Image(image):


if __name__ == '__main__':
    # [START vision_document_text_tutorial_run_application]
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    # myimage = Image_To_MyImage(args.detect_file)
    # ocr_image_content(myimage)
    #symbols = []

    #ocr_manager = Ocr_Manager()
    # ocr_manager.image_ocr(args.detect_file,symbols)

    # for symbol in symbols:
    #     print(symbol)

    #render_doc_text(args.detect_file, args.out_file)
    # [END vision_document_text_tutorial_run_application]
# [END vision_document_text_tutorial]
