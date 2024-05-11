import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from collections import defaultdict # частотный словарик
from pathlib import Path

#процент заполнения массива 1, ищем "-"
def filling_factor(arr): 
    return np.sum(arr) / arr.size 

#функция для определения дырок
def count_holes(region): 
    labeled = label(np.logical_not(region.image)) 
    regions = regionprops(labeled) 
    holes = 0 
    for region in regions: 
        coords = np.where(labeled == region.label) 
        bound = True 
        for y, x in zip(*coords): 
            if (y == 0 or x == 0 or y == labeled.shape[0] - 1 or x == labeled.shape[1] - 1): 
                bound = False 
        holes += bound 
    return holes 

#функция для определения линий
def has_vline(arr, width = 1): 
    return width <= np.sum(arr.mean(0) == 1) 

#главная функция
def recognize(region): 
    if filling_factor(region.image) == 1.0: 
        return '-' 
    else: 
        holes = count_holes(region) 
        if holes == 2: 
            if has_vline(region.image, 3): 
                return 'B' 
            else: 
                return '8' 
        elif holes == 1: 
            ny, nx = (region.local_centroid[0] / region.image.shape[0], region.local_centroid[1] / region.image.shape[1]) 
            if has_vline(region.image, 3): 
                if np.isclose(ny, nx, 0.09): 
                    return 'P' 
                else: 
                    return 'D' 
            if np.isclose(ny, nx, 0.05): 
                return '0' 
            else: 
                return 'A' 
        else: 
            if has_vline(region.image): 
                return '1' 
            else: 
                eccentricity = region.eccentricity 
                frames = region.image 
                frames[0,:] = 1 
                frames[-1,:] = 1 
                frames[:,0] = 1 
                frames[:,-1] = 1 
                holes = count_holes(region) 
                if eccentricity < 0.4:
                    return "*"
                else:
                  match holes:
                    case 2: return "/"
                    case 4: return "X"
                    case _: return "W"
    return '_' 

image = plt.imread("symbols.png").mean(2)

#считаем кол-во символов на изображении
image[image > 0] = 1
regions = regionprops(label(image))
symbols = len(regions)

print(symbols)

result = defaultdict(lambda: 0)
path = Path(".") / "result"
path.mkdir(exist_ok = True)

plt.figure()
for i, region in enumerate(regions):
    symbol = recognize(region)
    if symbol in "DP":
        plt.clf()
        plt.title(f"{symbol=}")
        plt.imshow(region.image)
        plt.tight_layout()
        plt.savefig(path / f"{i}.png")
    result[symbol] += 1
print(result)
//helloo
