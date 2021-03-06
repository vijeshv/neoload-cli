import json
from json import JSONDecodeError

import jsonschema
import requests
import yaml
from yaml.scanner import ScannerError

from neoload_cli_lib.user_data import update_schema, get_yaml_schema


def validate_yaml(yaml_file_path, schema_url):
    try:
        yaml_content = open(yaml_file_path)
    except Exception as err:
        raise Exception('Unable to open file %s:\n%s' % (yaml_file_path, str(err)))

    try:
        yaml_as_object = yaml.load(yaml_content, yaml.FullLoader)
    except ScannerError as err:
        raise Exception('This is not a valid yaml file :\n%s' % str(err))

    if schema_url is None:
        try:
            json_schema = get_yaml_schema()
        except Exception as err:
            raise Exception('Error getting the schema from disk : %s' % str(err))
    else:
        try:
            json_schema = requests.get(schema_url).text
        except Exception as err:
            raise Exception('Error getting the schema from the url: %s\n%s' % (schema_url, str(err)))
        try:
            update_schema(json_schema)
        except Exception as err:
            raise Exception('Error storing the schema : %s' % str(err))

    try:
        schema_as_object = json.loads(json_schema)
    except JSONDecodeError as err:
        raise Exception('This is not a valid json schema file :\n%s' % str(err))

    try:
        jsonschema.validate(yaml_as_object, schema_as_object)
    except jsonschema.SchemaError as err:
        raise Exception('This is not a valid json schema file :\n%s' % str(err))
    except jsonschema.ValidationError as err:
        raise Exception('Wrong Yaml structure. Violation of the Neoload schema:\n%s\n\nOn instance:\n%s' % (
            err.message, str(err.instance)))
