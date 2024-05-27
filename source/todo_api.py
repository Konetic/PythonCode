# https://www.youtube.com/watch?v=7dgQRVqF1N0  https://todo.pixegami.io/docs          api
import requests

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    print(" perfect ")
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200  # python test

    data = create_task_response.json()
    print(data)

    # testing the code to make sure data sent to the server
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    # checking the data
    assert get_task_data["content"] == payload["content"]  # to make pass
    # assert get_task_data["content"] == "wrong data" # to make failt the test
    assert get_task_data["user_id"] == payload["user_id"]

    def test_can_update_task():
        # create a task
        payload = new_task_payload()
        create_task_response.json()["task"]["task_id"]
        # update a task
        # get and validate the changes
        pass


# helper functions


def create_task(payload):
    return requests.put(ENDPOINT + "/create_task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def new_task_payload():
    return {
        "content": "my test",
        "user_id": "test_user",
        "is_done": False,
    }


# or

# def new_task_payload():
# payload ={
#         "content": "my test",
#         "user_id": "test_user",
#         "is_done": False,
#     }
# return payload
