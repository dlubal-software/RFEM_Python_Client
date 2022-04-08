# RFEM Python High Level Function Library

## Project Description
**Webservice and API**  is a programmable  interface  for RFEM 6 . Based on this technology, the program RFEM 6 provide a server service that can be used locally or via the network. The client-server communication allows you to send requests to and receive feedback from RFEM 6 .

High-level libraries are available for the Python and C# programming languages, which allow easy and intuitive use of web services. The high-level libraries are available on  [**GitHub under an open source license**](https://github.com/Dlubal-Software/RFEM_Python_Client). They can be used free of charge and adapted to your specific needs. Contributions to our repositories are always welcome.

## Example
```
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.enums import NodalSupportType, LoadDirectionType
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
```
## API Documentation

Visit our [GitHub page](https://dlubal-software.github.io/RFEM_Python_Client/)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
