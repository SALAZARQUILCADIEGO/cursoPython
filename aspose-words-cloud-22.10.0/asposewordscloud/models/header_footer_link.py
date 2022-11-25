# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="header_footer_link.py">
#   Copyright (c) 2022 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import datetime
import six
import json

class HeaderFooterLink(object):
    """HeaderFooter link element.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'type': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'type': 'Type'
    }

    def __init__(self, link=None, type=None):  # noqa: E501
        """HeaderFooterLink - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._type = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if type is not None:
            self.type = type

    @property
    def link(self):
        """Gets the link of this HeaderFooterLink.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this HeaderFooterLink.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this HeaderFooterLink.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this HeaderFooterLink.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def type(self):
        """Gets the type of this HeaderFooterLink.  # noqa: E501

        Gets or sets the paragraph's text.  # noqa: E501

        :return: The type of this HeaderFooterLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HeaderFooterLink.

        Gets or sets the paragraph's text.  # noqa: E501

        :param type: The type of this HeaderFooterLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["HeaderEven", "HeaderPrimary", "FooterEven", "FooterPrimary", "HeaderFirst", "FooterFirst"]  # noqa: E501
        if not type.isdigit():
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values))
            self._type = type
        else:
            self._type = allowed_values[int(type) if six.PY3 else long(type)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HeaderFooterLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other