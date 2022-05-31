
from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)

class HitCounter(Construct):

    def handler(self):
        return self._handler

    def table(self):
        return self._table

    def __init__(self, scope: Construct, id:str, downstream:_lambda.IFunction, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self._table = dynamodb.Table(
            self, 'Hits', 
            partition_key={'name' : 'path', 'type' : dynamodb.AttributeType.STRING}
        )

        self._handler = _lambda.Function(
            self, 'HitCounterHandler', 
            runtime= _lambda.Runtime.PYTHON_3_7,
            handler='hitcount.handler',
            code=_lambda.Code.from_asset('lambda'),
            environment={
                'DOWNSTREAM_FUNCTION_NAME' : downstream.function_name,
                'HITS_TABLE_NAME' : self._table.table_name
            }
        )

        self._table.grant_read_write_data(self.handler())
        downstream.grant_invoke(self.handler())



