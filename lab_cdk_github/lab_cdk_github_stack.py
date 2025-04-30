from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
)
from constructs import Construct

class LabCdkGithubStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear un bucket S3
        bucket = s3.Bucket(self, "MyBucket")

        # Crear una función Lambda simple
        function = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=_lambda.Code.from_inline(
                "def handler(event, context):\n"
                "    return {'statusCode': 200, 'body': 'Hola desde Lambda'}"
            ),
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }
        )

        # Otorgar permisos de lectura/escritura desde Lambda al Bucket
        bucket.grant_read_write(function)