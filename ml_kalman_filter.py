import numpy as np

class KalmanFilter:
  count = 0

  X = np.asarray([1, 0]) # State Vector
  P = np.eye(2) # Error Covariance Matrix
  samplingRate = 0.0 # Sampling Rate

  Pi = np.eye(2)  # State Transition Matrix
  H = np.empty(2) # Observation Matrix

  Q = np.eye(2)
  R = 0.0

  def __init__(self, samplingRate, processNoiseCov, measureNoiseCov):
    print("Kalman init")

    self.X = np.asarray([1.0, 0.0])
    self.P = np.eye(2)

    self.samplingRate = samplingRate
    self.Pi = np.asarray([[1.0, samplingRate], [0.0, 1.0]])
    self.H = np.asarray([1.0, 0.0])

    self.Q = np.asarray([[processNoiseCov, 0.0], [0.0, processNoiseCov]])
    self.R = measureNoiseCov

  def filter(self, data):
    # Measure
    z = data + np.random.normal(0, self.R)
    self.count += 1

    # Prediction State
    XPred = np.dot(self.Pi, self.X.T)
    PPred = np.dot(np.dot(self.Pi, self.P), self.Pi.T) + self.Q

    # Update State
    meas = z - np.dot(self.H, XPred)
    gain = np.dot(PPred, self.H) / np.dot(np.dot(self.H, PPred), self.H.T) + self.R
    
    XEst = XPred + gain * meas
    PEst = np.dot(np.eye(2) - np.dot(gain, self.H), PPred)
    
    self.X = XEst
    self.P = PEst

    return XEst, z