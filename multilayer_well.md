# Multilayer well (MLW)

Note: load FEFLOW file `doc = ifm.loadDocument(FILE_FEM)`

## Number of multilayer wells

```py
doc.getNumberOfMultiLayerWells()
```

## find node number corresponding to multilayer well

```py
for node in range(0, doc.getNumberOfNodes()):
    myval = doc.getBcFlowType(node)
    if myval == 4:
        well_node = node
        print(format(myval))
```

## Get info about the multillayer well

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

Get **constant** multilayer well attributes with `getMultiLayerWellAttrValue(int: nID, int: nAttr)`

* `nID` (*int*) = MLW ID (not related to node index, start at 0)
* `nAttr`(*int*) = 
    * `0` = Well rate value [m^3/d].
    * `1` = Minimum hydraulic head constraint value [m^3/d] or NaN if n/a.
    * `2` = Maximum hydraulic head constraint value [m^3/d] or NaN if n/a.

```py
doc.getMultiLayerWellAttrValue(0, 0)
```
