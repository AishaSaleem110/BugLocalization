from collections import namedtuple
from pathlib import Path

# Dataset root directory
_DATASET_ROOT = Path('/content/gdrive/MyDrive/project_folder/bug-localization/data')

Dataset = namedtuple('Dataset', ['name', 'root', 'src', 'bug_repo'])

# Source codes and bug repositories
certbot=Dataset(
  'certbot',
  _DATASET_ROOT / 'Certbot',
  _DATASET_ROOT /'Certbot/certbot-master',
  _DATASET_ROOT /'Certbot/certbot.json'
)

compose=Dataset(
  'compose-master',
  _DATASET_ROOT / 'compose-master',
  _DATASET_ROOT /'compose-master/compose-master',
  _DATASET_ROOT /'compose-master/compose.json'
)

django=Dataset(
  'django-rest-framework-master',
  _DATASET_ROOT / 'django-rest-framework-master',
  _DATASET_ROOT /'django-rest-framework-master/django-rest-framework-master',
  _DATASET_ROOT /'django-rest-framework-master/django_rest_framework.json'
)

keras=Dataset(
  'keras-master',
  _DATASET_ROOT / 'keras-master',
  _DATASET_ROOT /'keras-master/keras-master',
  _DATASET_ROOT /'keras-master/keras.json'
)
mitmproxy=Dataset(
  'mitmproxy-master',
  _DATASET_ROOT / 'mitmproxy-master',
  _DATASET_ROOT /'mitmproxy-master/mitmproxy-master',
  _DATASET_ROOT /'mitmproxy-master/mitmproxy.json'
)

requests=Dataset(
  'requests-master',
  _DATASET_ROOT / 'requests-master',
  _DATASET_ROOT /'requests-master/requests-master',
  _DATASET_ROOT /'requests-master/requests.json'
)
scikit=Dataset(
  'scikit-learn-master',
  _DATASET_ROOT / 'scikit-learn-master',
  _DATASET_ROOT /'scikit-learn-master/scikit-learn-master',
  _DATASET_ROOT /'scikit-learn-master/scikit-learn.json'
)
scrapy=Dataset(
  'scrapy-master',
  _DATASET_ROOT / 'scrapy-master',
  _DATASET_ROOT /'scrapy-master/scrapy-master',
  _DATASET_ROOT /'scrapy-master/scrapy.json'
)
spaCy=Dataset(
  'spaCy-master',
  _DATASET_ROOT / 'spaCy-master',
  _DATASET_ROOT /'spaCy-master/spaCy-master',
  _DATASET_ROOT /'spaCy-master/spaCy.json'
)

tornado=Dataset(
  'tornado-master',
  _DATASET_ROOT / 'tornado-master',
  _DATASET_ROOT /'tornado-master/tornado-master',
  _DATASET_ROOT /'tornado-master/tornado.json'
)


### Current dataset in use. (change this name to change the dataset)
DATASET = django

if __name__ == '__main__':
    print(DATASET.name, DATASET.root, DATASET.src, DATASET.bug_repo)
