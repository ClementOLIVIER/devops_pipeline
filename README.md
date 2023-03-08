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
**login**: clementolivier

**password**: SuchAS€cureP@ssw°rd


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
