# YOLO
Training on [Form Dataset](https://github.com/MrPanda1/FormDataset)

## Dependencies
* Python3 
* tensorflow 1.13.1 
* numpy 
* opencv 3
* Cython

## Getting started
(Omit python keyword if not on windows)
1. Download Form Dataset images and put it into image/train
2. Download Form Dataset annotations and put it into annotation/train
2. Run python setup.py build_ext --inplace
2. Run python flow --model cfg/yolo-forms.cfg --train --annotation data/annotation/train --dataset data/image/train
    - You can add the --load [path_to_file] flag if you have pre-trained weights to use.

## Notes
* annotation/test contains ALL xml files, while annotation/test_* contains subsets of those xml files to train on smaller datasets.
* Images and Annotations can be found at: https://github.com/MrPanda1/FormDataset
* Darkflow can be found at: https://github.com/thtrieu/darkflow
* Pretrained weights:
    * https://pjreddie.com/media/files/yolov3.weights
    * https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU
