import pytest
from kedro.io import DataCatalog, MemoryDataset


@pytest.fixture(scope="module")
def project_id():
    return "esgi-352608"


@pytest.fixture(scope="module")
def primary_folder():
    return "purchase_predict/primary.csv"


@pytest.fixture(scope="module")
def catalog_test(project_id, primary_folder):
    catalog = DataCatalog(
        {
            "params:gcp_project_id": MemoryDataset(project_id),
            "params:gcs_primary_folder": MemoryDataset(primary_folder),
        }
    )
    return catalog
