import qrcode
import argparse

def make_qrcode(data):
    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save("qrcode_img/{}.png".format(data))

if __name__ == '__main__':
    # [START vision_document_text_tutorial_run_application]
    parser = argparse.ArgumentParser()
    parser.add_argument('data', help='The data to make qrcode.')
    args = parser.parse_args()
    make_qrcode(args.data)
