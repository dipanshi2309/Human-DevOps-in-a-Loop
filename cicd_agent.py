from config import model

def cicd_agent(project_description):
    
    prompt = f"""
    Generate Github Actions workflow.
    
    Project:
    (project_description)
    """
    
    response = model.generate_content(prompt)
    
    return response.text