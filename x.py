import dask.array as da

XL = da.ones((67552, 365941), chunks=(652, 5792))
XL2 = XL.T.astype("f4")
XC = da.ones((365941, 26), chunks=(365941, 26))
LS = da.linalg.lstsq(XC, XL2)[0]
XC_LS = XC @ LS
XLP = XL2 - XC_LS

XLP.dask.visualize(color="layer_type")
