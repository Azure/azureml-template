# imports
from pathlib import Path
from azureml.core import Workspace, ScriptRunConfig, Experiment, Environment, Dataset

# constants
environment_name = "myenv-template"
experiment_name = "template-workflow-base"
compute_name = "cpu-cluster"
data_uri = "https://azuremlexamples.blob.core.windows.net/datasets/iris.csv"

# get workspace
ws = Workspace.from_config()

# setup path prefix
prefix = Path(__file__).parent

# training script
script_dir = str(prefix.joinpath("src"))
script_name = "train.py"

# environment file
environment_file = str(prefix.joinpath("requirements.txt"))

# dataset
ds = Dataset.File.from_files(data_uri)

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
