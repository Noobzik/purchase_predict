import os
import mlflow

from mlflow.tracking import MlflowClient


def push_to_model_registry(registry_name: str, run_id: int):
    """
    Pushes a model's version to the specified registry.
    """
    mlflow.set_tracking_uri(os.getenv("MLFLOW_SERVER"))
    result = mlflow.register_model(
        "runs:/{}/artifacts/model".format(run_id), registry_name
    )
    return result.version


def stage_model(registry_name: str, version: int):
    """
    Stages a model version pushed to model registry.
    """
    env = os.getenv("ENV")
    if env not in ["staging", "production"]:
        return

    client = MlflowClient()
    client.transition_model_version_stage(
        name=registry_name, version=str(version), stage=env[0].upper() + env[1:]
    )
    # latest_mv = client.get_latest_versions(registry_name, stages=[env.capitalize()])[0]
    # client.set_registered_model_alias(name=registry_name, alias=env.upper(), version=latest_mv.version)
