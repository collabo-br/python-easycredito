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


class SignupRequest(object):
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
        'cpf': 'str',
        'name': 'str',
        'birthday': 'date',
        'email': 'str',
        'phone': 'str',
        'zip_code': 'str',
        'has_credit_card': 'bool',
        'has_restriction': 'bool',
        'has_own_house': 'bool',
        'has_vehicle': 'bool'
    }

    attribute_map = {
        'cpf': 'cpf',
        'name': 'name',
        'birthday': 'birthday',
        'email': 'email',
        'phone': 'phone',
        'zip_code': 'zipCode',
        'has_credit_card': 'hasCreditCard',
        'has_restriction': 'hasRestriction',
        'has_own_house': 'hasOwnHouse',
        'has_vehicle': 'hasVehicle'
    }

    def __init__(self, cpf=None, name=None, birthday=None, email=None, phone=None, zip_code=None, has_credit_card=None, has_restriction=None, has_own_house=None, has_vehicle=None):  # noqa: E501
        """SignupRequest - a model defined in Swagger"""  # noqa: E501
        self._cpf = None
        self._name = None
        self._birthday = None
        self._email = None
        self._phone = None
        self._zip_code = None
        self._has_credit_card = None
        self._has_restriction = None
        self._has_own_house = None
        self._has_vehicle = None
        self.discriminator = None
        self.cpf = cpf
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.zip_code = zip_code
        if has_credit_card is not None:
            self.has_credit_card = has_credit_card
        if has_restriction is not None:
            self.has_restriction = has_restriction
        if has_own_house is not None:
            self.has_own_house = has_own_house
        if has_vehicle is not None:
            self.has_vehicle = has_vehicle

    @property
    def cpf(self):
        """Gets the cpf of this SignupRequest.  # noqa: E501

        > Document number, only numbers > > Número do documento, apenas números   # noqa: E501

        :return: The cpf of this SignupRequest.  # noqa: E501
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """Sets the cpf of this SignupRequest.

        > Document number, only numbers > > Número do documento, apenas números   # noqa: E501

        :param cpf: The cpf of this SignupRequest.  # noqa: E501
        :type: str
        """
        if cpf is None:
            raise ValueError("Invalid value for `cpf`, must not be `None`")  # noqa: E501

        self._cpf = cpf

    @property
    def name(self):
        """Gets the name of this SignupRequest.  # noqa: E501

        > Name of user > > Nome do usuário   # noqa: E501

        :return: The name of this SignupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignupRequest.

        > Name of user > > Nome do usuário   # noqa: E501

        :param name: The name of this SignupRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def birthday(self):
        """Gets the birthday of this SignupRequest.  # noqa: E501

        > Birhday, format (yyyy-mm-dd) > > Data de nascimento, formato (aaaa-mm-dd)   # noqa: E501

        :return: The birthday of this SignupRequest.  # noqa: E501
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this SignupRequest.

        > Birhday, format (yyyy-mm-dd) > > Data de nascimento, formato (aaaa-mm-dd)   # noqa: E501

        :param birthday: The birthday of this SignupRequest.  # noqa: E501
        :type: date
        """
        if birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")  # noqa: E501

        self._birthday = birthday

    @property
    def email(self):
        """Gets the email of this SignupRequest.  # noqa: E501

        > Valid email > > Email válido   # noqa: E501

        :return: The email of this SignupRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SignupRequest.

        > Valid email > > Email válido   # noqa: E501

        :param email: The email of this SignupRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this SignupRequest.  # noqa: E501

        > Valid phone with DDD, only numbers > > Telefone válido com DDD, apenas numeros   # noqa: E501

        :return: The phone of this SignupRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SignupRequest.

        > Valid phone with DDD, only numbers > > Telefone válido com DDD, apenas numeros   # noqa: E501

        :param phone: The phone of this SignupRequest.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def zip_code(self):
        """Gets the zip_code of this SignupRequest.  # noqa: E501

        > Valid zip code, only numbers > > CEP válido do usuário, apenas números   # noqa: E501

        :return: The zip_code of this SignupRequest.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this SignupRequest.

        > Valid zip code, only numbers > > CEP válido do usuário, apenas números   # noqa: E501

        :param zip_code: The zip_code of this SignupRequest.  # noqa: E501
        :type: str
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def has_credit_card(self):
        """Gets the has_credit_card of this SignupRequest.  # noqa: E501

        > Has credit card > > O usuário informou possuir cartão de crédito em seu nome   # noqa: E501

        :return: The has_credit_card of this SignupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_credit_card

    @has_credit_card.setter
    def has_credit_card(self, has_credit_card):
        """Sets the has_credit_card of this SignupRequest.

        > Has credit card > > O usuário informou possuir cartão de crédito em seu nome   # noqa: E501

        :param has_credit_card: The has_credit_card of this SignupRequest.  # noqa: E501
        :type: bool
        """

        self._has_credit_card = has_credit_card

    @property
    def has_restriction(self):
        """Gets the has_restriction of this SignupRequest.  # noqa: E501

        > Has overdue debts > > O usuário informou possuir restrições em seu nome   # noqa: E501

        :return: The has_restriction of this SignupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_restriction

    @has_restriction.setter
    def has_restriction(self, has_restriction):
        """Sets the has_restriction of this SignupRequest.

        > Has overdue debts > > O usuário informou possuir restrições em seu nome   # noqa: E501

        :param has_restriction: The has_restriction of this SignupRequest.  # noqa: E501
        :type: bool
        """

        self._has_restriction = has_restriction

    @property
    def has_own_house(self):
        """Gets the has_own_house of this SignupRequest.  # noqa: E501

        > Has own house > > O usuário informou possuir casa própria em seu nome   # noqa: E501

        :return: The has_own_house of this SignupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_own_house

    @has_own_house.setter
    def has_own_house(self, has_own_house):
        """Sets the has_own_house of this SignupRequest.

        > Has own house > > O usuário informou possuir casa própria em seu nome   # noqa: E501

        :param has_own_house: The has_own_house of this SignupRequest.  # noqa: E501
        :type: bool
        """

        self._has_own_house = has_own_house

    @property
    def has_vehicle(self):
        """Gets the has_vehicle of this SignupRequest.  # noqa: E501

        > Has vehicle > > O usuário informou possuir veículo em seu nome   # noqa: E501

        :return: The has_vehicle of this SignupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_vehicle

    @has_vehicle.setter
    def has_vehicle(self, has_vehicle):
        """Sets the has_vehicle of this SignupRequest.

        > Has vehicle > > O usuário informou possuir veículo em seu nome   # noqa: E501

        :param has_vehicle: The has_vehicle of this SignupRequest.  # noqa: E501
        :type: bool
        """

        self._has_vehicle = has_vehicle

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
        if issubclass(SignupRequest, dict):
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
        if not isinstance(other, SignupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
