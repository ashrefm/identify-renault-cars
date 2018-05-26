# Identify Renault Cars

This small project is an example of how to benefit from transfer learning using pre-trained convolutional neural nets in Keras.

The data is a various set of ~9400 car images (collected from google image using a web scrapping code) where 50% of them represent Renault cars.

Our goal is to build a powerful classifier capable of identifying Renault cars in different colors and positions (not only frontal pictures).

The approach is the following:


### Data collection

Run the script "google_image_scrapper.py" to collect images from google using a search keyword.  
Open a terminal and execute the following command: $ python google_image_scrapper.py


### Data preparation

* Splitting the modeling data into 90% train and 10% cross-validation. We kept 60 challenging images for the final test.
* Mapping of file paths and their labels are stored into csv files
* We also show how to use HDF5 files to store image features and labels in order to deal with volume


### Modeling

We use the pre-trained VGG-19 model to extract features from images (output of the first fully connected layer).  
Based on these features, we train a deep neural network with 4 densely connected layers where we gradually decrease the number of learnable parameters.  
Note: The training was accelerated using a 2014 CUDA GPU (Nvida GTX 880M).


### Scoring

We prepare a final notebook that can be used to featurize new images and generate predictions using our previously trained model.

