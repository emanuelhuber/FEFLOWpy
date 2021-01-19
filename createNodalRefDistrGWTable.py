# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:58:26 2020

@author: gwm-user
"""


# require:
#    import ifm_contrib as ifm
#    from ifm import Enum
import math

def createNodalRefDistrGWTable(doc, name):
    """Create a nodal reference distribution containing the groundwater table
    
    Parameters
    ----------
    doc : ifm doc
        FEM or DAC file
    name : character
        Name of the nodal reference distribution
    
    Returns
    -------
    nothing
    """
    #Here we creating the new User Data for Free Surface Node Distribution
    if doc.getNodalRefDistrIdByName(name) == -1:
        doc.createNodalRefDistr(name)
    else:
        # if the nodal reference distribution does exist, we delete it
        # and re-create it!
        idND = doc.getNodalRefDistrIdByName(name)
        doc.deleteNodalRefDistr(idND)
        doc.createNodalRefDistr(name)

    idND = doc.getNodalRefDistrIdByName(name)
    #print 'Number of nodes: ' + str(doc.getNumberOfNodesPerSlice())
    #print 'Number of Slices: ' + str(doc.getNumberOfSlices())
    #getting number of slices for model
    NSlices=doc.getNumberOfSlices()
    #getting number of nodes per slice
    Nodes=doc.getNumberOfNodesPerSlice()
    
    #loop for all layer nodes
    for ND in range(0,Nodes):
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
                if (not math.isnan(doc.getResultsFlowHeadValue(node))):
                    doc.setNodalRefDistrValue(idND,ND,doc.getResultsFlowHeadValue(node))
            if(math.isnan(p_prev) and p>=0):
                #check if previous slice was inactive
                doc.setNodalRefDistrValue(idND,ND,doc.getResultsFlowHeadValue(node))


