import os

from yaml import load, SafeLoader

slurm_array_job_template = """
#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --account={slurm_account}
#SBATCH --time={slurm_time}
#SBATCH --array={array_range}
#SBATCH --output={output_directory}/logs/%A_%a.out
#SBATCH --qos={slurm_qos}
{slurm_extra}

source {env_source}

python -m harmony.launch --output_directory {output_directory} --steps {steps} --task $SLURM_ARRAY_TASK_ID
"""


def slurm_array_job_expand_resources(config):
    pass


def slurm_array_job_builder(config):
    output_directory = config["output_directory"]

    steps = config["steps"].keys()

    slurm_account = config["job_builder"]["slurm_account"]

    with open(f"{output_directory}/harmony_tasks.yaml", "r") as f:
        tasks = load(f, Loader=SafeLoader).keys()

    for pipeline in steps:
        ntasks = sum(1 for t in tasks if t.startswith(pipeline))
        if isinstance(config["job_builder"]["env_source"], dict):
            env_source = config["job_builder"]["env_source"][pipeline]
        else:
            env_source = config["job_builder"]["env_source"]

        if isinstance(config["job_builder"]["resources"], dict):
            resources = config["job_builder"]["resources"][pipeline]
        else:
            resources = config["job_builder"]["resources"]
        sub_template = {
            "steps": pipeline,
            "job_name": config["job_builder"]["job_name"][pipeline],
            "output_directory": output_directory,
            "slurm_account": slurm_account,
            "array_range": f"0-{ntasks-1}",
            "env_source": env_source,
            **slurm_array_job_expand_resources(resources),
        }

        with open(f"{output_directory}/jobs/{pipeline}.slurm", "w") as f:
            f.write(slurm_array_job_template.format(**sub_template))

    with open(f"{output_directory}/harmony_run.sh", "w") as f:
        f.write("#!/bin/bash\n")
        for pipeline in steps:
            f.write(f"sbatch {output_directory}/jobs/{pipeline}.slurm\n")
    os.chmod(f"{output_directory}/harmony_run.sh", 0o755)
