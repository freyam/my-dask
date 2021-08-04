import dask.dataframe as dd

df = dd.demo.make_timeseries(
    start="2000",
    end="2015",
    dtypes={"A": float, "B": int},
    freq="5s",
    partition_freq="3M",
    seed=1234,
)
df = df.shuffle(1000)
# df = df.A.cumsum().resample("1w").mean()

df.dask.visualize()
