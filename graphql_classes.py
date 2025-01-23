from importlib import import_module
import os

def collect_resolver_classes(directory):
    """
    Returns a tuple of the classes in either the 
    queries or mutations folder.
    
    (BookMutation, AuthorMutation)
    """
    module_classes = []

    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            class_name = os.path.splitext(item)[0]
            module_path = f"{directory.replace('/', '.')}.{class_name}"
            module = import_module(module_path)

            # Get the actual class 
            class_name = getattr(module, class_name, None)

            if class_name:
                module_classes.append(class_name)

    return module_classes
