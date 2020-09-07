"""
draw.py 
=============================================

.. moduleauthor:: Lilian MAREY <lilian.marey@ensae.fr>

"""
# Packages import
import numpy as np
from matplotlib import pyplot as plt
from random import random
from time import time


##########################################
# Helper function

def random_sign():
    """Returns -1 or 1 with same probability
       
    Returns:
    --------
        Val : int
            1 or -1
    """
    if random()>0.5:
        val = 1
    else:
        val = -1

    return val


##########################################
# Final drawing function

def create_random_drawing(
        N = 1500, 
        constant = 10,
        x_noise_coef = .00002, 
        y_noise_coef = .00001,
        x_amplification = 1,
        y_amplification = 1,
        ):
    """Computes and saves in /images folder a randomly generated drawing

    Parameters:
    -----------
        N : int
            number of dots
        constant : float
            constant noise value
        x_noise_coef : float
            asumed to be positive, coefficient in x exponential noise term
        y_noise_coef : float
            asumed to be positive, coefficient in y exponential noise term
        x_amplification : float
            asumed to be positive, coefficient to which x noise power is raised 
        y_amplification : float
            asumed to be positive, coefficient to which y noise power is raised 
       
    Returns:
    --------
        None
            The function only saves the drawing in /images/ 
    """
    # Setting starting point
    x1, y1 = 0, 0

    # Red part
    for i in range(N // 3):

        x2 = x1 + constant * random_sign() * np.exp(-i * N // 3 * x_noise_coef) * random() ** (2 * x_amplification)
        y2 = y1 + constant * random_sign() * np.exp(-i * N // 3 * y_noise_coef) * random() ** (2 * y_amplification)

        plt.plot(
            [x2],
            [y2],
            'o',
            linestyle = 'dashed',
            markersize = 4 * random() / (1 + 0.0015 * i),
            color = [0.95 *  random() ** 1,
                    .39 *  random() ** 1,
                    .01 *  random() ** 1
                    ]
                )

        x1, y1 = x2, y2

    # Green part
    for i in range(N // 3):

        x2 = x1 + constant * random_sign() * np.exp(-i * N // 3 * x_noise_coef) * random() ** (2 * x_amplification)
        y2 = y1 + constant * random_sign() * np.exp(-i * N // 3 * y_noise_coef) * random() ** (2 * y_amplification)

        plt.plot(
            [x2],
            [y2],
            'o',
            linestyle = 'dashed',
            markersize = 4 * random() / (1 + 0.0015 * i),
            color = [0.01 *  random() ** 1,
                    .95 *  random() ** 1,
                    .39 *  random() ** 1
                    ]
                )

        x1, y1 = x2, y2

    # Blue part
    for i in range(N // 3):

        x2 = x1 + constant * random_sign() * np.exp(-i * N // 3 * x_noise_coef) * random() ** (2 * x_amplification)
        y2 = y1 + constant * random_sign() * np.exp(-i * N // 3 * y_noise_coef) * random() ** (2 * y_amplification)

        plt.plot(
            [x2],
            [y2],
            'o',
            linestyle = 'dashed',
            markersize = 4 * random() / (1 + 0.0015 * i),
            color = [0.39 *  random() ** 1,
                    .01 *  random() ** 1,
                    .95 *  random() ** 1
                    ]
                )

        x1, y1 = x2, y2

    # Saving the drawing
    plt.savefig(
        'images/image_' + 
        str(
            time()
            ) +
        '.png',
        format = 'png')


##########################################
# Lets run the function

create_random_drawing()
    