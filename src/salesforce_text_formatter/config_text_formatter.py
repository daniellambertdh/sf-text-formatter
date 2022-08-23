#!/usr/bin/python3

# Enter the values for the config_object dictionary and instantiate the object call the curated_data_yaml_formatter() method
# Will return the correct code for yaml file 

class ConfigObject:
    def __init__(self):
        print(""" config_object = {
    'object_name' : "Object name here : str",
    'table_description' : "Table Description goes here : str",
    'filter_by_country_and_entity' : "True or False : Boolean",
    'field_list' : ['List of fields : list']
}""")

class ConfigFormatter:
    def __init__(self, config_object):
        self.clean_object = config_object
        self.clean_object['field_list'] = self.fields_cleanup(
            self.clean_object['field_list']
        )
        self.clean_object['field_list'] = self.create_list(
            self.clean_object['field_list']
        )
        return self.curated_data_yaml_formatter(self.clean_object)

    def fields_cleanup(self, fields):
        fields = str(fields).replace("[", "")
        fields = fields.replace("]", "")
        fields = fields.replace("'", "")
        cleaned_fields = fields.replace(",", "")
        return cleaned_fields

    def create_list(self, old_list):
        self.new_list = old_list.split()
        self.new_list = list(map(str.lower,self.new_list))
        return self.new_list

    def curated_data_yaml_formatter(self, clean_object):
        print(f"""- name: {self.clean_object['object_name'].lower()}
  table_description: {self.clean_object['table_description']}
  is_view: false
  create_shared_view: true""")
        
        if self.clean_object['filter_by_country_and_entity']:
            print(f"""  filter_by_country: true
  filter_by_entity: true 
  entity_id_column: global_entity_id
  columns:  
   - country_code   
   - global_entity_id""")
        else:
            print(f"""  filter_by_country: false  
  filter_by_entity: false
  columns:""")

        for field in self.clean_object['field_list']:
             print(f"   - {field}")


config_object = {
    'object_name' : "AgentWork",
    'table_description' : "Salesforce VRM AgentWork",
    'filter_by_country_and_entity' : False,
    'field_list' : ['Id',
 'OwnerId',
 'IsDeleted',
 'Name',
 'CurrencyIsoCode',
 'CreatedDate',
 'CreatedById',
 'LastModifiedDate',
 'LastModifiedById',
 'SystemModstamp',
 'UserId',
 'WorkItemId',
 'Status',
 'ServiceChannelId',
 'OriginalQueueId',
 'CapacityWeight',
 'CapacityPercentage',
 'RequestDateTime',
 'AcceptDateTime',
 'DeclineDateTime',
 'CloseDateTime',
 'SpeedToAnswer',
 'AgentCapacityWhenDeclined',
 'PendingServiceRoutingId',
 'PushTimeout',
 'PushTimeoutDateTime',
 'HandleTime',
 'ActiveTime',
 'DeclineReason',
 'CancelDateTime',
 'ShouldSkipCapacityCheck',
 'RoutingType',
 'RoutingModel',
 'RoutingPriority',
 'AssignedDateTime',
 'PreferredUserId',
 'OriginalGroupId',
 'IsPreferredUserRequired',
 'AHT__c' ]
}



print(ConfigObject())
ConfigFormatter(config_object)