# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="markdown_save_options_data.py">
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

class MarkdownSaveOptionsData(object):
    """Container class for markdown save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_embedding_post_script_fonts': 'bool',
        'custom_time_zone_info_data': 'TimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'dml_rendering_mode': 'str',
        'file_name': 'str',
        'iml_rendering_mode': 'str',
        'update_created_time_property': 'bool',
        'update_fields': 'bool',
        'update_last_printed_property': 'bool',
        'update_last_saved_time_property': 'bool',
        'update_sdt_content': 'bool',
        'zip_output': 'bool',
        'encoding': 'str',
        'export_headers_footers_mode': 'str',
        'force_page_breaks': 'bool',
        'paragraph_break': 'str',
        'save_format': 'str',
        'table_content_alignment': 'str'
    }

    attribute_map = {
        'allow_embedding_post_script_fonts': 'AllowEmbeddingPostScriptFonts',
        'custom_time_zone_info_data': 'CustomTimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'Dml3DEffectsRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'dml_rendering_mode': 'DmlRenderingMode',
        'file_name': 'FileName',
        'iml_rendering_mode': 'ImlRenderingMode',
        'update_created_time_property': 'UpdateCreatedTimeProperty',
        'update_fields': 'UpdateFields',
        'update_last_printed_property': 'UpdateLastPrintedProperty',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'update_sdt_content': 'UpdateSdtContent',
        'zip_output': 'ZipOutput',
        'encoding': 'Encoding',
        'export_headers_footers_mode': 'ExportHeadersFootersMode',
        'force_page_breaks': 'ForcePageBreaks',
        'paragraph_break': 'ParagraphBreak',
        'save_format': 'SaveFormat',
        'table_content_alignment': 'TableContentAlignment'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, iml_rendering_mode=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, update_sdt_content=None, zip_output=None, encoding=None, export_headers_footers_mode=None, force_page_breaks=None, paragraph_break=None, table_content_alignment=None):  # noqa: E501
        """MarkdownSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._allow_embedding_post_script_fonts = None
        self._custom_time_zone_info_data = None
        self._dml3_d_effects_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._dml_rendering_mode = None
        self._file_name = None
        self._iml_rendering_mode = None
        self._update_created_time_property = None
        self._update_fields = None
        self._update_last_printed_property = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._zip_output = None
        self._encoding = None
        self._export_headers_footers_mode = None
        self._force_page_breaks = None
        self._paragraph_break = None
        self._save_format = "md"
        self._table_content_alignment = None
        self.discriminator = None

        if allow_embedding_post_script_fonts is not None:
            self.allow_embedding_post_script_fonts = allow_embedding_post_script_fonts
        if custom_time_zone_info_data is not None:
            self.custom_time_zone_info_data = custom_time_zone_info_data
        if dml3_d_effects_rendering_mode is not None:
            self.dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if file_name is not None:
            self.file_name = file_name
        if iml_rendering_mode is not None:
            self.iml_rendering_mode = iml_rendering_mode
        if update_created_time_property is not None:
            self.update_created_time_property = update_created_time_property
        if update_fields is not None:
            self.update_fields = update_fields
        if update_last_printed_property is not None:
            self.update_last_printed_property = update_last_printed_property
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if update_sdt_content is not None:
            self.update_sdt_content = update_sdt_content
        if zip_output is not None:
            self.zip_output = zip_output
        if encoding is not None:
            self.encoding = encoding
        if export_headers_footers_mode is not None:
            self.export_headers_footers_mode = export_headers_footers_mode
        if force_page_breaks is not None:
            self.force_page_breaks = force_page_breaks
        if paragraph_break is not None:
            self.paragraph_break = paragraph_break
        if table_content_alignment is not None:
            self.table_content_alignment = table_content_alignment

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this MarkdownSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this MarkdownSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this MarkdownSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this MarkdownSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Basic", "Advanced"]  # noqa: E501
        if not dml3_d_effects_rendering_mode.isdigit():
            if dml3_d_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml3_d_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml3_d_effects_rendering_mode, allowed_values))
            self._dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        else:
            self._dml3_d_effects_rendering_mode = allowed_values[int(dml3_d_effects_rendering_mode) if six.PY3 else long(dml3_d_effects_rendering_mode)]

    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :return: The dml_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this MarkdownSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Simplified", "None", "Fine"]  # noqa: E501
        if not dml_effects_rendering_mode.isdigit():
            if dml_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml_effects_rendering_mode, allowed_values))
            self._dml_effects_rendering_mode = dml_effects_rendering_mode
        else:
            self._dml_effects_rendering_mode = allowed_values[int(dml_effects_rendering_mode) if six.PY3 else long(dml_effects_rendering_mode)]

    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :return: The dml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this MarkdownSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Fallback", "DrawingML"]  # noqa: E501
        if not dml_rendering_mode.isdigit():
            if dml_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml_rendering_mode, allowed_values))
            self._dml_rendering_mode = dml_rendering_mode
        else:
            self._dml_rendering_mode = allowed_values[int(dml_rendering_mode) if six.PY3 else long(dml_rendering_mode)]

    @property
    def file_name(self):
        """Gets the file_name of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this MarkdownSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :return: The iml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this MarkdownSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Fallback", "InkML"]  # noqa: E501
        if not iml_rendering_mode.isdigit():
            if iml_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `iml_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(iml_rendering_mode, allowed_values))
            self._iml_rendering_mode = iml_rendering_mode
        else:
            self._iml_rendering_mode = allowed_values[int(iml_rendering_mode) if six.PY3 else long(iml_rendering_mode)]

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :return: The update_created_time_property of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this MarkdownSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content

    @property
    def zip_output(self):
        """Gets the zip_output of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :return: The zip_output of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :param zip_output: The zip_output of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def encoding(self):
        """Gets the encoding of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the character encoding to use when exporting in plain text format.  # noqa: E501

        :return: The encoding of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this MarkdownSaveOptionsData.

        Gets or sets the character encoding to use when exporting in plain text format.  # noqa: E501

        :param encoding: The encoding of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding

    @property
    def export_headers_footers_mode(self):
        """Gets the export_headers_footers_mode of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls whether to output headers and footers when exporting in plain text format. default value is TxtExportHeadersFootersMode.PrimaryOnly.  # noqa: E501

        :return: The export_headers_footers_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_headers_footers_mode

    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, export_headers_footers_mode):
        """Sets the export_headers_footers_mode of this MarkdownSaveOptionsData.

        Gets or sets the option that controls whether to output headers and footers when exporting in plain text format. default value is TxtExportHeadersFootersMode.PrimaryOnly.  # noqa: E501

        :param export_headers_footers_mode: The export_headers_footers_mode of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "PrimaryOnly", "AllAtEnd"]  # noqa: E501
        if not export_headers_footers_mode.isdigit():
            if export_headers_footers_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `export_headers_footers_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(export_headers_footers_mode, allowed_values))
            self._export_headers_footers_mode = export_headers_footers_mode
        else:
            self._export_headers_footers_mode = allowed_values[int(export_headers_footers_mode) if six.PY3 else long(export_headers_footers_mode)]

    @property
    def force_page_breaks(self):
        """Gets the force_page_breaks of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :return: The force_page_breaks of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._force_page_breaks

    @force_page_breaks.setter
    def force_page_breaks(self, force_page_breaks):
        """Sets the force_page_breaks of this MarkdownSaveOptionsData.

        Gets or sets a value indicating whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :param force_page_breaks: The force_page_breaks of this MarkdownSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._force_page_breaks = force_page_breaks

    @property
    def paragraph_break(self):
        """Gets the paragraph_break of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the string to use as a paragraph break when exporting in plain text format.  # noqa: E501

        :return: The paragraph_break of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._paragraph_break

    @paragraph_break.setter
    def paragraph_break(self, paragraph_break):
        """Sets the paragraph_break of this MarkdownSaveOptionsData.

        Gets or sets the string to use as a paragraph break when exporting in plain text format.  # noqa: E501

        :param paragraph_break: The paragraph_break of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._paragraph_break = paragraph_break

    @property
    def save_format(self):
        """Gets the save_format of this MarkdownSaveOptionsData.  # noqa: E501

        Gets the format of save.  # noqa: E501

        :return: The save_format of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format


    @property
    def table_content_alignment(self):
        """Gets the table_content_alignment of this MarkdownSaveOptionsData.  # noqa: E501

        Gets or sets the value, that specifies how to align contents in tables when exporting into the Markdown format. The default value is Auto.  # noqa: E501

        :return: The table_content_alignment of this MarkdownSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._table_content_alignment

    @table_content_alignment.setter
    def table_content_alignment(self, table_content_alignment):
        """Sets the table_content_alignment of this MarkdownSaveOptionsData.

        Gets or sets the value, that specifies how to align contents in tables when exporting into the Markdown format. The default value is Auto.  # noqa: E501

        :param table_content_alignment: The table_content_alignment of this MarkdownSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Auto", "Left", "Center", "Right"]  # noqa: E501
        if not table_content_alignment.isdigit():
            if table_content_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `table_content_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(table_content_alignment, allowed_values))
            self._table_content_alignment = table_content_alignment
        else:
            self._table_content_alignment = allowed_values[int(table_content_alignment) if six.PY3 else long(table_content_alignment)]


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
        if not isinstance(other, MarkdownSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other