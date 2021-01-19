# Well and multi-layer wells(MLW)

Note: load FEFLOW file `doc = ifm.loadDocument(FILE_FEM)`

## Well and MLW Nodes

* Get the well and MLW nodes with the self-made function `getWellNodes()`
* Get the flow budget:
    ```py
    doc.startSimulator(FILE_DAC, 0)
    well_nodes = getWellNodes(doc)
    bdgt = doc.budgetCompute(0, well_nodes[0] + well_nodes[1], True)
    # bdgt[11] for extraction; bdgt[10] for injection... ????
    Q_eff = (bdgt[11] + bdgt[10])* 1000 / (24 * 3600)
    ```

## Singel Wells

* Get flow rate:
    ```py
    doc.getBcFlowValue(node)
    ```
* Set flow rate *Q*:
    ```py
    doc.setBcFlowValueAtCurrentTime(node, Q)
    ```
* Get constraint (here min-head constraint):
    ```py
    doc.getBccFlowValue(node, 0)
    ```
* Set constraint (here min-head constraint *h*):
    ```py
    doc.setBccFlowValueAtCurrentTime(node,  h, 0)
    ```
      

## MLW properties

Note: the MLW have an indexing not based on the node number but on the number of MLW (indexing start at 0).

### Number of multilayer wells

```py
doc.getNumberOfMultiLayerWells()
```

### Get *geometry* info about the multillayer well

Here `well_node` is the node number (integer) of the multilayer well.

```py
well_info = doc.queryMultiLayerWellInfo(well_node)
```

Here is the list of attributes (`dir(well_info)`):

```py
well_info.getBottomElevation()
well_info.getBottomNode()
well_info.getId()
well_info.getName
well_info.getRadius()
well_info.getTopElevation()
well_info.getTopNode()
```

Get the coordinates of the MLW *i* (indexing start at *0*):

```py
MLW_node = doc.getMultiLayerWellTopNode(i)
MLW_xy = [doc.getX(MLW_node), doc.getY(MLW_node)]
```

### Constant MLW attributes


Get **constant** multilayer well attributes with `getMultiLayerWellAttrValue(nID, nAttr)`

* `nID` (*int*) = MLW ID (not related to node index, start at 0)
* `nAttr`(*int*) = 
    * `0` = Well rate value [m^3/d].
    * `1` = Minimum hydraulic head constraint value [m^3/d] or NaN if n/a.
    * `2` = Maximum hydraulic head constraint value [m^3/d] or NaN if n/a.

```py
doc.getMultiLayerWellAttrValue(0, 0)
print("current well rate = {} m3/d".format(Q_current))
```

Set **constant** multilayer well attributes with `setMultiLayerWellAttrValue(nID, nAttr, dValue)`

* `nID` (*int*) = MLW ID (not related to node index, start at 0)
* `nAttr`(*int*) = 
    * `0` = Well rate value [m^3/d].
    * `1` = Minimum hydraulic head constraint value [m^3/d] or NaN if n/a.
    * `2` = Maximum hydraulic head constraint value [m^3/d] or NaN if n/a.
* `dValue` (*double*) = attribute value (be careful sign!)

```py
Q_well = -2 * 60 * 60 * 24 / 1000 # l/s
doc.setMultiLayerWellAttrValue(0, 0, Q_well)
Q_new = doc.getMultiLayerWellAttrValue(0, 0)
print("new well rate = {} m3/d".format(Q_new))
```

### Transient MLW attributes

Check if transient with `isMultiLayerWellAttrTransient()`

Get attributes with `getMultiLayerWellAttrTSID()`

Set attributes with `setMultiLayerWellAttrTSID()`
