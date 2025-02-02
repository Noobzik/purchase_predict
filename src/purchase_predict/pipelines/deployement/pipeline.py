"""
This is a boilerplate pipeline 'deployement'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, node

from .nodes import push_to_model_registry, stage_model


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=push_to_model_registry,
                inputs=["params:mlflow_model_registry", "mlflow_run_id"],
                outputs="mlflow_model_version",
                name="push_to_model_registry",
            ),
            node(
                func=stage_model,
                inputs=["params:mlflow_model_registry", "mlflow_model_version"],
                outputs=None,
                name="stage_model",
            ),
        ]
    )
