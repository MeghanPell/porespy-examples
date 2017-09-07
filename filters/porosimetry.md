# Porosimetry

The following recipe illustrates how to simulate mercury intrusion porosimetry on an image using the ``porosimetry`` filter.  The PoreSpy implementation is equivalent to 'morphological image opening' of [Hilpert et al](<https://doi.org/10.1016/S0309-1708(00)00056-7>).  PoreSpy's implementation uses distance transforms instead of morphological operations so it is generally faster, especially for larger sphere sizes since binary opening slows down with larger structuring elements.  

Start by importing the necessary packages:

``` python
import porespy as ps
import matplotlib.pyplot as plt

```

Generate an artificial 2D image for illustration purposes:
``` python
im = ps.generators.blobs(shape=[400, 400], porosity=0.6, blobiness=2)
plt.imshow(im)
plt.axis('off')

```

![](https://i.imgur.com/aFynH6W.png)

Apply the ``porosimetry`` filter to the image both with and without ``access_limited`` applied:

``` python
mip = ps.filters.porosimetry(im, access_limited=True)
local_t = ps.filters.porosimetry(im, access_limited=False)
plt.subplot(1, 2, 1)
plt.imshow(mip)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(local_t)
plt.axis('off')

```

![](https://i.imgur.com/1LAh5XJ.png)

Finally, the images produced by the filter can be passed to the ``pore_size_distribution`` function in the ``metrics`` module to produce numerical data of the pore volume vs. sphere radius:

``` python
mip_data = ps.metrics.pore_size_distribution(mip)
local_t_data = ps.metrics.pore_size_distribution(local_t)
plt.plot(*mip_data, 'b.-', label='mip')
plt.plot(*local_t_data, 'r.-', label='local_thickness')
plt.legend()
```

![](https://i.imgur.com/oCaER4n.png)
