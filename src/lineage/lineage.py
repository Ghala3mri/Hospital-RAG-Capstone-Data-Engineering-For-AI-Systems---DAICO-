from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job
from datetime import datetime

# بدون Marquez → نخلي الـ URL فاضي
client = OpenLineageClient()

def emit_start_event(task_name):
    event = RunEvent(
        eventType=RunState.START,
        eventTime=datetime.utcnow().isoformat(),
        run=Run(runId=f"{task_name}-{datetime.utcnow().timestamp()}"),
        job=Job(namespace="hospital_pipeline", name=task_name),
    )
    client.emit(event)

def emit_complete_event(task_name):
    event = RunEvent(
        eventType=RunState.COMPLETE,
        eventTime=datetime.utcnow().isoformat(),
        run=Run(runId=f"{task_name}-{datetime.utcnow().timestamp()}"),
        job=Job(namespace="hospital_pipeline", name=task_name),
    )
    client.emit(event)

def emit_fail_event(task_name):
    event = RunEvent(
        eventType=RunState.FAIL,
        eventTime=datetime.utcnow().isoformat(),
        run=Run(runId=f"{task_name}-{datetime.utcnow().timestamp()}"),
        job=Job(namespace="hospital_pipeline", name=task_name),
    )
    client.emit(event)