import matplotlib.pyplot as plt
import numpy as np
# problem givens (weight measuremnts in pounds & SF & model rate)
# actual = np.linspace(160,180,41)
# noise_scale = 7
# noise = (0.5-np.random.rand(len(actual)))*noise_scale
# measurements = actual + noise
measurements = np.array([158.0, 164.2, 160.3, 159.9, 162.1, 164.6,169.6, 167.4, 166.4, 171.0, 171.2, 172.6])
dt = 1.0 # day
g = 0.4
ini_rate=  -1#lb/day
ini_esti = 160
pred = np.zeros(len(measurements))
esti= np.zeros(len(measurements)+1)
h = 1/3.0

esti[0] = ini_esti
rate = ini_rate
for k in range(len(measurements)):
    #prediction
    print(esti[k])
    pred[k] =  esti[k] + rate*dt
    #update
    residual = measurements[k] - pred[k] 
    esti[k+1] = pred[k] + g*residual
    rate = rate +  h*residual/dt

    

# Time arrays
time_measurements = np.arange(len(measurements))+1
time_estimates = np.arange(len(esti))
time_predictions = np.arange( len(pred))+1  # Start from index 1

# Plot all three datasets
plt.figure(figsize=(14, 8))
plt.plot(time_measurements, measurements, 'ro', markersize=8, label='Measurements', zorder=3)
plt.plot(time_estimates, esti, 'b-', linewidth=2, label='Estimates posterior', marker='s', markersize=6)
plt.plot(time_predictions, pred, 'g--', linewidth=2, label='Predictions', marker='^', markersize=6)  # Skip first element
# plt.plot(time_measurements, actual, 'k--', linewidth=2, label='Actual Trend')
plt.plot([0,12], [160,172], 'k--', linewidth=2, label='Actual Trend')

# Labels and formatting
plt.xlabel('Day', fontsize=12)
plt.ylabel('Weight (lbs)', fontsize=12)
plt.title('Weight Tracking: Measurements, Predictions, and Estimates', fontsize=14, fontweight='bold')
plt.legend(fontsize=10, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
