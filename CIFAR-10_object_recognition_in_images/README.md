## CIFAR-10 - Object Recognition in Images

### Identify the subject of 60,000 labeled images

[CIFAR-10](http://www.cs.toronto.edu/~kriz/cifar.html) is an established computer-vision dataset used for object 
recognition. It is a subset of the [80 million tiny images dataset](http://groups.csail.mit.edu/vision/TinyImages/) and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

Kaggle is hosting a CIFAR-10 leaderboard for the machine learning community to use for fun and practice. You can see how 
your approach compares to the latest research methods on Rodrigo Benenson's [classification results page](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html).

![alt tag](https://kaggle2.blob.core.windows.net/competitions/kaggle/3649/media/cifar-10.png)

Please cite this technical report if you use this dataset: [Learning Multiple Layers of Features from Tiny Images](http://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf), Alex Krizhevsky, 2009.

### Data Files

|File Name        |Available Formats  |
|-----------------|-------------------|
|sampleSubmission |.csv (3.04 mb)     |
|test             |.7z (609.75 mb)    |
|train            |.7z (104.64 mb)    |
|trainLabels      |.csv (575.10 kb)   |

The CIFAR-10 data consists of 60,000 32x32 color images in 10 classes, with 6000 images per class. There are 50,000 training images and 10,000 test images in the official data. We have preserved the train/test split from the original dataset.  The provided files are:

**train.7z** - a folder containing the training images in png format
**test.7z** - a folder containing the test images in png format
**trainLabels.csv** - the training labels

To discourage certain forms of cheating (such as hand labeling) we have added 290,000 junk images in the test set. These images are ignored in the scoring. We have also made trivial modifications to the official 10,000 test images to prevent looking them up by file hash. These modifications should not appreciably affect the scoring. You should predict labels for all 300,000 images.

The label classes in the dataset are:

* airplane 
* automobile 
* bird 
* cat 
* deer 
* dog 
* frog 
* horse 
* ship 
* truck

The classes are completely mutually exclusive. There is no overlap between automobiles and trucks. "Automobile" includes sedans, SUVs, things of that sort. "Truck" includes only big trucks. Neither includes pickup trucks.

### Evaluation

Submissions are evaluated on classification accuracy (the percent of labels that are predicted correctly).

### Submission Format

For each image in the test set, predict a label for the given id. Your labels must match the official labels exactly {airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck}. Your submission should have a header.

```
id,label
1,cat
2,cat
3,cat
4,cat
...
```
