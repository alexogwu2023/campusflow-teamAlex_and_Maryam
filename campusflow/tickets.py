def check_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be text")
    
    title = title.strip()
    if len(title) == 0:
        raise ValueError("Title cannot be blank")
        
    return title

def check_category(category):
    if not isinstance(category, str):
        raise ValueError("category must be text")

    cleaned = category.strip().lower()
    allowed_name = ["Network", "Hardware", "Software", "Other"] 

    for official_name in allowed_name:
        if official_name.lower() == cleaned:
            return official_name
        
    raise ValueError("Category must be one of: Network, Hardware, Software, Other")

def check_urgency(urgency):
    if not isinstance(urgency, str):
        raise ValueError("Urgency must be text")

    cleaned = urgency.strip().lower()
    if cleaned != "low" and cleaned != "medium" and cleaned != "high":
        raise ValueError("Urgency must be low, medium or high")

    return cleaned



    

    

    




