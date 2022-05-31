from inspect import stack
from pyclbr import Function
from typing_extensions import runtime
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    assertions 
)

from cdk_workshop.hitcounter import HitCounter
import pytest

# def test_dynamodb_table_created():
#     stack = Stack()
#     HitCounter(stack, 'HitCOunter'
#         downstream=_lambda.Function(stack, 'TestFunction', 
#         runtime=_lambda.Runtime.) 
#     )