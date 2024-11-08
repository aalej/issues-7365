from firebase_functions import tasks_fn

@tasks_fn.on_task_dispatched()
def dummy_test(request: tasks_fn.CallableRequest) -> str:
    return "Hello World"