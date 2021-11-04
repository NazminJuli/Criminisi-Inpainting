#!/usr/bin/python

import sys, os
import cv2
import numpy as np
from Inpainter import Inpainter

if __name__ == "__main__":
    """
    Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth=4].
    """
    # if not len(sys.argv) == 3 and not len(sys.argv) == 4:
    #     print ('Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth].')
    #     exit(-1)
    #
    # if len(sys.argv) == 3:
    #     halfPatchWidth = 4
    # elif len(sys.argv) == 4:
    #     try:
    #         halfPatchWidth = int(sys.argv[3])
    #     except ValueError:
    #         print('Unexpected error:', sys.exc_info()[0])
    #         exit(-1)
    #
    halfPatchWidth = 4
    # image File Name
    originalImage = cv2.imread('/home/kow/CutOutWiz/Projects/pythonProject/exemplar_inpainting/Exemplar-Based-Inpaining-Python-aeb181846b3d779626f74832b1fe6d1d6471fe09/source/beautiful-caucasian-woman-with-makeup.png', 1)
    # originalImage = cv2.resize(originalImage,(1000,1000))
    # cv2.imshow('w', originalImage)
    # CV_LOAD_IMAGE_COLOR: loads the image in the RGB format TODO: check RGB sequence
    # originalImage = cv2.imread(imageName, cv2.CV_LOAD_IMAGE_COLOR)
    if originalImage is None:
        print('Error: Unable to open Input image.')
        exit(-1)
    
    # mask File Name
    inpaintMask = cv2.imread('/home/kow/CutOutWiz/Projects/pythonProject/exemplar_inpainting/Exemplar-Based-Inpaining-Python-aeb181846b3d779626f74832b1fe6d1d6471fe09/source/black.png', 0)
    # inpaintMask = cv2.resize(inpaintMask, (1000, 1000))
    # inpaintMask = cv2.imread(maskName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    if inpaintMask is None:
        print('Error: Unable to open Mask image.')
        exit(-1)
    
    i = Inpainter(originalImage, inpaintMask, halfPatchWidth)
    if i.checkValidInputs()== i.CHECK_VALID:
        i.inpaint()
        cv2.imwrite("result.jpg", i.result)
        # cv2.namedWindow("result")
        # cv2.imshow("result", i.result)
        # cv2.waitKey()
    else:
        print('Error: invalid parameters.')
    
