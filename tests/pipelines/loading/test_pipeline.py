"""
This is a boilerplate test file for pipeline 'loading'
generated using Kedro 0.19.10.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from kedro.runner import SequentialRunner
from src.purchase_predict.pipelines.loading.pipeline import create_pipeline
import pandas as pd


def test_pipeline(catalog_test):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    pipeline_output = runner.run(pipeline, catalog_test)
    df = pipeline_output["primary"]
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 16
    assert "purchased" in df
