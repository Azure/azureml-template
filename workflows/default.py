# imports
from pathlib import Path
from azureml.core import Workspace
from azureml.core import ScriptRunConfig, Experiment, Environment, Dataset

# get workspace
ws = Workspace.from_config()

# setup path prefix
prefix = Path("..")

# training script
script_dir = prefix.joinpath("code")
script_name = "train.py"

# environment file
environment_file = prefix.joinpath("environments", "env.txt")

# dataset
ds = Dataset.File.from_files(
    "https://azuremlexamples.blob.core.windows.net/datasets/iris.csv"
)

# azure ml settings
environment_name = "template-env"
experiment_name = "template-workflow"
compute_name = "cpu-cluster"

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
    compute_target=compute_name,
)

# submit job
run = Experiment(ws, experiment_name).submit(src)
run.wait_for_completion(show_output=True)
