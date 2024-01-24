from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Simulation wifi signal strength in a space

def signal_strength(distance, freq, transmitter_gain=0, relative_permittivity=1):
    # Returns total path loss in dB
    # distance is in meters
    # freq is in GHz
    return transmitter_gain -20*np.log10(distance) - 20*np.log10(freq) - 32.45 - 20*np.log10(relative_permittivity)

materials = {
    "air": 1,
    "concrete": 4.5,
    "silicon": 11.7,
    "methanol": 33,
    "water": 80,
}

x = np.linspace(0, 10, 1000)

# y = [np.array([signal_strength(i, 2.4, relative_permittivity=materials[materials[material]]) for i in x]) for material in materials.keys()]
y = []
for material in materials.keys():
    y.append(np.array([signal_strength(i, 2.4, relative_permittivity=materials[material]) for i in x]))

fig = plt.figure()
for i in range(len(materials)):
    plt.plot(x, y[i], label=list(materials.keys())[i])
plt.legend()
plt.xlabel('Distance (m)')
plt.ylabel('Signal Strength (dB)')
plt.title('Total path loss for 2.4 GHz')
plt.show()