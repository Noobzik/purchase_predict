"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, node
from .nodes import auto_ml


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=auto_ml,
                inputs=[
                    "X_train",
                    "y_train",
                    "X_test",
                    "y_test",
                    "params:automl_max_evals",
                    "params:mlflow_enabled",
                    "params:mlflow_experiment_id",
                ],
                outputs=dict(model="model", mlflow_run_id="mlflow_run_id"),
                name="auto_ml",
            )
        ]
    )
