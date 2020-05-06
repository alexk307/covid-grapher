# covid-grapher
Graph Covid-19 Trends by U.S. Counties. Uses [New York Times data](https://github.com/nytimes/covid-19-data) and [Plotly](https://plotly.com/python/).


```
>  python generate.py --help
Usage: generate.py [OPTIONS]

Options:
  --state TEXT   State in the US  [required]
  --county TEXT  County in the US  [required]
  --graph TEXT   cases | deaths
  --help         Show this message and exit.
```

Example:

```
> python generate.py --state illinois --county cook
```

![](example.png)
