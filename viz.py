import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go
import plotly.figure_factory as ff

def plot_candlestick(ohlc, sample='price'):
    candlestick = go.Candlestick(
        x=ohlc.index,
        open=ohlc[(sample, 'open')],
        high=ohlc[(sample, 'high')],
        low=ohlc[(sample, 'low')],
        close=ohlc[(sample, 'close')]
    )
    return go.Figure(data=candlestick)

def show_scatter_plot(x, y):
    t = go.Scatter(x=x, y=y)
    py.iplot([t])

def plot_scatter_df_series(df, title, sep_y_axis=False, y_axis_label='', scale='linear', initial_hide=False):
    label_arr = list(df)
    series_arr = list(map(lambda col: df[col], label_arr))

    layout = go.Layout(
        title=title,
        legend=dict(orientation='h'),
        xaxis=dict(type='date'),
        yaxis=dict(
            title=y_axis_label,
            showticklabels=not sep_y_axis,
            type=scale
        )
    )

    y_axis_config = dict(
        overlaying='y',
        showticklabels=False,
        type=scale
    )
    visibility = True
    if initial_hide: visibility = 'legendonly'

    tarr = []
    for i, series in enumerate(series_arr):
        t = go.Scatter(
            x=series.index,
            y=series,
            name=label_arr[i],
            visible=visibility
        )

        if sep_y_axis:
            t['yaxis'] = 'y{}'.format(i + 1)
            layout['yaxis{}'.format(i + 1)] = y_axis_config
        tarr.append(t)

    return go.Figure(data=tarr, layout=layout)

def plot_pearson_correlation_heatmap(df, title, absolute_bounds=True):
    df = df.pct_change()
    heatmap = go.Heatmap(
        z=df.corr(method='pearson').values,
        x=df.columns,
        y=df.columns,
        colorbar=dict(title='Pearson Coefficient')
    )
    layout = go.Layout(title=title)
    if absolute_bounds:
        heatmap['zmax'] = 1.0
        heatmap['zmin'] = 1.0
    return go.Figure(data=[heatmap], layout=layout)
