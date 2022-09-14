#!/usr/bin/python3

import wordninja

class SqlFormatter:
    def __init__(self, sql_object):
        self.sql_object = sql_object
        self.no_dunder_strings = self.field_with_no_dunder(self.sql_object)
        self.clean_object = self.object_cleanup(self.sql_object)
        self.clean_object = self.fields_cleanup(self.sql_object)
        self.object_name_underscore = self.object_name_with_underscore(
            sql_object
            )

        return self.curated_data_sql_formatter(
            self.clean_object, 
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
        object['fields_v2'] = object['fields']
        self.lowercase_fields = list(map(str.lower, object['fields_v2']))
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
        object_name_with_undscore
        ):
        print(f"""CREATE OR REPLACE TABLE
  `{{{{ params.project_id }}}}.cl_salesforce.{object['object'].lower()}`
AS
SELECT """)
        for field in range(len(object['fields'])):
            print(
f"""  {object['object_abreviation']}.{object['fields'][field]} AS {object['fields_v2'][field].lower()},""")
        print(f"""FROM
  `{{{{ params.project_id }}}}.dl_salesforce.salesforce_{object_name_with_undscore}` AS {object['object_abreviation']}""")


class ConfigFormatter:
    def __init__(self, yaml_object):
        self.clean_object = yaml_object
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

