# average predictions from all the folds from 3rd and 4th epoch

import pandas as pd

path_common='./data/submission'
sub_names=['model001_fold0_ep2_test_tta5.csv',\
           'model001_fold1_ep2_test_tta5.csv',\
           'model001_fold2_ep2_test_tta5.csv',\
           'model001_fold3_ep2_test_tta5.csv',\
           'model001_fold4_ep2_test_tta5.csv',\
           'model001_fold0_ep3_test_tta5.csv',\
           'model001_fold1_ep3_test_tta5.csv',\
           'model001_fold2_ep3_test_tta5.csv',\
           'model001_fold3_ep3_test_tta5.csv',\
           'model001_fold4_ep3_test_tta5.csv']

subs=[]
for s in sub_names:
    subs.append(pd.read_csv(path_common+'/'+s))

for s in subs[1:]:
    subs[0].Label = subs[0].Label + s.Label 

subs[0].Label=subs[0].Label/len(subs)

print(len(subs))
subs[0].head()

subs[0].to_csv(path_common+'/model006_blend_all5folds_ep2_new-tta8.csv', index=False)

# submit predictions
# kaggle competitions submit -c rsna-intracranial-hemorrhage-detection -f model006_blend_all5folds_ep2_new-tta8.csv -m "tta8"