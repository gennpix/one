# GCP Logging

## Audit log

### Compute

1. 查询 VM 创建记录

    ```logging
    resource.type="gce_instance"
    protoPayload.methodName='beta.compute.instances.insert" OR protoPayload.methodName='v1.compute.instances.insert"
    "your vm name"
    ```

1. 查询 VM 删除记录

    ```logging
    resource.type="gce_instance"
    protoPayload.methodName='v1.compute.instances.delete" 
    "your vm name"
    ```

1. 查询 VM 的所有activity 日志

    ```logging
    resource.type="gce_instance"
    logName="project/xxxxx/logs/cloudaudit.googleapis.com%2Factivity"
    "your vm name"
    ```

