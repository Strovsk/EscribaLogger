import json
import inspect

def transform_class_into_string(value):
    result = str(value)
    class_params = inspect.signature(value.__init__).parameters
    class_params = list(class_params.keys())
    return result

def process_extra_context(context: dict):
    if not context:
        return ""
    if type(context) is str:
        raise TypeError(
            f"Context must be a object dict, not {type(context).__name__}!!!"
        )

    for key, value in context.items():
        if isinstance(value, type):
            context.update({key: transform_class_into_string(value)})
        elif hasattr(value, '__str__'):
            class_name = value.__class__.__name__
            new_value = f"<object ({class_name})>: {str(value)}"
            context.update({key: new_value})

    return " - " + json.dumps(context)
