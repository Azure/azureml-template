# imports
import git

from pathlib import Path
from azureml.core import Workspace
from azureml.core import ScriptRunConfig, Experiment, Environment, Dataset

# get workspace
ws = Workspace.from_config()

# get root of git repo
prefix = Path(git.Repo(".", search_parent_directories=True).working_tree_dir)

# training script
script_dir = prefix.joinpath("code", "train", "lightgbm", "iris")
script_name = "train-advanced.py"

# environment file
environment_file = prefix.joinpath("environments", "lightgbm.txt")

# dataset
ds = Dataset.File.from_files(
    "https://azuremlexamples.blob.core.windows.net/datasets/iris.csv"
)

# azure ml settings
environment_name = "lightgbm"
experiment_name = "lightgbm-template-workflow"
compute_target = "cpu-cluster"

# create environment
env = Environment.from_pip_requirements(environment_name, environment_file)

# setup arguments
args = ["--data-dir", ds.as_mount()]

# create job config
src = ScriptRunConfig(
    source_directory=script_dir,
    script=script_name,
    arguments=args,
    environment=env,
    compute_target=compute_target,
)

# submit job
run = Experiment(ws, experiment_name).submit(src)
run.wait_for_completion(show_output=True)
