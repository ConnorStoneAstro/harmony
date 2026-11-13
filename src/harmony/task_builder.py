from pathlib import Path
from itertools import product
from math import ceil, log10

from yaml import dump


def parse_steps(step_config):
    if isinstance(step_config["name"], str):
        return [step_config]
    res = []
    for i in range(len(step_config["name"])):
        sub_res = {}
        for key, value in step_config.items():
            if isinstance(value, list):
                sub_res[key] = value[i]
            else:
                sub_res[key] = value
        res.append(sub_res)
    return res


def task_builder(config):
    if config["task_builder"]["data"]["paths_list"] is not None:
        data_paths = config["task_builder"]["data"]["paths_list"]
    elif config["task_builder"]["data"]["paths_file"] is not None:
        with open(config["task_builder"]["data"]["paths_file"], "r") as f:
            data_paths = [line.strip() for line in f.readlines()]
    elif config["task_builder"]["data"]["paths_dir"] is not None:
        data_paths = [str(p) for p in Path(config["task_builder"]["data"]["paths_dir"]).glob("*")]
    else:
        raise ValueError("No data paths specified")

    output_directory = Path.cwd()

    steps = config["steps"]

    width = ceil(log10(len(data_paths) * len(steps)))
    tasks = {}
    task_counters = {pipeline_name: 0 for pipeline_name in steps}
    for data_path, pipeline in product(data_paths, steps):
        taskname = f"{pipeline}_task_{task_counters[pipeline]:0{width}d}"
        task_counters[pipeline] += 1
        tasks[taskname] = {
            "data_path": data_path,
            "save_path": str(output_directory / taskname),
        }

    with open(output_directory / "harmony_tasks.yaml", "w") as file:
        dump(tasks, file, default_flow_style=False, sort_keys=False)
