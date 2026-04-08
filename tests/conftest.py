from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(activities)

    yield

    # Preserve object identity while resetting mutable global state.
    activities.clear()
    activities.update(deepcopy(original_activities))
