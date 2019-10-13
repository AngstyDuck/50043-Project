from flask import Blueprint

# Import all the view function
from app.modules.endpoint_folder_1.endpoint_1 import endpoint_1

# Define the blueprint name
module = Blueprint("endpoint_folder_1", __name__)

module.add_url_rule("/endpoint_folder_1/register",
                    view_func=endpoint_1, methods=['POST'])
