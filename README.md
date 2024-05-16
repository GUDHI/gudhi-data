# gudhi-data

These datasets are used as examples, for benchmark purposes and in gudhi python data fetch methods.

Do not hesitate to submit a pull request with new model data and sources or to submit an issue of a "wanted" dataset.

## License

The [root LICENSE file](LICENSE) applies to all datasets, except if another license file is located in a dataset
directory, then it applies to the datasets in this same directory and subdirectories.

For instance, [Stanford bunny LICENSE](points/bunny/LICENSE) applies to [Stanford bunny point cloud](points/bunny/).

## Point clouds

| Model Name | Source | Description |
|------------|--------|-------------|
| [Stanford bunny](points/bunny/bunny.off) | [Stanford University](http://graphics.stanford.edu/data/3Dscanrep/) | [OFF file](https://en.wikipedia.org/wiki/OFF_(file_format)) with 35947 points in $\mathbb{R}^3$ and 69451 triangles |
| [Spiral 2D](points/spiral_2d/spiral_2d.csv) | Generated within GUDHI | CSV file with 114562 points in $\mathbb{R}^2$ |
| [Daily and sports activities](points/activities/activities_p1_left_leg.csv) | [UC Irvine ML repository](https://archive.ics.uci.edu/ml/datasets/daily+and+sports+activities) - [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) | CSV file with 30000 points in 3d + activity type column |
| [SO3](points/SO3/SO3_50000.off) | The SO3 points clouds have been generated with [the ISOI software](https://mitchell-web.ornl.gov/SOI/index.php) | [OFF file](https://en.wikipedia.org/wiki/OFF_(file_format)) with 50000 points in $\mathbb{R}^9$ |

## Time Series

| Model Name | Source | Description                                                                                                                                                                           |
|------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Topological Wheels](timeseries/topological-wheels/tw-data-annotated.png) | [DataShape](https://www.inria.fr/fr/datashape) | 10 CSV files where each file has 64 timeseries over 10000 timestamps each, and a $y$ ground truth indicating anomalous regime. See [README](timeseries/topological-wheels/README.md). |
