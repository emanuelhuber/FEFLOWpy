# FEFLOWpy
Python code for FEFLOW pre- and post-processing. Check also:

- [IFM API documentation](https://dhi.github.io/ifm/)

    Check also 
    - the section "Tutorial" for the new features
    - the section "Examples" for inspiration
- [FEFLOW documentation: IFM function index, callbacks, constant, etc.](http://www.feflow.info/html/help74/feflow/13_Programming/IFM/API/appendix_b_index.html)
- [DHI Developers (Internal) ](https://dhi-developer-documentation.azurewebsites.net/engine_libraries/feflow/feflow_and_python/)
- [ifm contrib](https://github.com/DHI/ifm_contrib)

## IFM model properties

Get the list of IFM model properties:

```py
dir(ifm.Enum)
```

### List of Parameter Values

Available functions:

```py
getParamSize()
getParamValue()
getParamValues()
setParamValue()
setParamValues()
enableParamRecording()
```

## BC conditions
```py
{c: getattr(ifm.Enum, c) for c in dir(ifm.Enum) if c.startswith("P_BC")}
```

