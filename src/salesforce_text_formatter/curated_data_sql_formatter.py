#!/usr/bin/python3

# # This file will convert a string of multiple field names to format that can be entered into a curated data for SQL.
import re
import wordninja

class ConfigObject:
    def __init__(self):
        print(""" config_object = {
    'fields': ['List of fields : list'],
    'object': "Object name here : str",
    'object_abreviation': "object abreviation goes here (e.g. opp) : str" 
}""")

class SqlFormatter:
    def __init__(self, config_object):
        self.config_object = config_object
        self.no_dunder_strings = self.field_with_no_dunder(self.config_object)
        self.clean_object = self.object_cleanup(self.config_object)
        self.clean_object = self.fields_cleanup(self.config_object)
        self.object_name_underscore = self.object_name_with_underscore(
            config_object
            )

        return self.curated_data_sql_formatter(
            self.clean_object, 
            self.no_dunder_strings, 
            self.object_name_underscore
            )

    def object_cleanup(self, object):
        object['object'] = object['object'].lower()
        return object

    def fields_cleanup(self, object):
        object['fields'] = list(map(str.lower, object['fields']))
        object['fields'] = list(map(wordninja.split, object['fields']))
        object['fields'] = list(map('_'.join, object['fields']))
        return object

    def field_with_no_dunder(self, object):
        self.lowercase_fields = list(map(str.lower, object['fields']))
        self.no_dunder_strings = list(map(
            lambda x: x.replace(r"__","_"), self.lowercase_fields))
        return self.no_dunder_strings

    def object_name_with_underscore(self, object):
        self.object_name_underscore = wordninja.split(object['object'].lower())
        self.object_name_underscore = '_'.join(self.object_name_underscore)
        return(self.object_name_underscore)

    def curated_data_sql_formatter(
        self, 
        object, 
        field_no_dunder, 
        object_name_with_undscore
        ):
        print(f"""CREATE OR REPLACE TABLE
  `{{{{ params.project_id }}}}.cl_salesforce.{object['object'].lower()}`
AS
SELECT """)
        # print(object['fields'][3])
        for field in range(len(object['fields'])):
            print(
f"""  {object['object_abreviation']}.{object['fields'][field]} AS {field_no_dunder[field]},""")
        print(f"""FROM
  `{{{{ params.project_id }}}}.dl_salesforce.salesforce_{object_name_with_undscore}` AS {object['object_abreviation']}""")

config_object = {
    'fields': ['Id',
 'OwnerId',
 'IsDeleted',
 'Name',
 'CurrencyIsoCode',
 'CreatedDate',
 'CreatedById',
 'LastModifiedDate'
],
    'object': "AgentWork",
    'object_abreviation': "a",  
}

print(ConfigObject())
SqlFormatter(config_object)
