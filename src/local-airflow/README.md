# Local airflow (docker-compose) setup






## Setup reference

First time setup
```bash
# downloading docker-compose yaml for Airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.2/docker-compose.yaml'

# initializing folder structure and noting UID:GID for airflow to run
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# initializing authentication `airflow:airflow`
docker-compose up airflow-init

# installing airflow docker script to use cli
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.2/airflow.sh'
chmod +x airflow.sh
```

Running airflow (compose)
```bash
docker-compose up -d
```
