#!/usr/bin/env python3

import aws_cdk as cdk
from lab_cdk_github.lab_cdk_github_stack import LabCdkGithubStack

app = cdk.App()

LabCdkGithubStack(app, "LabCdkGithubStack")

app.synth()
#test to user