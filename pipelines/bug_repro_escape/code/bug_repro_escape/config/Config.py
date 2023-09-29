from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, raw_schema: str=None, **kwargs):
        self.spark = None
        self.update(raw_schema)

    def update(self, raw_schema: str="test_escape_raw_schema_value", **kwargs):
        prophecy_spark = self.spark
        self.raw_schema = raw_schema
        pass
