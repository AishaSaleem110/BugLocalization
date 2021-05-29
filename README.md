# BugLocalization for Python based Projects
#This is an extension of the work produced by Reba Al Gharibi (et. al) for Java based projects which can be found at https://github.com/h4iku/bug-localization.git

#The work has been extended for Python-based projects.

#Follow the instructions to run the project on google colab

1. On google colab install the following dependencies.

```
!pip install xmltodict javalang pygments inflection nltk numpy scipy scikit-learn spacy
!python -m spacy download en_vectors_web_lg

import nltk
nltk.download('punkt')

import nltk
nltk.download('averaged_perceptron_tagger')
```
2. Connect google colab with your google drive to access the project or you can also clone the repositsory.
```
from google.colab import drive
drive.mount('/content/gdrive')
```
3. Download the dataset for python based projects from https://github.com/muvvasandeep/BuGL and unzip it, upload the projects source code, .json files in the data directory of the  project. 
4. Check the path of datasets in ``` buglocalizerPython/datasets.py``` module and change the value of the DATASET variable to choose different datasets.
5. Run the main module after changing the base path for your google drive
```
!python /content/gdrive/MyDrive/project_folder/bug-localization/buglocalizerPython/main.py
```


