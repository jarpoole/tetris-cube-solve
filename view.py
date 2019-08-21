#https://terbium.io/2017/12/matplotlib-3d/

#To install:
# python -m pip install -U pip
# python -m pip install -U matplotlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pickle

from mpl_toolkits.mplot3d import Axes3D

fig = None

def make_ax(grid=False):
    global fig
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(grid)
    return ax

def displayPieces(pieces):
    finalVolume = np.array([[[0 for col in range(4)]for row in range(4)] for x in range(4)])
    for piece in pieces:
        finalVolume = finalVolume | piece.volume

    colors = np.empty(finalVolume.shape, dtype=object)

    for piece in pieces:
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if piece.volume[x][y][z] == 1:
                        colors[x,y,z] = piece.color

    mpl.rcParams['toolbar'] = 'None'
    ax = make_ax(True)
    
    ax.voxels(finalVolume, facecolors=colors, edgecolors='black')
    
    plt.show()
    return ax

def displayArray(volume):
    mpl.rcParams['toolbar'] = 'None'
    ax = make_ax(True)
    color = np.where(volume, '#FFD65DC0', '#7A88CCC0')
    ax.voxels(volume, facecolors=color, edgecolors='black')
    
    plt.show()
