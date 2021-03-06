"""
作业04 - 训练应用

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import numpy as np
from keras.models import load_model


# lte80: load model and predict
def next_soc_lte80(arr):
    x_data = np.array(arr).reshape(len(arr) // 30, 30)
    model = load_model("model/ep22mce_soc_lte80.h5")
    return model.predict(x_data)


# lte80: train apply model
soc_lte80_lines = [11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13,
                   13, 13,
                   13, 13, 13]
print("next soc: {0}".format(int(next_soc_lte80(soc_lte80_lines)[0, 0])))


# gte80: load model and predict
def next_soc_gte80(arr):
    x_data = np.array(arr).reshape(len(arr) // 30, 30)
    model = load_model("model/ep22mce_soc_gte80.h5")
    return model.predict(x_data)


# gte80: train apply model
soc_gte80_lines = [91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93,
                   93, 93,
                   93, 93, 93]
print("next soc: {0}".format(int(next_soc_gte80(soc_gte80_lines)[0, 0])))

"""
# extra: result -> 80
count = 0
next_target_soc = 0
while next_target_soc < 80:
    count += 1
    print(soc_extra_lines[-30:])
    next_target_soc = int(next_soc_lte80(soc_extra_lines[-30:])[0, 0])
    print("{0} -> soc: {1}".format(count, next_target_soc))
    soc_extra_lines.append(next_target_soc)
"""


# extra: load model and predict
def recursion_soc_lte80(model, arr, count=0):
    count += 1
    print(arr[-30:])
    x_data = np.array(arr[-30:]).reshape(1, 30)
    next_soc = int(model.predict(x_data)[0, 0])
    print("{0} -> {1}".format(count, next_soc))
    if 80 > model.predict(x_data):
        arr.append(next_soc)
        return recursion_soc_lte80(model, arr, count)


# extra: train apply model
soc_extra_lines = [27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29,
                   29, 29,
                   29, 29, 29]
model = load_model("model/ep22mce_soc_lte80.h5")
print(recursion_soc_lte80(model, soc_extra_lines))
