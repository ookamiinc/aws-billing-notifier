from unittest.mock import MagicMock
from unittest import mock
import unittest
import sys
import os
import datetime
import dateutil
import handler
from dateutil.tz import tzlocal

sys.path.append(os.pardir)


class NotifierTest(unittest.TestCase):
    def test_message_payload(self):
        services_json = {
            "Metrics": [
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "awskms"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonRDS"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSLambda"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonSageMaker"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSConfig"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "awswaf"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSDataTransfer"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSSecretsManager"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonSES"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonSNS"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [{"Name": "Currency", "Value": "USD"}],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonS3"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonRoute53"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSCloudTrail"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonStates"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSMarketplace"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonCloudWatch"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonEC2"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AWSBudgets"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
                {
                    "Namespace": "AWS/Billing",
                    "MetricName": "EstimatedCharges",
                    "Dimensions": [
                        {"Name": "ServiceName", "Value": "AmazonCloudFront"},
                        {"Name": "Currency", "Value": "USD"},
                    ],
                },
            ],
            "ResponseMetadata": {
                "RequestId": "a21fa897-a829-11e9-9006-abab1ff1cace",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "a21fa897-a829-11e9-9006-abab1ff1cace",
                    "content-type": "text/xml",
                    "content-length": "7893",
                    "vary": "accept-encoding",
                    "date": "Wed, 17 Jul 2019 00:27:17 GMT",
                },
                "RetryAttempts": 0,
            },
        }
        handler.client.list_metrics = MagicMock(return_value=services_json)
        billing_json = {
            "Label": "EstimatedCharges",
            "Datapoints": [
                {
                    "Timestamp": datetime.datetime(
                        2019, 7, 16, 0, 27, tzinfo=tzlocal()
                    ),
                    "Average": 1557.99,
                    "Unit": "None",
                }
            ],
            "ResponseMetadata": {
                "RequestId": "aae332f4-a82a-11e9-843e-2319aa9bda51",
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "x-amzn-requestid": "aae332f4-a82a-11e9-843e-2319aa9bda51",
                    "content-type": "text/xml",
                    "content-length": "500",
                    "date": "Wed, 17 Jul 2019 00:34:42 GMT",
                },
                "RetryAttempts": 0,
            },
        }
        handler.client.get_metric_statistics = MagicMock(return_value=billing_json)
        output = {
            "attachments": [
                {
                    "fallback": "今月のAWSの利用費は、1,558.0 USDです。",
                    "pretext": "今月のAWSの利用費は、1,558.0 USDです。",
                    "color": "good",
                    "fields": [
                        {"title": "awskms", "value": "1,558.0 USD", "short": "true"},
                        {"title": "AmazonRDS", "value": "1,558.0 USD", "short": "true"},
                        {"title": "AWSLambda", "value": "1,558.0 USD", "short": "true"},
                        {
                            "title": "AmazonSageMaker",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {"title": "AWSConfig", "value": "1,558.0 USD", "short": "true"},
                        {"title": "awswaf", "value": "1,558.0 USD", "short": "true"},
                        {
                            "title": "AWSDataTransfer",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AWSSecretsManager",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {"title": "AmazonSES", "value": "1,558.0 USD", "short": "true"},
                        {"title": "AmazonSNS", "value": "1,558.0 USD", "short": "true"},
                        {"title": "AmazonS3", "value": "1,558.0 USD", "short": "true"},
                        {
                            "title": "AmazonRoute53",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AWSCloudTrail",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AmazonStates",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AWSMarketplace",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AmazonCloudWatch",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {"title": "AmazonEC2", "value": "1,558.0 USD", "short": "true"},
                        {
                            "title": "AWSBudgets",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                        {
                            "title": "AmazonCloudFront",
                            "value": "1,558.0 USD",
                            "short": "true",
                        },
                    ],
                }
            ]
        }
        self.assertEqual(handler.message_payload(), output)

    def test_send_slack(self):
        url = "sample url"
        channel = "sample channel"
        payload = {"key": "value"}
        handler.requests.post = MagicMock(return_value=200)
        handler.send_slack(url, channel, payload)
        handler.requests.post.assert_called_once_with(
            url, '{"key": "value", "channel": "sample channel"}'
        )
