# Devops Pipeline
## Project Description
Experimenting a full devops pipeline.

The idea is to:
- Run a Streamlit application inside a docker container
- Implement a GitLab Flow with main and production branches
- Deploy the production branch with fly.io
- Automatize the deployment of the production branch with a Github Action workflow


Application feature:
- Authentification
- Tab1: Run a dummy function (that prints anything)
- Tab2: Run a dice game

## Credentials
**Username**: clementolivier

**Password**: SuchAS€cureP@ssw°rd


# Run the application
## Locally
### Install
```bash
pip install -r app/requirements.txt
```

### Run
```bash
streamlit run app/streamlit_app.py
```

### Play with the application
Go to http://localhost:8501

## Locally with Docker
### Build
```bash
docker build -t devops_pipeline .
```

### Run
```bash
docker run -p 8501:8501 devops_pipeline
```

### Play with the application
Go to http://localhost:8501


## Deployed with fly.io
### Play with the application
Go to https://devops-pipeline.fly.dev
