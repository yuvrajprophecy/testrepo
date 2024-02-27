from perftest_abhisheks_e2etests_yuvraj_snapshot_sql_test_snapshot_yuvraj.utils import *

def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile_snowflake":
        dbt_props_cmd = " --profile run_profile_snowflake"

    if "orders_model":
        dbt_props_cmd = dbt_props_cmd + " -m " + "+orders_model"

    return BashOperator(
        task_id = "DBT_0",
        bash_command = f'''{" && ".join(
          ["set -euxo pipefail && tmpDir=`mktemp -d` && git clone https://github.com/yuvrajprophecy/testrepo --branch test --single-branch $tmpDir && cd $tmpDir/Yuvraj_Snapshot_SQL",            "dbt seed" + dbt_props_cmd,  "dbt run" + dbt_props_cmd,  "dbt test" + dbt_props_cmd]
        )}''',
        env = envs,
        append_env = True,
    )
