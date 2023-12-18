from pathlib import Path
import face_recognition
import pickle
import argparse
from recogniser import encode_know_faces, recognize_faces, _display_face, validate
from collections import Counter
from PIL import Image, ImageDraw



parser = argparse.ArgumentParser(description = "Recognize faces in an image")
parser.add_argument("--train", action="store_true", help="Train on input data")
parser.add_argument("--validate", action="store_true", help="Validate on trained model")
parser.add_argument("--test", action="store_true", help="Test the trained model with an unknow image")
parser.add_argument("-m", action="store", default="hog", choices=["hog","cnn"], help="Model to use for face detection")
parser.add_argument("-f", action="store", default="training", help="Path to an image with an unknown face")

args = parser.parse_args()

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

if __name__ == "__main__":
    if args.train:
        encode_know_faces()
    elif args.validate:
        validate(model=args.m)
    elif args.test:
        recognize_faces(image_location=args.f, model=args.m)
    else:
        print("Please specify an action")
        parser.print_help()