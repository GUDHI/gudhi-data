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
| [Stanford bunny](points/bunny/bunny.off) | [Stanford University](http://graphics.stanford.edu/data/3Dscanrep/) | [OFF file](https://en.wikipedia.org/wiki/OFF_(file_format)) with 35947 points in 3d and 69451 triangles |
| [Spiral 2D](points/spiral_2d/spiral_2d.csv) | Generated within GUDHI | CSV file with 114562 points in 2d |
| [Daily and sports activities](points/activities/activities.csv.xz) | [UC Irvine ML repository](https://archive.ics.uci.edu/ml/datasets/daily+and+sports+activities) - [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) | CSV file compressed in a `xz` format |
