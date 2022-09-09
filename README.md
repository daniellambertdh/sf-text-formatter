# Salesforce text formatter for Big query and config files

[Salesforce Text Formatter - Pypi](https://pypi.org/project/Text-Formatter-sf/)

`pip install Text-Formatter-sf`

--------------------

### SQL formatter 

All you have to do is instantiate the SQLFormatter class with the config_object argument.

`SqlFormatter(config_object)`

Please pass a dictionary in and you can use the pseudo code below as an example.

`config_object = {  'fields': ['List of fields : list'],  
    
    'object': "Object name here : str",  
    
    'object_abreviation': "object abreviation goes here (e.g. opp) : str"       }`
