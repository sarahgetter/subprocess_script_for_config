import subprocess
import json

project_id = "<insert-your-bigquery-project-name-here>"

# Get the list of datasets in the project
datasets_output = subprocess.check_output(["bq", "ls", "--format=json", project_id])
datasets = json.loads(datasets_output)

# Loop over the datasets and get the information for each one
for dataset in datasets:
    dataset_id = dataset["datasetReference"]["datasetId"]
    print(f"Dataset: {dataset_id}")

    # Get the schema of the dataset
    schema_output = subprocess.check_output(["bq", "show", "--schema", dataset_id])
    schema = schema_output.decode("utf-8")
    print(f"Schema: {schema}")

    # Get the ACL of the dataset
    acl_output = subprocess.check_output(["bq", "show", "--format=json", dataset_id])
    acl = json.loads(acl_output)["access"]
    print(f"ACL: {acl}")

    # Get the list of tables in the dataset
    tables_output = subprocess.check_output(["bq", "ls", "--format=json", dataset_id])
    tables = json.loads(tables_output)

    # Loop over the tables and get the information for each one
    for table in tables:
        table_id = f"{dataset_id}.{table['tableReference']['tableId']}"
        print(f"Table: {table_id}")

        # Get the schema of the table
        schema_output = subprocess.check_output(["bq", "show", "--schema", table_id])
        schema = schema_output.decode("utf-8")
        print(f"Schema: {schema}")

        # Get the list of partitions in the table (if it's partitioned)
        if "timePartitioning" in table:
            partitions_output = subprocess.check_output(["bq", "ls", "--apilog", f"{dataset_id}.{table['tableReference']['tableId']}"])
            partitions = partitions_output.decode("utf-8")
            print(f"Partitions: {partitions}")
