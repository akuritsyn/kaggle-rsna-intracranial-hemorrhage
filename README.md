# [Kaggle RSNA Intracranial Hemorrhage Detection](https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection)

## Top 5% solution (56/1345) based on an initial model developed by [appian42](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage)


## Requirements

- Python 3.6.6
- [Pytorch](https://pytorch.org/) 1.1.0
- [NVIDIA apex](https://github.com/NVIDIA/apex) 0.1 (for mixed precision training)


## Architecture (Single model)

| Backbone | Image size |
----|----
| se\_resnext50\_32x4d | 512x512 |

- Final score is an average ensemble of predictions from 10 models based on 5 folds and 3rd and 4th epochs  with clip=0.98

## Windowing

For this challenge, windowing is important to focus on the matter, in this case the brain and the blood. There are good kernels explaining how windowing works.

- [See like a Radiologist with Systematic Windowing](https://www.kaggle.com/dcstang/see-like-a-radiologist-with-systematic-windowing) by David Tang
- [RSNA IH Detection - EDA](https://www.kaggle.com/allunia/rsna-ih-detection-eda) by Allunia

We used three types of windows to focus and assigned them to each of the chennel to construct images on the fly for training.

| Channel | Matter | Window Center | Window Width |
----------|--------|---------------|---------------
| 0 | Brain | 40 | 80 |
| 1 | Blood/Subdural | 80 | 200 |
| 2 | Soft tissues | 40 | 380 |


## Preparation

Please put `./input` directory in the root level and unzip the file downloaded from kaggle there. All other directories such as `./cache`, `./data`, `./model` will be created if needed when `./bin/preprocess.sh` is run.


## Preprocessing

Please make sure you run the script from parent directory of `./bin`.

~~~
$ sh ./bin/preprocess.sh
~~~

[preprocess.sh](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/bin/preprocess.sh) does the following at once.

- [dicom_to_dataframe.py](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/src/preprocess/dicom_to_dataframe.py) reads dicom files and save its metadata into the dataframe. 
- [create_dataset.py](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/src/preprocess/create_dataset.py) creates a dataset for training.
- [make_folds.py](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/src/preprocess/make_folds.py) makes folds for cross validation. 


## Training

~~~
$ sh ./bin/train001.sh
~~~

[train.001.sh](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/bin/train001.sh) uses se\_resnext50\_32x4d from [pretrained-models.pytorch](https://github.com/Cadene/pretrained-models.pytorch) for training. 
One epoch probably takes 20,000 seconds to train with a single 1080ti.


## Predicting

~~~
$ sh ./bin/predict001.sh
~~~

[predict001.sh](https://github.com/appian42/kaggle-rsna-intracranial-hemorrhage/blob/master/bin/predict001.sh) does the predictions and makes a submission file for scoring on Kaggle. Please uncomment the last line if you want to automatically submit it to kaggle through API.


