import numpy as np


def precision_recall(y_pred, y_label):
    TP = np.sum((y_pred == 1) & (y_label == 1))
    FP = np.sum((y_pred == 1) & (y_label == 0))
    FN = np.sum((y_pred == 0) & (y_label == 1))
    TN = np.sum((y_pred == 0) & (y_label == 0))

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    return precision, recall
