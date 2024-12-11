#!/usr/bin/env python3

import aws_cdk as cdk

from stack.infra_stack import InfraStack


app = cdk.App()
InfraStack(app, "InfraStack")

app.synth()
