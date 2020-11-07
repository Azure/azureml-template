# Azure Machine Learning (AML) GitHub Template

[![run-workflows-badge](https://github.com/Azure/azureml-template/workflows/run-workflows/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Arun-workflows)
[![cleanup](https://github.com/Azure/azureml-template/workflows/cleanup/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Acleanup)
[![smoke](https://github.com/Azure/azureml-template/workflows/smoke/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Asmoke)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Welcome to the Azure Machine Learning (AML) template repository!

## Prerequisites

1. An Azure subscription. If you don't have an Azure subscription, [create a free account](https://aka.ms/AMLFree) before you begin.
2. Familiarity with Python and [Azure Machine Learning concepts](https://docs.microsoft.com/en-us/azure/machine-learning/concept-azure-machine-learning-architecture).
3. A terminal and Python >=3.6,[\<3.9](https://pypi.org/project/azureml-core).

## Installation

Clone this repository and install required packages:

```sh
git clone https://github.com/Azure/azureml-template
cd azureml-template
pip install --upgrade -r requirements.txt
```

## Setup

First, export your subscription id as an environment variable:

```console
export ID=<your-subscription-id>
```

Second, create the Azure Resource Group and requires resources:

```console
python setup-workspace.py --subscription-id $ID
```

where `$ID` is your subscription id. This will create a resource group named `azureml-template`, a workspace named `default`, and a cluster name `cpu-cluster`. Edit `setup-workspace.py` as needed. If you change the names, ensure you change corresponding names in the `.github/workflow` files.

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

In your GitHub repo, navigate to Settings > Secrets > New Secret. Name the secret `AZ_CREDS` and paste the json output from above.

## Contents

This template is structured for real ML projects. You can utilize the structure for automating the entire ML lifecycle on GitHub, using AML for central tracking and scaling up/out.

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

Modify all actions and files for your scenario. By default:

- [`.github/workflows/smoke.yml`](.github/workflows/smoke.yml) runs on every PR and push to `main` to check code format
- [`.github/workflows/run-workflows.yml`](.github/workflows/run-workflows.yml) runs a ml workflow every two hours and push/PR to `main`
- [`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml) runs daily and can be used to cleanup AML resources
