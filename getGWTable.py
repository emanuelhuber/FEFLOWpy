def getGWTable(doc, ti = None):
    """Compute the groundwater table
    
    Parameters
    ----------
    doc : doc
        DAC file
    ti : integer
        time step number
    
    Returns
    -------
    a list of groundwater table height values (length = doc.getNumberOfNodesPerSlice())
    """
    # Get head values of current DAC file for given times
    if ti is not None:
        dacTimes = doc.getTimeSteps()
        doc.loadTimeStep(dacTimes[ti][0])
    
    #idND = doc.getNodalRefDistrIdByName(name)
    NSlices=doc.getNumberOfSlices()
    #getting number of nodes per slice
    Nodes=doc.getNumberOfNodesPerSlice()
    
    gwtlist = [0]*Nodes
    
    #loop for all layer nodes
    for ND in range(0,Nodes):
        # default value
        gwtlist[ND] = doc.getResultsFlowHeadValue(ND)
        #loop for all layers starting with the second layer
        for sl in range (2,NSlices):
            #current slice node:
            node=ND + Nodes*(sl-1)
            #previous slice node:
            node_prev=ND + Nodes*(sl-2)
            #current slice node pressure:
            p = doc.getResultsFlowPressureValue(node)
            #previous slice node pressure:
            p_prev = doc.getResultsFlowPressureValue(node_prev)
            
            #if previous slice pressure <0 and current slice pressure >0 then we get the water table in current node
            if(p_prev<0 and p>=0):
                gwtlist[ND] = doc.getResultsFlowHeadValue(node)
                #if (not math.isnan(doc.getResultsFlowHeadValue(node))):
                #    doc.setNodalRefDistrValue(idND,ND,doc.getResultsFlowHeadValue(node))
            if(math.isnan(p_prev) and p>=0):
                #check if previous slice was inactive
                gwtlist[ND] = doc.getResultsFlowHeadValue(node)
                #doc.setNodalRefDistrValue(idND,ND,doc.getResultsFlowHeadValue(node))
    return(gwtlist)
