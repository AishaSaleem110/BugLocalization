# BugLocalization for Python based Projects
#This is an extension of the work produced by Reba Al Gharibi (et. al) for Java based projects which can be found at https://github.com/h4iku/bug-localization.git

#The work has been extended for Python-based projects.

#Follow the instructions to run the project on google colab

1. Download the code from github and upload it on your google drive.Alternatively, you can directly clone it on google colab.

2. On google colab install the following dependencies.

```
!pip install xmltodict javalang pygments inflection nltk numpy scipy scikit-learn spacy
!python -m spacy download en_vectors_web_lg

import nltk
nltk.download('punkt')

import nltk
nltk.download('averaged_perceptron_tagger')
```
3. Connect google colab with your google drive to access the project or you can also clone the repositsory.
```
from google.colab import drive
drive.mount('/content/gdrive')
```
4. Download the dataset for python based projects from https://github.com/muvvasandeep/BuGL and unzip it, upload the projects source code, .json files in the data directory of the  project. 
5. Check the path of datasets in ``` /datasets.py``` module and change the value of the DATASET variable to choose different datasets.
6. Run the main module after changing the base path for your google drive. Please note the following is my path project_folder/bug-localization/buglocalizerPython and you should change it to yours:
```
!python /content/gdrive/MyDrive/project_folder/bug-localization/buglocalizerPython/main.py
```


