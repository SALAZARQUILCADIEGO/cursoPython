# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="execute_mail_merge_request.py">
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
import json

from six.moves.urllib.parse import quote
from asposewordscloud import *
from asposewordscloud.models import *
from asposewordscloud.models.requests import *
from asposewordscloud.models.responses import *

class ExecuteMailMergeRequest(BaseRequestObject):
    """
    Request model for execute_mail_merge operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param data Mail merge data.
    :param options Field options.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password of protected Word document. Use the parameter to pass a password via SDK. SDK encrypts it automatically. We don't recommend to use the parameter to pass a plain password for direct call of API.
    :param encrypted_password Password of protected Word document. Use the parameter to pass an encrypted password for direct calls of API. See SDK code for encyption details.
    :param with_regions The flag indicating whether to execute Mail Merge operation with regions.
    :param mail_merge_data_file The data file.
    :param cleanup The cleanup options.
    :param use_whole_paragraph_as_region The flag indicating whether paragraph with TableStart or TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields. The default value is true.
    :param dest_file_name The filename of the output document. If this parameter is omitted, the result will be saved with autogenerated name.
    """

    def __init__(self, name, data=None, options=None, folder=None, storage=None, load_encoding=None, password=None, encrypted_password=None, with_regions=None, mail_merge_data_file=None, cleanup=None, use_whole_paragraph_as_region=None, dest_file_name=None):
        self.name = name
        self.data = data
        self.options = options
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.encrypted_password = encrypted_password
        self.with_regions = with_regions
        self.mail_merge_data_file = mail_merge_data_file
        self.cleanup = cleanup
        self.use_whole_paragraph_as_region = use_whole_paragraph_as_region
        self.dest_file_name = dest_file_name

    def create_http_request(self, api_client):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `execute_mail_merge`")  # noqa: E501

        path = '/v4.0/words/{name}/MailMerge'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501

        # path parameters
        collection_formats = {}
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                path = path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=api_client.configuration.safe_chars_for_path_param)
                )

        # remove optional path parameters
        path = path.replace('//', '/')

        query_params = []
        if self.folder is not None:
                query_params.append(('folder', self.folder))  # noqa: E501
        if self.storage is not None:
                query_params.append(('storage', self.storage))  # noqa: E501
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.encrypted_password is not None:
                query_params.append(('encryptedPassword', self.encrypted_password))  # noqa: E501
        if self.with_regions is not None:
                query_params.append(('withRegions', self.with_regions))  # noqa: E501
        if self.mail_merge_data_file is not None:
                query_params.append(('mailMergeDataFile', self.mail_merge_data_file))  # noqa: E501
        if self.cleanup is not None:
                query_params.append(('cleanup', self.cleanup))  # noqa: E501
        if self.use_whole_paragraph_as_region is not None:
                query_params.append(('useWholeParagraphAsRegion', self.use_whole_paragraph_as_region))  # noqa: E501
        if self.dest_file_name is not None:
                query_params.append(('destFileName', self.dest_file_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.data is not None:
            form_params.append(['data', self.data, 'string'])  # noqa: E501
        if self.options is not None:
            form_params.append(['options', self.options, 'json'])  # noqa: E501

        for file_content_value in file_content_params:
            form_params.append([file_content_value.reference, file_content_value.content, 'file'])  # noqa: E501

        return {
            "method": "PUT",
            "path": path,
            "body": None,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "collection_formats": collection_formats,
            "response_type": 'DocumentResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'DocumentResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), DocumentResponse)