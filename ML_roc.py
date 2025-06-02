import numpy as np


def roc_curve(pred, label, threshold_num=10):
    """
    x-axis: False Postivie Rates
    y-axis: True Positive Rates
    """

    thresholds = np.linspace(1.0, 0.0, threshold_num)

    TRPs = []
    FPRs = []

    for threshold in thresholds:
        pred_ = (pred >= threshold).astype(int)

        TP = np.sum((pred_ == 1) & (label == 1))
        TN = np.sum((pred_ == 0) & (label == 0))
        FP = np.sum((pred_ == 1) & (label == 0))
        FN = np.sum((pred_ == 0) & (label == 1))

        TPR = TP / (TP + FN) if (TP + FN) > 0 else 0.0
        FPR = FP / (FP + TN) if (FP + TN) > 0 else 0.0

        TRPs.append(TPR)
        FPRs.append(FPR)

    return TRPs, FPRs, thresholds
