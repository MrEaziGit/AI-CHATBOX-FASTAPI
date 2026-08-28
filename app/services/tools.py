from datetime import datetime
from app.services.business__db import check_order, find_customer, add_order, update_order, cancel_order, add_customer

def calculate(a, b):
    return a + b


def get_time():
    return datetime.now().strftime("%H:%M:%S")



tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number."
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number."
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
       {
        "type": "function",
        "function": {
            "name": "check_order",
            "description": "Look up a customer's order using the order ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The customer's order ID."
                    }
                },
                "required": ["order_id"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "find_customer",
            "description": "Find all orders belonging to a customer by their name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer": {
                        "type": "string",
                        "description": "The customer's name."
                    }
                },
                "required": ["customer"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_order",
            "description": "create a new customer order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The unique order ID."
                    },
                    "customer": {
                        "type": "string",
                        "description": "The customer name",
                    },
                    "status": {
                        "type": "string",
                        "description": "The current status of the order",
                    },
                    "total": {
                        "type": "string",
                        "description": "The current state of the order"
                    }
                },
                "required": ["order_id", "customer", "status", "total"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_order",
            "description": "Update the status of an existing customer order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID to update."
                    },
                    "status": {
                        "type": "string",
                        "description": "The new status for the order."
                    }
                },
                "required": ["order_id", "status"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_order",
            "description": "Cancel an existing customer order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID to cancel."
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_customer",
            "description": "Add a new customer to the database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The customer's name."
                    },
                    "email": {
                        "type": "string",
                        "description": "The customer's email address."
                    },
                    "phone": {
                        "type": "string",
                        "description": "The customer's phone number."
                    }
                },
                "required": ["name", "email", "phone"]
            }
        }
    }
]

tool_functions = {
    "calculate": calculate,
    "get_time": get_time,
    "check_order": check_order,
    "find_customer": find_customer,
    "add_order": add_order,
    "update_order": update_order,
    "cancel_order": cancel_order,
    "add_customer": add_customer
}