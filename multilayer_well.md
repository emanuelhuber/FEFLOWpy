# Multilayer well (MLW)

Note: load FEFLOW file `doc = ifm.loadDocument(FILE_FEM)`

## MLW properties

### Number of multilayer wells

```py
doc.getNumberOfMultiLayerWells()
```

### find node number corresponding to multilayer well

```py
well_node = []
for node in range(0, doc.getNumberOfNodes()):
    node_val = doc.queryMultiLayerWellInfo(node)
        if node_val != None:
            well_node.append(node)
```

### Get info about the multillayer well

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

## Constant MLW attributes


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

## Transient MLW attributes

Check if transient with `isMultiLayerWellAttrTransient()`

Get attributes with `getMultiLayerWellAttrTSID()`

Set attributes with `setMultiLayerWellAttrTSID()`
