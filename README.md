# Azure Machine Learning (AML) Template

[![run-workflows-badge](https://github.com/Azure/azureml-template/workflows/run-workflows/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Arun-workflows)
[![cleanup](https://github.com/Azure/azureml-template/workflows/cleanup/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Acleanup)
[![smoke](https://github.com/Azure/azureml-template/workflows/smoke/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Asmoke)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Welcome to the Azure Machine Learning (AML) template repository!

## Prerequisites

1. An Azure subscription. If you don't have an Azure subscription, [create a free account](https://aka.ms/AMLFree) before you begin.
2. A terminal and Python >=3.6,[\<3.9](https://pypi.org/project/azureml-core).

## Getting started

Click "Use this template" above and create a repository.

Follow the setup guide below to add your Azure credentials and create required Azure resources. At the end, you will have a repository with:

- simple LightGBM training workflow running every 2 hours and on push/PR
- code format check on push/PR
- resource cleanup script running nightly

## Setup

First, export your Azure subscription id as an environment variable:

```console
export ID=<your-subscription-id>
```

Second, create the Azure resource group and required AML resources:

```console
python setup-workspace.py --subscription-id $ID
```

This will create a resource group named `azureml-template`, a workspace named `default`, and a cluster named `cpu-cluster`. Edit `setup-workspace.py` as needed. If you change the names, ensure you change corresponding names in the `.github/workflows` files and in the third step below.

Third, create a service principal for the resource group:

```console
az ad sp create-for-rbac --name "azureml-template" \
                         --role contributor \
                         --scopes /subscriptions/$ID/resourceGroups/azureml-template \
                         --sdk-auth
```

Copy the output json, which looks like this:

```console
{
    "clientId": "<GUID>",
    "clientSecret": "<GUID>",
    "subscriptionId": "<GUID>",
    "tenantId": "<GUID>",
    (...)
}
```

In your repository, navigate to "Settings > Secrets > New Secret". Name the secret `AZ_CREDS` and paste the json output from above. This is used in the Azure login action in the GitHub Actions. If you use a different name for the secret, ensure you change the corresponding names in the `.github/workflows` files.

## Contents

You can utilize the structure for automating the entire ML lifecycle on GitHub, using AML for central tracking and scaling up/out on Azure compute.

|directory|description|
|-|-|
|`.cloud`|cloud templates|
|`.github`|GitHub specific files like Actions workflow yaml definitions and issue templates|
|`code`|ML code|
|`environments`|environment definition files such as conda yaml, pip txt, or dockerfile|
|`mlprojects`|mlflow project specifications|
|`notebooks`|interactive jupyter notebooks for iterative ML development|
|`workflows`|AML control plane specification (currently Python scripts) of job(s) to be run|

## GitHub Actions

Modify all actions and files as needed.

**Actions**:

- [`.github/workflows/smoke.yml`](.github/workflows/smoke.yml) runs on every PR and push to `main` to check code format
- [`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml) runs daily and can be used to cleanup AML resources
- [`.github/workflows/run-workflows.yml`](.github/workflows/run-workflows.yml) runs a ml workflow every two hours and push/PR to `main`

**Other**:

- [`cleanup.py`](cleanup.py) can be modified for nightly workspace cleanup tasks
- [`setup-workspace.py`](setup-workspace.py) can be modified for workspace and resource setup
- [`code/train.py`](code/train.py) is the ML training script with mlflow tracking
- [`workflows/default.py`](workflows/default.py) is the AML control code
- [`environments/env.txt`](environments/env.txt) specifies required pip packages for the training script

## Reference

- [Azure Machine Learning Examples](https://github.com/Azure/azureml-examples)
- [Azure Machine Learning Documentation](https://docs.microsoft.com/azure/machine-learning)
