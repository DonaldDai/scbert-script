import os
job_id = os.environ.get("SLURM_JOB_ID", "default_job_id")
job_name = os.environ.get("SLURM_JOB_NAME", "default_job_name")
rank = os.environ.get("LOCAL_RANK", "default_local_rank")

print(f'{job_name}-{job_id}, {rank}')
