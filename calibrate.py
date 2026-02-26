from sklearn.calibration import CalibratedClassifierCV

def calibrate_model(model, X, y):
    calibrated = CalibratedClassifierCV(model, method="isotonic")
    calibrated.fit(X, y)
    return calibrated