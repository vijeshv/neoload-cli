# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ZoneDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'controllers': 'list[SimpleResourceApiDefinition]',
        'loadgenerators': 'list[SimpleResourceApiDefinition]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'controllers': 'controllers',
        'loadgenerators': 'loadgenerators'
    }

    def __init__(self, id=None, name=None, type=None, controllers=None, loadgenerators=None, local_vars_configuration=None):  # noqa: E501
        """ZoneDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._controllers = None
        self._loadgenerators = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if controllers is not None:
            self.controllers = controllers
        if loadgenerators is not None:
            self.loadgenerators = loadgenerators

    @property
    def id(self):
        """Gets the id of this ZoneDefinition.  # noqa: E501

        Unique identifier of the zone  # noqa: E501

        :return: The id of this ZoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ZoneDefinition.

        Unique identifier of the zone  # noqa: E501

        :param id: The id of this ZoneDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ZoneDefinition.  # noqa: E501

        Name of the zone  # noqa: E501

        :return: The name of this ZoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ZoneDefinition.

        Name of the zone  # noqa: E501

        :param name: The name of this ZoneDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ZoneDefinition.  # noqa: E501

        Type of the zone  # noqa: E501

        :return: The type of this ZoneDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ZoneDefinition.

        Type of the zone  # noqa: E501

        :param type: The type of this ZoneDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def controllers(self):
        """Gets the controllers of this ZoneDefinition.  # noqa: E501


        :return: The controllers of this ZoneDefinition.  # noqa: E501
        :rtype: list[SimpleResourceApiDefinition]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this ZoneDefinition.


        :param controllers: The controllers of this ZoneDefinition.  # noqa: E501
        :type: list[SimpleResourceApiDefinition]
        """

        self._controllers = controllers

    @property
    def loadgenerators(self):
        """Gets the loadgenerators of this ZoneDefinition.  # noqa: E501


        :return: The loadgenerators of this ZoneDefinition.  # noqa: E501
        :rtype: list[SimpleResourceApiDefinition]
        """
        return self._loadgenerators

    @loadgenerators.setter
    def loadgenerators(self, loadgenerators):
        """Sets the loadgenerators of this ZoneDefinition.


        :param loadgenerators: The loadgenerators of this ZoneDefinition.  # noqa: E501
        :type: list[SimpleResourceApiDefinition]
        """

        self._loadgenerators = loadgenerators

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ZoneDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneDefinition):
            return True

        return self.to_dict() != other.to_dict()