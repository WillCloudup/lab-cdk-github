import aws_cdk as core
import aws_cdk.assertions as assertions

from lab_cdk_github.lab_cdk_github_stack import LabCdkGithubStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lab_cdk_github/lab_cdk_github_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LabCdkGithubStack(app, "lab-cdk-github")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
