# imports
from pathlib import Path
from azureml.core import Workspace, ScriptRunConfig, Experiment, Environment, Dataset

# constants
compute_name = "cpu-cluster"  # use "local" for local execution
entry_script = "train.py"
environment_name = "myenv-template"
experiment_name = "template-workflow-base"
data_uri = "https://azuremlexamples.blob.core.windows.net/datasets/iris.csv"

# get workspace
ws = Workspace.from_config()

# setup path prefix
prefix = Path(__file__).parent

# get relative paths
script_dir = str(prefix.joinpath("src"))
environment_file = str(prefix.joinpath("requirements.txt"))

# create dataset
ds = Dataset.File.from_files(data_uri)

# create environment
env = Environment.from_pip_requirements(environment_name, environment_file)

# setup entry script arguments
args = ["--data-dir", ds.as_mount()]

# create a job configuration
src = ScriptRunConfig(
    source_directory=script_dir,
    script=entry_script,
    arguments=args,
    environment=env,
    compute_target=compute_name,
)

# run the job
run = Experiment(ws, experiment_name).submit(src)
run.wait_for_completion(show_output=True)
