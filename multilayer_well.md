# Multilayer well

Note: load FEFLOW file `doc = ifm.loadDocument(FILE_FEM)`

## Number of multilayer wells 

```
doc.getNumberOfMultiLayerWells()
```

## find node number corresponding to multilayer well

```
for node in range(0, doc.getNumberOfNodes()):
    myval = doc.getBcFlowType(node)
    if myval == 4:
        well_node = node
        print(format(myval))
```
