# College-minor-project-dog-show

## Project Goal

* In this project, we will use an image classifier to identify dog breeds.

## Description

* Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.
* Some people are planning on registering pets that aren’t actual dogs. You need to use an already developed Python classifier to make sure the participants are dogs.

## Important Notes

* For this image classification task, we will be using an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN). CNNs work particularly well for detecting features in images like colors, textures, and edges; then using these features to identify objects in the images. We'll use a CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet. There are different types of CNNs that have different structures (architectures) that work better or worse depending on our criteria. With this project, we'll explore the three different architectures (AlexNet, VGG, and ResNet) and determine which is best for our application.
* Remember that certain breeds of dogs look very similar. The more images of two similar-looking dog breeds that the algorithm has learned from, the more likely the algorithm will be able to distinguish between those two breeds. We have found the following breeds to look very similar: Great Pyrenees and Kuvasz, German Shepherd and Malinois, Beagle and Walker Hound, amongst others.

## Project Instructions

### Principal Objectives

1. Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.
2. Correctly classify the breed of dog, for the images that are of dogs.
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.
4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.


### Program Outline

* Time your program

  * Use Time Module to compute program runtime
* Get program Inputs from the user

  * Use command line arguments to get user inputs
* Create Pet Images Labels

  * Use the pet images filenames to create labels
  * Store the pet image labels in a data structure(e.g. a dictionary)
* Create Classifier Labels and Compare Labels

  * Use the Classifier function to classify the images and create the classifier labels
  * Compare Classifier Labels to Pet Image Labels
  * Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
* Classifying Labels as "Dogs" or "Not Dogs"

  * Classify all Labels as "Dogs" or "Not Dogs" using the dognames.txt file
  * Store new classifications in the complex data structure (e.g. dictionary of lists)
* Calculate the Results

  * Use Labels and their classifications to determine how well the algorithm worked on classifying images
* Print the Results
