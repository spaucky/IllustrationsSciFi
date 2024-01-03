# IllustrationsSciFi
Understanding the files in this repository:
- data
This file contains the images which were used to train the neural network, they are split into two groups PlantArt (812 images) and PlantScientific (592 images)
- logs
This file contains logs of all of training and validation permutations of the neural network.
- models
This file contains the two different neural networks which I trained. ScientificVSArt.h5 was created before I understood regularisation and was highly overfitted leading to very low testing scores. However, having implemented BatchNormalisation and Dropout into my neural network (ImprovedNeuralNetwork.h5), there was less overfitting and my neural network had better test results.
- OurDrawings
This file contains the graph that featured on the final page of our final report, it also contains the neural network's scores for all of the scientific illustrations we created, as well as these images themselves.

