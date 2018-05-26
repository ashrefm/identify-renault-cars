
import numpy as np
import matplotlib.pyplot as plt
import itertools
from scipy.misc import imread
from keras.preprocessing import image

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def plot_img_score(subsample, best_thresh, labels=['Other', 'Renault']):
    """
    Plot all images contained in subsample data frame and their scores
    
    Args:
    subsample -- Pandas DataFrame containes the path of the images, the labels and the predictions    
    """

    n = len(subsample) # number of images to visualize
    plt.figure(figsize=[12,12*n/2])

    for i in range(n):
        img_path = subsample.iloc[i]['image']
        img = image.load_img(img_path)    
        pred_value = subsample.iloc[i]['pred']
        pred_bool = np.int(subsample.iloc[i]['pred'] > best_thresh)
        correct = 'Correct'  if subsample.iloc[i]['label'] == pred_bool else 'Wrong'
        title = correct + '\n' + labels[pred_bool] + ' (proba=' + str(round(pred_value,2)) + ')' + '\n' + img_path
        
        plt.subplot(n,2,i+1)
        plt.imshow(img)
        plt.title(title, fontsize=14)
        if i == n-1:
            break