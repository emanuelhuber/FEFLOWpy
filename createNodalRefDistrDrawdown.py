# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:58:26 2020

@author: gwm-user
"""


# require:
#    import ifm_contrib as ifm
#    from ifm import Enum
import math

def createNodalRefDistrDrawdown(doc, name0, name1, name_new):
    """Create a nodal reference distribution containing the groundwater table
    
    Parameters
    ----------
    doc : ifm doc
        FEM or DAC file
    name0 : character
        nodal reference distribution name of the reference GW table (copmuted with 'createNodalRefDistrGWTable()')
    name1 : character
        nodal reference distribution name of the modified GW table (copmuted with 'createNodalRefDistrGWTable()')
    name_new : character
        nodal reference distribution name of the drawdown data
    
    
    Returns
    -------
    nothing
    """
    doc.createNodalRefDistr(name_new)
    idND_new = doc.getNodalRefDistrIdByName(name_new)
        
    idND1 = doc.getNodalRefDistrIdByName(name1)
    idND0 = doc.getNodalRefDistrIdByName(name0)
    
    n_nodes = doc.getNumberOfNodesPerSlice()
    
    #loop for all layer nodes
    for k in range(0, n_nodes):
        val1 = doc.getNodalRefDistrValue(idND1, k)
        if val1 == -99999:
            val = val1
        else:
            val = doc.getNodalRefDistrValue(idND0, k) - val1
        doc.setNodalRefDistrValue(idND_new, k, val)
        

