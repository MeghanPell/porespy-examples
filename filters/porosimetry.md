# Porosimetry

``` python
import porespy as ps
import scipy as sp
import scipy.ndimage as spim
import matplotlib.pyplot as plt

```

``` python
im = ps.generators.blobs(shape=[400, 400], porosity=0.6, blobiness=2)
plt.imshow(im)
plt.axis('off')

```

![](https://i.imgur.com/aFynH6W.png)

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

``` python
mip_data = ps.metrics.pore_size_distribution(mip)
local_t_data = ps.metrics.pore_size_distribution(local_t)
plt.plot(*mip_data, 'b.-', label='mip')
plt.plot(*local_t_data, 'r.-', label='local_thickness')
plt.legend()
```

![](https://i.imgur.com/oCaER4n.png)
