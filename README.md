# mplheatmap
Convenience utility to create interpolated 2d heatmaps.
Creates a two-dimensional color-coded "heat map" plot on a matplotlib axis from a pandas DataFrame. The API is
designed to mimic seaborn functions.

## Installation
Install via pip:
```
pip install mplheatmap
```
or clone the repository and run:
```
python -m setup.py
```

## Example usage

Suppose we have a pandas Dataframe `df`, which contains a response variable in the columns `z` as a function
of two input variables `x` and `y`. The DataFrame contains measured points in the parameterspace z(x, y). 
This module interpolates the data and plots it onto a matplotlib axis as a heatmap, where `z` is colorcoded
as a function of `x` and `y` in a rectangular space.

    from mplheatmap import heatmap
    ax = heatmap(data=df, x='x', y='y', z='z', xlabel='x-variable (unit)', ylabel='y-variable (unit)', 
                 zlabel='z-variable (unit)', cmap='jet', show_points=True)
    ax.figure.savefig('test.png', dpi=300, bbox_inches='tight')

<img src="https://github.com/fredericjs/mplheatmap/assets/63259596/31f2beb2-ffe1-4148-a71f-3e20c224cf5d" width="50%" />

## Docs
The following parameters are accepted by `heatmap`:

    Parameters
    ----------
    data: pandas.Dataframe
        A pandas DataFrame object containing the data for x, y and z parameters.
    x: str
        The name of the column in the 'data' Dataframe containing the x values
    y: str
        The name of the column in the 'data' Dataframe containing the y values
    resolution: int, optional.
        Number of interpolation points in x and y. Defaults to 300.
    aspect_ratio: float, optional
        Aspect ratio of the imshow plot. Defaults to 1.
    cmap: str or matplotlib.colors.Colormap, optional
        The colormap to use for the imshow plot and colorbar. Defaults to 'jet'.
    ax: matplotlib Axes, optional
        Axes object to draw the plot onto, otherwise uses the current Axes.
    show_points: bool, optional
        Specifies whether to show the actual datapoints using a scatterplot.
        Defaults to True.
    colorbar: bool, optional
        Specifiees whether to show a colorbar. Defaults to True.
    cbar_width: float, optional
        Width of the colorbar in axes coordinates. Defaults to 0.03.
    cbar_pad: float, optional
        Space between plot and colorbar. Defualts to 0.01.
    xlabel: str, optional
        Label to show on the x-axis. Defaults to the value of 'x'.
    ylabel: str, optional
        Label to show on the y-axis. Defaults to the value of 'y'.
    zlabel: str, optional
        Label to show on the z-axis. Defaults to the value of 'z'.
    zlabel_inside: bool, optional
        If True, puts the z-label inside the colorbar. If False, puts the zlabel
        outside the colorbar.
    title: str, optional
        Title of the plot. Defualts to None.
    vmin: float, optional
        Defines the minimum of the datarange in the plot. Defaults to the minimum
        of 'z' values.
    vmax: float, optional
        Defines the maximum of the datarange in the plot. Defaults to the maximum
        of 'z' values.
    imshow_kwargs: dict, optional
        Keyword arguments to pass the the imshow function responsible for plotting the
        colorplot. Default values will be overwritten.
    scatter_kwargs: dict, optional
        Keyword arguments to pass the the scatter function responsible for plotting the
        datapoints. Default values will be overwritten.
    
    Returns
    -------
    ax: matplotlib Axes
        The Axes object containing the plot.

