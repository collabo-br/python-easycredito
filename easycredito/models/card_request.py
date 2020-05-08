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


class CardRequest(object):
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
        'network': 'Network',
        'international': 'bool',
        'prepaid': 'bool',
        'digital_account': 'bool',
        'pay_day': 'float'
    }

    attribute_map = {
        'network': 'network',
        'international': 'international',
        'prepaid': 'prepaid',
        'digital_account': 'digitalAccount',
        'pay_day': 'payDay'
    }

    def __init__(self, network=None, international=None, prepaid=None, digital_account=None, pay_day=None):  # noqa: E501
        """CardRequest - a model defined in Swagger"""  # noqa: E501
        self._network = None
        self._international = None
        self._prepaid = None
        self._digital_account = None
        self._pay_day = None
        self.discriminator = None
        if network is not None:
            self.network = network
        if international is not None:
            self.international = international
        if prepaid is not None:
            self.prepaid = prepaid
        if digital_account is not None:
            self.digital_account = digital_account
        if pay_day is not None:
            self.pay_day = pay_day

    @property
    def network(self):
        """Gets the network of this CardRequest.  # noqa: E501


        :return: The network of this CardRequest.  # noqa: E501
        :rtype: Network
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this CardRequest.


        :param network: The network of this CardRequest.  # noqa: E501
        :type: Network
        """

        self._network = network

    @property
    def international(self):
        """Gets the international of this CardRequest.  # noqa: E501

        Internacional  # noqa: E501

        :return: The international of this CardRequest.  # noqa: E501
        :rtype: bool
        """
        return self._international

    @international.setter
    def international(self, international):
        """Sets the international of this CardRequest.

        Internacional  # noqa: E501

        :param international: The international of this CardRequest.  # noqa: E501
        :type: bool
        """

        self._international = international

    @property
    def prepaid(self):
        """Gets the prepaid of this CardRequest.  # noqa: E501

        Cartão pré pago  # noqa: E501

        :return: The prepaid of this CardRequest.  # noqa: E501
        :rtype: bool
        """
        return self._prepaid

    @prepaid.setter
    def prepaid(self, prepaid):
        """Sets the prepaid of this CardRequest.

        Cartão pré pago  # noqa: E501

        :param prepaid: The prepaid of this CardRequest.  # noqa: E501
        :type: bool
        """

        self._prepaid = prepaid

    @property
    def digital_account(self):
        """Gets the digital_account of this CardRequest.  # noqa: E501

        Conta Digital  # noqa: E501

        :return: The digital_account of this CardRequest.  # noqa: E501
        :rtype: bool
        """
        return self._digital_account

    @digital_account.setter
    def digital_account(self, digital_account):
        """Sets the digital_account of this CardRequest.

        Conta Digital  # noqa: E501

        :param digital_account: The digital_account of this CardRequest.  # noqa: E501
        :type: bool
        """

        self._digital_account = digital_account

    @property
    def pay_day(self):
        """Gets the pay_day of this CardRequest.  # noqa: E501

        Dia da Fatura  # noqa: E501

        :return: The pay_day of this CardRequest.  # noqa: E501
        :rtype: float
        """
        return self._pay_day

    @pay_day.setter
    def pay_day(self, pay_day):
        """Sets the pay_day of this CardRequest.

        Dia da Fatura  # noqa: E501

        :param pay_day: The pay_day of this CardRequest.  # noqa: E501
        :type: float
        """

        self._pay_day = pay_day

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
        if issubclass(CardRequest, dict):
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
        if not isinstance(other, CardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
