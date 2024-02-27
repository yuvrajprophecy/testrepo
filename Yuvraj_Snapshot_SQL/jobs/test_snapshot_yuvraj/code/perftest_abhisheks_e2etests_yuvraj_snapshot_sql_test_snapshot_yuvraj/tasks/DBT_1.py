from perftest_abhisheks_e2etests_yuvraj_snapshot_sql_test_snapshot_yuvraj.utils import *

def DBT_1():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile_snowflake":
        dbt_props_cmd = " --profile run_profile_snowflake"

    if "orders_snapshot":
        # if self.props.runSnapshotWithChildren:
        #     val = val + "+"
        # if self.props.runSnapshotWithParents:
        #     val = "+" + val
        dbt_props_cmd = dbt_props_cmd + " -s " + "orders_snapshot"

    return BashOperator(
        task_id = "DBT_1",
        bash_command = f'''{" && ".join(
          ["set -euxo pipefail && tmpDir=`mktemp -d` && git clone https://github.com/yuvrajprophecy/testrepo --branch test --single-branch $tmpDir && cd $tmpDir/Yuvraj_Snapshot_SQL",            "dbt snapshot" + dbt_props_cmd,  "dbt run" + dbt_props_cmd]
        )}''',
        env = envs,
        append_env = True,
    )
