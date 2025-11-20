# Module for using prompt templates to define RFEM 6 models

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

_INTRODUCTION_TPL = read_file("templates/introduction.txt")
_MATERIAL_TPL = read_file("templates/Material.txt")
_Geometry_TPL = read_file("templates/Geometry.txt")
_CrossSection_TPL = read_file("templates/crosssection.txt")
_LOAD_TPL = read_file("templates/load.txt")
_SOLVER_TPL = read_file("templates/solver.txt")
_RESULTS_TPL = read_file("templates/results.txt")

_keywords = {
    'INTRO':_INTRODUCTION_TPL,
    'MATERIAL': _MATERIAL_TPL,
    'GEOMETRY':_Geometry_TPL,
    'CROSSSECTION':_CrossSection_TPL,
    'LOADS': _LOAD_TPL,
    'SOLVER': _SOLVER_TPL,
    'RESULTS': _RESULTS_TPL,
    }


# Process prompt to use template if applicable
# The template keyword shall be specified at the beginning of the prompt with a semicolon
# Example:
# MATERIAL: My model...

def process_prompt(prompt):
    if ':' not in prompt:
        return prompt
    key, value = prompt.split(':', 1)
    if key not in _keywords:
        return prompt
    return _keywords[key].format(placeholder=value)