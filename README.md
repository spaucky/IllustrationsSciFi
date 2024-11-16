# IllustrationsSciFi
This experimental Sci-Fi, Convolutional Neural Network, Scientific Illustration and Philosophy project was a collaboration between myself, Freya Gascoyne and Reuben Tyler-Wilkinson. In it we ask what separates scientific illustration from art, objectivity from ML Model Outputs and fact from fiction. The project's output can be accessed at [FinalOutput.pdf](https://github.com/spaucky/IllustrationsSciFi/blob/main/FinalOutput.pdf) inside this repository.

### Understanding the files in this repository:
- data  
This file contains the images which were used to train the neural network, they are split into two groups PlantArt (812 images) and PlantScientific (592 images)
- logs  
This file contains logs of all of training and validation permutations of the neural network.
- models  
This file contains the two different neural networks which I trained. ScientificVSArt.h5 was created before I understood regularisation and was highly overfitted leading to very low testing scores. However, having implemented BatchNormalisation and Dropout into my neural network (ImprovedNeuralNetwork.h5), there was less overfitting and my neural network had better test results.
- OurDrawings  
This file contains the graph that featured on the final page of our final report, it also contains the neural network's scores for all of the scientific illustrations we created, as well as these images themselves.
### .py files
- DataSetup.py  
This splits our data up into batches of 30 images which are then distributed in a 70/20/10% split between training, validation and testing. It uses the Python module Tensorflow to do this.
- DuplicateCheck.py  
This uses image hashes to remove duplicate images from each of our two data files (PlantArt and PlantScientific) to ensure that no single images has too much of an effect on the final model.
- FalseImageFinder.py  
This identifies files within each of our two neural network data files which are not .bmp, .gif, .jpg, .jpeg or .png as only these image types are supported by Tensorflow.
- GraphCreation.py  
This Python file creates the graph for the final page of our submission. It also performs linear regression and calculates some basic statistics about the neural network's understanding of our illustrations.
- NeuralNetworkModel.py  
This .py file lays out the structure of our neural network and then trains it using our training data. It does this through the use of tensorflow.keras
- OwnDrawingsTesting.py  
This file tests our own drawings with the neural network. It then stores these scores in a .csv file.
- PinterestScraping.py  
This file was used to scrape images from Pinterest. It runs through search terms and stores all of the images produced by these search terms in two seperate folders.
- TestSave.py  
This .py file was highly important in allowing us to test the neural network to determine its accuracy and precision. It also created plots showing how loss and accuracy changed over time for the training data and the validation data as the neural network trained. These graphs could be used to determine the extent to which the neural network was overfitting.
