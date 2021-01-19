# Discrete Fracture Elements

**TODO**: function to compute (i) the Cross-sect. Area and (ii) the Hydraulic aperture as a function of the well Radius

## Get Coordinates

```py
n_df = doc.getNumberOf1DFractureElements()
if n_df > 0:
    df_x = []
    df_y = []
    for q in range(0, n_df):
        ij = doc.getNodalArrayOfFractureElement(q)
        df_x.append(doc.getX(ij[0]))
        df_y.append(doc.getY(ij[0]))
        df_x.append(doc.getX(ij[1]))
        df_y.append(doc.getY(ij[1]))
```

## Get and set Fracture Area

```py
# get
fracArea = doc.getFracArea(0, 0, 0, 1)
# set
for elt in range(0, doc.getNumberOf1DFractureElements()):
    myval = doc.setFracArea(elt, 0.34, 0, 0, 1)
```
