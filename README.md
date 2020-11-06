# Azure Machine Learning (AML) GitHub Template

[![run-workflows-badge](https://github.com/Azure/azureml-template/workflows/run-workflows/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Arun-workflows)
[![cleanup](https://github.com/Azure/azureml-template/workflows/cleanup/badge.svg)](https://github.com/Azure/azureml-template/actions?query=workflow%3Acleanup)
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

## Contents

This example repo is structured for real ML projects. You can utilize the structure for automating the entire ML lifecycle on GitHub using AML.

|directory|description|
|-|-|
|`.cloud`|cloud templates|
|`.github`|GitHub specific files like Actions workflow yaml definitions and issue templates|
|`code`|ML code organized by scenario (train, deploy, etc.) then tool (pytorch, tensorflow, etc.)|
|`environments`|environment definition files such as conda yaml, pip txt, or dockerfile|
|`mlprojects`|mlflow project specifications|
|`notebooks`|interactive jupyter notebooks for iterative ML development|
|`workflows`|AML control plane specification (currently Python scripts) of job(s) to be run|

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Please see the [code of conduct](CODE_OF_CONDUCT.md) for details.
