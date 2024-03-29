"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from graalsystems.api_client import ApiClient, Endpoint as _Endpoint
from graalsystems.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from graalsystems.model.error import Error
from graalsystems.model.infrastructure import Infrastructure
from graalsystems.model.patch import Patch
from graalsystems.model.services import Services
from graalsystems.model.target_info import TargetInfo


class InfrastructureApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_infrastructure_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}',
                'operation_id': 'delete_infrastructure_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_capacity_by_infrastructure_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (TargetInfo,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}/capacity',
                'operation_id': 'find_capacity_by_infrastructure_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.capacity+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_infrastructure_by_infrastructure_id_endpoint = _Endpoint(
            settings={
                'response_type': (Infrastructure,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}',
                'operation_id': 'find_infrastructure_by_infrastructure_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.infrastructure+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_infrastructures_endpoint = _Endpoint(
            settings={
                'response_type': ([Infrastructure],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures',
                'operation_id': 'find_infrastructures',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                ],
                'required': [
                    'x_tenant',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                },
                'location_map': {
                    'x_tenant': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.infrastructure+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_public_ips_by_infrastructure_id_endpoint = _Endpoint(
            settings={
                'response_type': ([str],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}/public-ips',
                'operation_id': 'find_public_ips_by_infrastructure_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_services_by_infrastructure_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Services,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}/services',
                'operation_id': 'find_services_by_infrastructure_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.services+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_infrastructure_endpoint = _Endpoint(
            settings={
                'response_type': (Infrastructure,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/infrastructures/{infrastructureId}',
                'operation_id': 'update_infrastructure',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'infrastructure_id',
                    'patch',
                ],
                'required': [
                    'x_tenant',
                    'infrastructure_id',
                    'patch',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_tenant':
                        (str,),
                    'infrastructure_id':
                        (str,),
                    'patch':
                        ([Patch],),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'infrastructure_id': 'infrastructureId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'infrastructure_id': 'path',
                    'patch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.infrastructure+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [
                    'application/json-patch+json;charset=UTF-8'
                ]
            },
            api_client=api_client
        )

    def delete_infrastructure_by_id(
        self,
        x_tenant,
        infrastructure_id,
        **kwargs
    ):
        """Delete a infrastructure by an id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_infrastructure_by_id(x_tenant, infrastructure_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        return self.delete_infrastructure_by_id_endpoint.call_with_http_info(**kwargs)

    def find_capacity_by_infrastructure_by_id(
        self,
        x_tenant,
        infrastructure_id,
        **kwargs
    ):
        """Retrieve the capacity of an infrastructure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_capacity_by_infrastructure_by_id(x_tenant, infrastructure_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TargetInfo
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        return self.find_capacity_by_infrastructure_by_id_endpoint.call_with_http_info(**kwargs)

    def find_infrastructure_by_infrastructure_id(
        self,
        x_tenant,
        infrastructure_id,
        **kwargs
    ):
        """Find infrastructure by Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_infrastructure_by_infrastructure_id(x_tenant, infrastructure_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Infrastructure
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        return self.find_infrastructure_by_infrastructure_id_endpoint.call_with_http_info(**kwargs)

    def find_infrastructures(
        self,
        x_tenant,
        **kwargs
    ):
        """Retrieve all infrastructure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_infrastructures(x_tenant, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Infrastructure]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        return self.find_infrastructures_endpoint.call_with_http_info(**kwargs)

    def find_public_ips_by_infrastructure_id(
        self,
        x_tenant,
        infrastructure_id,
        **kwargs
    ):
        """Find public ips by infrastructure id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_public_ips_by_infrastructure_id(x_tenant, infrastructure_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [str]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        return self.find_public_ips_by_infrastructure_id_endpoint.call_with_http_info(**kwargs)

    def find_services_by_infrastructure_by_id(
        self,
        x_tenant,
        infrastructure_id,
        **kwargs
    ):
        """Retrieve the services of an infrastructure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_services_by_infrastructure_by_id(x_tenant, infrastructure_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Services
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        return self.find_services_by_infrastructure_by_id_endpoint.call_with_http_info(**kwargs)

    def update_infrastructure(
        self,
        x_tenant,
        infrastructure_id,
        patch,
        **kwargs
    ):
        """Update an infrastructure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_infrastructure(x_tenant, infrastructure_id, patch, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            infrastructure_id (str): Id of the infrastructure
            patch ([Patch]): The patch

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Infrastructure
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['infrastructure_id'] = \
            infrastructure_id
        kwargs['patch'] = \
            patch
        return self.update_infrastructure_endpoint.call_with_http_info(**kwargs)

