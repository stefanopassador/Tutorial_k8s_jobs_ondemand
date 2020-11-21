import yaml
import time
from kubernetes import client, config, watch

JOB_NAME = "simple-job"

def create_job_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="busybox",
        image="busybox",
        args=["sleep", "10"])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"name": "simple-job"}),
        spec=client.V1PodSpec(restart_policy="OnFailure", containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(
        parallelism=4,
        template=template,
        backoff_limit=4)
    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec)

    return job


def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace="default")
    print("Job created. status='%s'" % str(api_response.status))

def delete_job(api_instance):
    api_response = api_instance.delete_namespaced_job(
        name=JOB_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=0))
    print("Job deleted. status='%s'" % str(api_response.status))


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    #config.load_kube_config('C:\Users\spassador\.kube\config')
    config.load_incluster_config()
    batch_v1 = client.BatchV1Api()
    core_v1 = client.CoreV1Api()

    # Create a job object with client-python API. The job we
    # created is same as the `pi-job.yaml` in the /examples folder.
    job = create_job_object()

    create_job(batch_v1, job)
    time.sleep(30)
    delete_job(batch_v1)


if __name__ == '__main__':
    for i in range(1, 3):
        main()
        time.sleep(5)