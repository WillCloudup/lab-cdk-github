from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    RemovalPolicy,
    Duration,
)
from constructs import Construct

class LabCdkGithubStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear un bucket S3 con un nombre personalizado
        bucket = s3.Bucket(
            self,
            "MyBucket",
            bucket_name="mi-bucket-lab-cdk-github",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.days(30),
                    noncurrent_version_expiration=Duration.days(30)
                )
            ]
        )

        # Crear una función Lambda simple
        function = _lambda.Function(
            self,
            "MyLambdaFunction",
            function_name="lambda-lab-cdk-github",
            description="Lambda function for lab-cdk-github",
            memory_size=128,
            timeout=Duration.seconds(10),
            environment={  # Mantener solo una definición de environment
                "BUCKET_NAME": bucket.bucket_name
            },
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=_lambda.Code.from_inline(
                "def handler(event, context):\n"
                "    return {'statusCode': 200, 'body': 'Hola desde Lambda'}"
            )
        )

        # Otorgar permisos de lectura/escritura desde Lambda al Bucket
        bucket.grant_read_write(function)