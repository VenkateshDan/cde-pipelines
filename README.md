# cde-pipeline

## Jenkins Pipeline Rule

Jenkins Multibranch Pipeline reads the `Jenkinsfile` from the repository root by default.

### Standard:
- `Jenkinsfile` → Must stay in repo root
- `deploy/` → Helper deployment scripts only
- `configs/` → Environment/service configs
- `dags/` → Airflow DAGs
- `spark_jobs/` → Spark jobs

### Important:
If Jenkinsfile is placed in another folder (example: `deploy/Jenkinsfile`), Jenkins will NOT use it unless Script Path is explicitly changed in Jenkins job configuration.

### Lesson Learned:
Default Jenkins behavior = Root `Jenkinsfile`
