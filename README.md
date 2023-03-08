# Devops Pipeline
## Project Description
Experimenting a full devops pipeline.

The idea is to:
- Runner a streamlit application inside a docker container
- Implement a GitLab Flow with main and production branches
- Deploy the prodcution branch in Google Cloud environment
- Automatize deployment of the prod branch with a Github Action workflow


Application feature:
- Authentification
- Run a dummy function (that prints anything)

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
- Go to http://localhost:8501

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
- Go to http://localhost:8501


## In Google Cloud Platform
Tutorial: https://www.youtube.com/watch?v=6dLHcnlPi_U
Tools: GCR, 