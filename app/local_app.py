import yaml
import time
from kubernetes import client, config, watch

JOB_NAME = 'simple-job'
kubernetes_config_file_path = 'C:\\Users\\username\\.kube\\config'

def create_job_object():
    # Configureate Pod template container
    container = client.V1Container(
        name='busybox',
        image='busybox',
        args=['sleep', '6'])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={'name': 'simple-job'}),
        spec=client.V1PodSpec(restart_policy='OnFailure', containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(template=template)
    # Instantiate the job object
    job = client.V1Job(
        api_version='batch/v1',
        kind='Job',
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec)

    return job


def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace='default')
    print("Job created. status='%s'" % str(api_response.status))

def delete_job(api_instance):
    api_response = api_instance.delete_namespaced_job(
        name=JOB_NAME,
        namespace='default',
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=0))
    print("Job deleted. status='%s'" % str(api_response.status))


def main():
    config.load_kube_config(kubernetes_config_file_path)
    batch_v1 = client.BatchV1Api()

    job = create_job_object()

    create_job(batch_v1, job)
    time.sleep(30)
    delete_job(batch_v1)


if __name__ == '__main__':
    main()