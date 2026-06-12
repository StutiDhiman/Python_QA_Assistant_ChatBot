# from fastapi.testclient import TestClient

# from app.main import app

# client = TestClient(app)


# def test_health():
#     response = client.get("/health")

#     assert response.status_code == 200


# def test_ask():
#     response = client.post(
#         "/ask",
#         json={
#             "question": "How do I reverse a list in Python?"
#         }
#     )

#     assert response.status_code == 200



import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200


def test_ask():
    response = client.post(
        "/ask",
        json={
            "question":
            "How do I reverse a list in Python?"
        }
    )

    assert response.status_code == 200