# Salesforce text formatter for Big query and config files

[Salesforce Text Formatter - Pypi](https://pypi.org/project/Text-Formatter-sf/)

`pip install Text-Formatter-sf`

--------------------

### SQL formatter 

All you have to do is instantiate the SQLFormatter class with the config_object argument.

`SqlFormatter(config_object)`

Please pass a dictionary in and you can use the pseudo code below as an example.

```
sql_object = {  
    'fields': ['List of fields : list'],  
    'object': "Object name here : str",  
    'object_abreviation': "object abreviation goes here (e.g. opp) : str"
    }
```

Example
```
sql_object = {
    'fields': ['lease_termination_one_off__c', 'lease_termination_due_rent__c', 'reverse_to_original_contiditons__c', 'cost_of_reversal__c', 'stock_transfer_cost__c', 'shrinkage_cost__c', 'personnel_costs__c', 'other_costs__c', 'additional_comments__c', 'equipment_relocated__c', 'equipment_stored__c', 'equipment_related_costs__c', 'closure_date__c', 'handover_date__c', 'closure_reason__c', 'reopening_date__c', 'is_temporarily_closing__c'],
    'object': "AgentWork",
    'object_abreviation': "acc",  
}
```
### Yaml config formatter


```
yaml_object = {
    'object_name' : "Object name here : str",
    'table_description' : "Table Description goes here : str",
    'filter_by_country_and_entity' : "True or False : Boolean",
    'field_list' : ['List of fields : list']
}
```

Example
```
yaml_object = {
    'object_name' : "AgentWork",
    'table_description' : "Salesforce VRM AgentWork",
    'filter_by_country_and_entity' : False,
    'field_list' : ['lease_termination_one_off__c', 'lease_termination_due_rent__c', 'equipment_relocated__c', 'equipment_stored__c', 'equipment_related_costs__c', 'closure_date__c', 'handover_date__c', 'closure_reason__c', 'reopening_date__c', 'is_temporarily_closing__c']
}
```
