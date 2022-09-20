
from distutils import errors
from mailbox import linesep
import re
import sys
sys.path.append("preprocess\pdfminer")
from autogenerate import autogenerate


txt="""
1. Introduction
YOLO se- ries always pursuit the optimal speed and accuracy trade-off for real-time applications. Currently, YOLOv5 holds the best performance with 48.2% AP on COCO at 13.7 ms. YOLOX-L achieves 50.0% AP with 640 × 640 resolution, outperforming the counterpart YOLov5-L by 1.8% AP.2. YOLOX
CNN.com will feature iReporter photos in a weekly Travel Snapshots gallery. Please submit your best shots of the U.S. for next week. Visit CNN.com/Travel next Wednesday for a new gallery of snapshots. Visit the gallery for a weekly selection of snapshots from across the globe.   
2.1. YOLOX-DarkNet53
We train the models for a total of 300 epochs with 5 epochs warm- up on COCO train2017. We choose YOLOv3 [25] with Darknet53 as our base- line. We report the inference time with batch=1 on V100 in Tab. 2 and Tab. 3. The decoupled head is essential to the end-to-end version of YOLOX.
4 The term “anchor” refers to “anchor point” in the context of anchor-
SimOTA reduces the training time and avoids additional solver hyperparameters in Sinkhorn- Knopp algorithm. SimOTA raises the detector from 
45.0% AP to 47.3% AP. We follow [39] to add two additional conv layers, one-to-one label assignment, and stop gradient.
2.2. Other Backbones
YOLOX achieves consis- tent improvements against all the corresponding counter- parts. We adopt the exact YOLOv5’s backbone including modiﬁed CSPNet, SiLU activation, and the PAN [19] head. We further shrink our model as YOLOX-Tiny to compare with YOLov4-T Tiny [30]. For mobile devices, we adopt depth wise convolution to con- struct a YOLOx-Nano model, which has only 0.91M pa- rameters.
3. Comparison with the SOTA
Fig. 1 plots the somewhat controlled speed/accuracy curve. There are some high performance YOLO series with larger model sizes. We adopt a YOLOX-L model with TensorRT to product our model for the challenge to win the 1st place. We found that the best trade-off point for the metric on 30 FPS data stream is a powerful model.
5. Conclusion
YOLOX achieves a better trade-off between speed and accuracy than other counterparts across all model sizes. It is remarkable that we boost 
the architecture of YOLOv3, which is still one of the most widely used detectors in industry due to its broad compatibility. We hope this report can help developers and researchers get better experience in practical scenes.
"""


# lines=txt.split('\n')
# outputresult=''
 
# for line in lines:
#     if re.findall('^[0-9]{1}[\.\s]+[A-Z][a-zA-Z\s\w\S]+$|^[0-9]{1}[\.\s]*[0-9]{1}[\.\s]+[A-Z][a-zA-Z\s\w\S]+$',line):
#         outputresult=outputresult+r"\newpage"+'\n'
#         outputresult=outputresult+'#'+line+'\n'
#     elif line:
#         outputresult=outputresult+'p>'+line+'\n'
#     else:
#         continue

# with open("1.md","a",encoding='UTF-8',errors='ignore') as test:
#     test.write(outputresult)


a=autogenerate("output.pptx",'1.md',10)

a.allmain()
