# coding: utf-8

"""
    Easyc External

    API para processo externo  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tecnologia@easycredito.me
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Address(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'zip_code': 'str',
        'address': 'str',
        'address_number': 'str',
        'complement': 'str',
        'district': 'str',
        'state': 'State',
        'city': 'City'
    }

    attribute_map = {
        'zip_code': 'zipCode',
        'address': 'address',
        'address_number': 'addressNumber',
        'complement': 'complement',
        'district': 'district',
        'state': 'state',
        'city': 'city'
    }

    def __init__(self, zip_code=None, address=None, address_number=None, complement=None, district=None, state=None, city=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._zip_code = None
        self._address = None
        self._address_number = None
        self._complement = None
        self._district = None
        self._state = None
        self._city = None
        self.discriminator = None
        self.zip_code = zip_code
        self.address = address
        self.address_number = address_number
        if complement is not None:
            self.complement = complement
        self.district = district
        self.state = state
        self.city = city

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.  # noqa: E501

        Código CEP  # noqa: E501

        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.

        Código CEP  # noqa: E501

        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def address(self):
        """Gets the address of this Address.  # noqa: E501

        Endereço  # noqa: E501

        :return: The address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Address.

        Endereço  # noqa: E501

        :param address: The address of this Address.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address_number(self):
        """Gets the address_number of this Address.  # noqa: E501

        Número  # noqa: E501

        :return: The address_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_number

    @address_number.setter
    def address_number(self, address_number):
        """Sets the address_number of this Address.

        Número  # noqa: E501

        :param address_number: The address_number of this Address.  # noqa: E501
        :type: str
        """
        if address_number is None:
            raise ValueError("Invalid value for `address_number`, must not be `None`")  # noqa: E501

        self._address_number = address_number

    @property
    def complement(self):
        """Gets the complement of this Address.  # noqa: E501

        Complemento  # noqa: E501

        :return: The complement of this Address.  # noqa: E501
        :rtype: str
        """
        return self._complement

    @complement.setter
    def complement(self, complement):
        """Sets the complement of this Address.

        Complemento  # noqa: E501

        :param complement: The complement of this Address.  # noqa: E501
        :type: str
        """

        self._complement = complement

    @property
    def district(self):
        """Gets the district of this Address.  # noqa: E501

        Bairro  # noqa: E501

        :return: The district of this Address.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this Address.

        Bairro  # noqa: E501

        :param district: The district of this Address.  # noqa: E501
        :type: str
        """
        if district is None:
            raise ValueError("Invalid value for `district`, must not be `None`")  # noqa: E501

        self._district = district

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501


        :return: The state of this Address.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.


        :param state: The state of this Address.  # noqa: E501
        :type: State
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501


        :return: The city of this Address.  # noqa: E501
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  # noqa: E501
        :type: City
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Address, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
