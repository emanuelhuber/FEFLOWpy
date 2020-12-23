# Multilayer well

Note: load FEFLOW file `doc = ifm.loadDocument(FILE_FEM)`

## Number of multilayer wells 

```
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

```
well_info = doc.queryMultiLayerWellInfo(well_node)
```
