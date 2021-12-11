# In-painting 
Python implementation of A. Criminisi object removal algorithm
It has two input parameters: the original image in RGB and the desired mask to be inpainted in color mode of Gray

* OpenCV
* Numpy
* NVIDIA CUDA 

# Sample input and output
![marked area to be removed](https://github.com/NazminJuli/Criminisi-Inpainting/blob/155bb02433761202e4aca90db8e85c48ebcc418b/problem_2.png)
![marked area after inpainting](https://github.com/NazminJuli/Criminisi-Inpainting/blob/155bb02433761202e4aca90db8e85c48ebcc418b/problem_2_out_5.jpg)

It works the trick to remove spot from the source image but takes higher computation time for higher resolution images.
*** More advanced modification for less computation time will be released soon.... ***

# References
Criminisi, Antonio, Patrick Pérez, and Kentaro Toyama. "Region filling and object removal by exemplar-based image inpainting." Image Processing, IEEE Transactions on 13.9 (2004): 1200-1212.
