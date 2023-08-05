# Audit

## CloudSQL

1. who delete the cloudsql instance

    ```logging
    resource.type="cloudsql_database"
    resource.labels.database_id="<your-database-id>"
    protoPayload.methodName="cloudsql.instances.delete"
    ```

## IAM

1. who create the SA key

    ```logging
    resource.type="servcie_account"
    protoPayload.methodName:"google.iam.admin.v1.CreateServiceAccountKey"
    "your-service-account-email"
    ```

