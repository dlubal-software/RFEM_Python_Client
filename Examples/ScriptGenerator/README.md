# How to use the script generators
Both the WSScriptSenerator and XMLScriptGenerator examples are intended for users who want to obtain a copy of the RFEM model in the form of an executable script. It reads all data stored in the model and creates scripts, reducing development time to a minimum. The examples use 2 sources. Either XML generated from RFEM or Web Services. Prerequisite is to set the correct model name.

Running both examples will generate a complete script with the necessary components. The script also contains begin_modification, finish_modification and creating a model with a default name. Empty values or lists and null values are deleted.
