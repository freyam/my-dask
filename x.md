# Update

![](https://user-images.githubusercontent.com/62539811/129021356-37018144-0d62-4eca-862f-a13eff322ff1.png)

## Color Scheme

```py
layer_colors = {
    "DataFrameIOLayer": "purple",
    "ShuffleLayer": "rose",
    "SimpleShuffleLayer": "rose",
    "ArrayOverlayLayer": "pink",
    "BroadcastJoinLayer": "blue",
    "Blockwise": "green",
    "BlockwiseLayer": "green",
    "BlockwiseCreateArray": "green",
    "MaterializedLayer": "gray",
}
```

## Explanation

- `DataFrameIOLayer`: inefficient;
- `ShuffleLayer`, `SimpleShuffleLayer`: inefficient;
- `ArrayOverlayLayer`: inefficient;
- `BroadcastJoinLayer`: (?);
- `Blockwise`, `BlockwiseLayer`, `BlockwiseCreateArray`: efficient; easy to parallize;
- `MaterializedLayer`: inefficient; better to materialize as late as possible;

#### Key Points

- Blockwise Layers are more efficient than others and can be readily parallelized. As a result, they are **green** (a color used to signify something that is right, something that is correct). When users see a green layer, they may be certain that it is the most efficient method to accomplish things and that no optimization is required.
- The **gray** color (which signifies neutrality and balance) is used for Materialized layers to indicate that the layer should be materialized as late as feasible. Since we are not sure of the optimal way to optimize , we use the **gray** color to indicate that we are not sure.
- All of the other levels are inefficient in some way. As a result, they are colored brighter and stronger to attract the user's attention. Colors such as **purple**, **pink**, and **blue** are used to indicate to the user that something needs to be optimized. Users should utilize as little of these levels as feasible.
