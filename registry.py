"""
Add new AI:s here
"""
import importlib
import pkgutil


def get_ai_list():
    ai_list = []

    # Dynamically discover and import all modules in the ai_contenders package
    for _, module_name, _ in pkgutil.iter_modules(['ai_contenders']):
        module = importlib.import_module(f'ai_contenders.{module_name}')
        # Look for callable objects in the module (like functions or classes)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if callable(attribute):
                ai_list.append(attribute)

    return ai_list

# This allows it to run standalone but also lets other scripts use it
if __name__ == "__main__":
    ai_list = get_ai_list()
    print(ai_list)
