# Lungs X-ray Classification

## Workflow

- constants
- config_entity
- artifact_entity
- components
- pipeline
- main

## Create project folder

```bash
git init
```
```bash
git remote -v 
```
(to check if any git repository connected)

## Connect to git repository
```bash
git remote add origin https://github.com/ayushrjc/DLproject.git
```
```bash
git pull origin main
```
## To push the changes
```bash
git add .
```
```bash
git commit -m "project structure updated"
```
```bash
git branch -M main
```
```bash
git push origin main
```

## Create environment

```bash
conda create -p venv python=3.8 -y
```
```bash
source activate ./venv
```
OR 
```bash
conda activate ./venv
```

## Configure AWS CLI
```bash
aws configure
```
```bash
AWS_ACCESS_KEY_ID= ***

AWS_SECRET_ACCESS_KEY= ***

AWS_REGION= us-east-1
```