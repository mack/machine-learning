# Notebook
So... uh... theres a lot of cluttered junk in here. This is mostly just me testing out something quickly. Theres not much worthy content here, but once in a while I might test out something I find cool. So to fight the clutter material, I'll post somethings I want to share here.

## PCA (dimensionality reduction)
[PCA.py](PCA.py/)
Principle component analysis, PCA, is a dimensionality reduction technique. To my understanding it lets people visualize multi-dimensional data in lower dimensions, while withholding the important information.

To accomplish this...
* I first normalized my data to prevent from one principle component being so much greater due to it's data.
* Then I computed the eigen values and vectors from the normalized matrix
* Then I sorted the pairs by the eigen values
* Then I dropped the vectors with the lower eiganvalues
* Now when I matrix multiple the eigen vectors and my data, it reduces the dimensions
to the number of eigenvectors.

I performed the tests on the iris dataset.

Here is a preview of the data... (I dropped the class column for my matrix)
<p align="center">
  <img src="https://i.imgur.com/yQNicaU.png" alt="Current"/>
</p>

Then after PCA, here is the data plotted in two dimensions.
<p align="center">
  <img src="https://i.imgur.com/Z8IuFQV.png" alt="Current"/>
</p>

####TODO
I plan on trying to perform classification on the PCA data to compare the results with just classifying the regular matrix.
