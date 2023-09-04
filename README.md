# OpiFormAnalysis
Python scripts (mostly as jupyter notebooks) that were used to analyse the simulated data from the opinion formation project with Mitja & Matjaz Steinbacher (Steinbacher et al. 2023). Simulation code can be found in [this repository](https://github.com/pixlifai/opiform).

## Dependencies
The analysis relies mainly on visualisations, which were performed with the standard Python plotting library [Matplotlib](https://matplotlib.org/) (Hunter, 2007), as well as [Seaborn](https://seaborn.pydata.org/) (Waskom, 2021). Data processing and calculations were performed almost exclusively with [NumPy](https://numpy.org/) (Harris et al., 2020). As opinion dynamics were analysed in dependence of five parameters, it was more convenient to use 5-dimensional arrays rather than spreadsheet-style (2D) dataframes, as they would be provided by Pandas. Aggergating over any dimensions in order to isolate the effect of others becomes easy and efficient with this data structure and could be extended to all possible parameters and parameter combinations without much effort. The density of interaction networks, a measure of integration of the society, was calculated with the [NetworkX](https://networkx.org/) (Hagberg et al. 2008) library.

Flow-charts, as e.g. for the classification ranking, or the explanations of the roommate matching algorithm in the appendix were performed with the community version of [Manim](https://www.manim.community/), a Python library for mathematical animations It also produces visually pleasing static images, providing the necessary flexibiblity of design choices, while abstracting away the code to produce actual graphics.

## Organisation of the repository
There are two main versions of the model that we analyse: with and without coherence features in matching and opinion updating. The scripts to analyse the corresponding data are in separate folders ("full_credibility" and "no_credibility") accordingly. Many notebooks can be found in both folders, with slight amendments to fit the respective model version. There should be enough explanatory text to explain what, why and how the code does what it does within those notebooks. The organisation of model output files is explained in separate text files that can be found in the data folders. For both versions, with and without coherence features, we ran the model at sentiment values 0 and 1 (ON and OFF), of which the data can be found in the FIG1-DATA-NEW. After some analysis, we found the results interesting enough to run the model at intermediate values of sentiment as well, the data of that version of the model can be found in the folders M1 and M2. The folder "ManimVisualisations" contains the scripts to produce the non-data images for the paper. The figures were rendered through the command line interface of the Manim package (check documentation for details).

## References
Hagberg, A.A., Schult, D.A.,Swart, P.J., 2008. Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference (SciPy2008)*, Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), pp. 11–15.

Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane, A., del Río, J. F., Wiebe, M., Peterson, P., Gérard-Marchant, P., Sheppard, K., Reddy, T., Weckesser, W., Abbasi, H., Gohlke, C., Oliphant, T. E. (2020). Array programming with NumPy. *Nature, 585*(7825), pp. 357–362. https://doi.org/10.1038/s41586-020-2649-2.

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering, 9*(3), pp. 90–95. https://doi.org/10.1109/MCSE.2007.55.

The Manim Community Developers. (2023). Manim – Mathematical Animation Framework (Version v0.17.3) [Computer software]. https://www.manim.community/.

Steinbacher, M., Steinbacher, M., Knoppe, C. (2023). Opinion dynamics with preference matching: How the desire to meet facilitates opinion exchange. *Computational Economics*. https://doi.org/10.1007/s10614-023-10455-7.

Waskom, M. (2021). Seaborn: statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021.
