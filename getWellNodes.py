def getWellNodes(doc):
    """Return the nodes corresponding to multi-layer and single wells
    
    Parameters
    ----------
    doc : ifm doc
        FEM or DAC file
   
    Returns
    -------
    two-component list: 1. multi-layer nodes; 2. singel well nodes
    """
    MLW = [] # multi-layer wells
    SW = []  # single wells
    for node in range(0, doc.getNumberOfNodes()):
        myval = doc.getBcFlowType(node)
        if myval == 4:
            SW.append(node)
        myval2 = doc.queryMultiLayerWellInfo(node)
        if myval2 != None:
            MLW.append(node)
    return [MLW, SW]
