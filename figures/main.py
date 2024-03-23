from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

image = np.load("ps.npy.txt")

labeling = label(image)
print(f"Всего объектов: {labeling.max()}")

struct1 = np.array([[1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0],
                    [1, 1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0]])

result = binary_erosion(image, struct1)
result = binary_dilation(result, struct1)
print(f'struct1: {label(result).max()}')

image -= result

struct2 = np.array([[1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0]])

result = binary_erosion(image, struct2)
result = binary_dilation(result, struct2)
print(f'struct2: {label(result).max()}')

image -= result

struct3 =  np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]])

result = binary_erosion(image, struct3)
result = binary_dilation(result, struct3)
print(f'struct3: {label(result).max()}')

image -= result

struct4 = np.array([[1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]])

result = binary_erosion(image, struct4)
result = binary_dilation(result, struct4)
print(f'struct4: {label(result).max()}')

image -= result

struct5 = np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]])

result = binary_erosion(image, struct5)
result = binary_dilation(result, struct5)
print(f'struct5: {label(result).max()}')

image -= result

plt.imshow(image)
plt.show()
