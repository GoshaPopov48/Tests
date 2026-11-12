from uuid import uuid4



def generated_name_project(prefix: str):
    suffix = uuid4().hex[:6]
    return f"{prefix}_{suffix}"

def generated_id_project(prefix: str):
    suffix = uuid4().hex[:3]
    return f"{prefix}_{suffix}"


def generated_name_issues(prefix: str):
    suffix = uuid4().hex[:10]
    return f"{prefix}_{suffix}"

def generated_description_issue(prefix: str):
    suffix = uuid4().hex[:100]
    return f"{prefix}_{suffix}"