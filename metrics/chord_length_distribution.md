# Chord Length Distributions

## Import Packages

``` python
import porespy as ps
import matplotlib.pyplot as plt

```

## Generate Artificial Image

``` python
im = ps.generators.blobs(shape=[600, 600], blobiness=2, porosity=0.6)
plt.imshow(im)
plt.axis('off')

```
![](https://i.imgur.com/pmcS4z7.png)

## Apply Chords Using Filter and Analyze

``` python
chords = ps.filters.apply_chords(im, spacing=1)
d = ps.metrics.chord_length_distribution(im=chords)

```
Note in this image that chords connected to the edge have been removed.  These chords are unnaturally shortened so could skew the distribution.  These chords can be preserved by setting the ``trim_edges`` argument to ``False`` in the call to ``apply_chords``.   Also, the spacing between the yellow chords is adjustable.  These chords must have a least 1 blank (purple) voxel between them, but this value can be increased using the ``spacing`` argument.  

![](https://i.imgur.com/FftGDem.png)

## Plot the Results

``` python
x = d.chord_length_bins
plt.subplot(1, 2, 1)
plt.plot(x, d.differential_chord_count, 'r-o', label='number weighted')
plt.subplot(1, 2, 1)
plt.plot(x, d.differential_chord_length, 'b-o', label='length weighted')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(x, d.cumulative_chord_count, 'r-o', label='number weighted')
plt.subplot(1, 2, 2)
plt.plot(x, d.cumulative_chord_length, 'b-o', label='length weighted')
plt.legend()

```
The following results are noisy since the number of chords in a 2D image is not large enough to provide a good statistical distribution.

![](https://i.imgur.com/dYuQbXL.png)
