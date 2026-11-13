import os
from pathlib import Path

from yaml import load, SafeLoader

slurm_array_job_template = """
#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --account={slurm_account}
#SBATCH --array={array_range}
#SBATCH --output={output_directory}/logs/%A_%a.out
{slurm_extra}

source {env_source}

python -m harmony.launch --output_directory {output_directory} --steps {steps} --task $SLURM_ARRAY_TASK_ID
"""


def slurm_array_job_builder(config):
    output_directory = Path.cwd()

    steps = config["steps"].keys()

    slurm_account = config["job_builder"]["slurm_account"]

    with open(output_directory / "harmony_tasks.yaml", "r") as f:
        tasks = load(f, Loader=SafeLoader).keys()

    for pipeline in steps:
        ntasks = sum(1 for t in tasks if t.startswith(pipeline + "_task"))
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
            "slurm_extra": "".join(
                f"#SBATCH --{key}={value}\n" for key, value in resources.items()
            ),
        }

        (output_directory / "jobs").mkdir(exist_ok=True)
        with open(output_directory / "jobs" / f"{pipeline}.slurm", "w") as f:
            f.write(slurm_array_job_template.format(**sub_template))

    with open(output_directory / "harmony_run.sh", "w") as f:
        f.write("#!/bin/bash\n")
        for pipeline in steps:
            f.write(f"sbatch {output_directory / 'jobs' / f'{pipeline}.slurm'}\n")
    os.chmod(output_directory / "harmony_run.sh", 0o755)
