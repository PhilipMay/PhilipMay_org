# Pandas Data Format and Compression

:::{post} 2024-07-02
:::

This is a systematic comparison of the most important [pandas](https://pandas.pydata.org/docs/)
data formats (CSV,
[Parquet](https://parquet.apache.org/docs/) with [PyArrow](https://arrow.apache.org/docs/python/) backend and
[Feather](https://arrow.apache.org/docs/python/feather.html)) and
different compression methods respectively compression levels.
The comparison is based on the compression ratio and the time it takes to save and load the data.
Factors such as RAM usage are not considered.

For better transparency, the data and the Jupyter notebooks are stored in a
[GitHub repository](https://github.com/PhilipMay/pandas_compression).

:::{figure} /\_static/img/blog-2024/pandas_parquet_feather.png
:width: 550px
:::

## Test Data

Our test data has a size of 785.45 MB in RAM with a table of 363,491 rows and 42 columns. 
The content of the columns is as follows:

- an UUID (string)
- an English text (string)
- 20 columns with random integer values
- 20 columns with random float values

For details see the Notebook called [01_create_dataset.ipynb](https://github.com/PhilipMay/pandas_compression/blob/main/01_create_dataset.ipynb).

## Compression Methods

First, we compare the compression ratio of the different combinations of data format and compression method.
It should be noted that not every compression method is available for every data format.

The compression ratio is a measure that describes how much a file has been reduced in size during the compression process. It is the original file size divided by the compressed file size (higher is better).

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_comp_ratio.svg
:::

In the above graph we see that xz, bz2 and brotli achieve very good results in terms of to the compression ratio.
However, as we also want to compare the times for saving and loading,
the saving time is visualized in the next diagram.

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_save_time.svg
:::

We can see that xz requires an extremely long storage time. bz2 also requires a relatively long time. The storage time of brotli, on the other hand, appears to be relatively good.

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_read_time.svg
:::

The picture for loading times is very similar to that for storage times. xz and bz2 take quite a long time. Brotli is relatively fast.

Without considering the compression options, the conclusion would now be that brotli is the best compression method.
For this reason, we want to compare different compression levels next. In particular those for zstd and lz4.

## Compression Levels

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_comp_ratio_feather.svg
:::

We see that zstd with a compression level of 10 reaches the compression ratio of brotli.
This applies to both Feather and Parquet.
Regardless of the compression level, lz4 compression cannot achieve the compression ratio of brotli.

In the next 2 diagrams, we will now also compare the storage and loading times.

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_save_time_feather.svg
:::

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_bar_read_time_feather.svg
:::

In the two diagrams above we can clearly see that both the loading and
saving times of zstd with compression level 10 are faster than those of brotli.

Our finding so far is that zstd achieves the best values for compression ratio and
storage/loading time by specifically setting the compression level.

Now let's compare the properties of the different zstd compression levels in detail.

## Zstd Compression Levels in Detail

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_scatter_comp_ratio_feather.svg
:::

For the Feather format, the curve of compression level and compression ratio is almost linear.
Remarkably, this is not the case for Parquet.
With Parquet, the curve has an elbow between 5 and 10.
After that it almost starts to plateau but has another step from 15 to 16.

Compression seems to work more efficiently for the Feather format than for Parquet.

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_scatter_save_time_feather.svg
:::

Regardless of the data format, the storage times are very low and
almost constant up to a compression level of 12.
From a compression level of 13, the storage times increase significantly.

:::{figure} https://raw.githubusercontent.com/PhilipMay/pandas_compression/main/plots/pandas_ff_scatter_read_time_feather.svg
:::

The loading time curves are relatively bumpy.
The reason could be that the hard disk is the bottleneck at low compression rates.
Then at very high compression rates the CPU starts to be the bottleneck for Parquet but not for Feather.
In general, the loading time for Feather is significantly shorter than for Parquet.

Overall, it can be assumed that the course of this curve depends very strongly on the speed of the hard disk used.
However, values between 10 and 15 seem to provide the best values in terms of loading speed for both Parquet and Feather.

## Further Considerations

### PyArrow vs. fastparquet

For this evaluation, we deliberately chose [PyArrow](https://arrow.apache.org/docs/python/)
over [fastparquet](https://fastparquet.readthedocs.io/en/latest/) as the backend.
There are 2 reasons for this:

1. Pandas 3.0 will add PyArrow as a required dependency (see [here](https://pandas.pydata.org/docs/whatsnew/v2.1.0.html#pyarrow-will-become-a-required-dependency-with-pandas-3-0))
2. fastparquet was deprecated in dask 2024.1.0 (see [here](https://docs.dask.org/en/stable/changelog.html#v2024-1-0))

### CSV Data Format

Since we often store more complex data such as lists and dictionaries in the cells of our pandas DataFrames, CSV does not appear to be a really sensible alternative.
For this reason, only Parquet and Feather appear to be really useful data formats for us.

## Conclusion

If you consider the compression method together with the compression level,
then zstd is the best option.
This is especially true for compression levels from 10 to 12.

In terms of data format, Feather seems to be the better choice.
Feather has a better compression ratio than Parquet.
Up to a compression level of 12, the storage times of Parquet and Feather are virtually the same.
The loading times of Feather are definitely and significantly better than those of Parquet.

For these reasons, Feather appears to be the best choice in combination with zstd and a compression level of 10 to 12.

## Examples

Here are two concrete examples of how you can save the pandas DataFrames in the various formats and compression levels.
This is particularly good to know because the documentation for the `compression_level` parameter is somewhat hidden.

```python
# Feather:
df.to_feather("filename.feather", compression="zstd", compression_level=10)

# Parquet:
df.to_parquet("filename.parquet", compression="zstd", compression_level=10, index=False)
```
