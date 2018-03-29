"""Handle commands of a user according to their request"""
from yellowant.messageformat import MessageClass, MessageAttachmentsClass, MessageButtonsClass, AttachmentFieldsClass
from db import Database


# mock database
database = Database()

class Commands:
    """Handles user commands
    
    Args:
        yellowant_integration_id (int): The integration id of a YA user
        command_name (str): Invoke name of the command the user is calling
        args (dict): Any arguments required for the command to run
    """
    def __init__(self, yellowant_integration_id, command_name, args):
        self.yellowant_integration_id = yellowant_integration_id
        self.command_name = command_name
        self.args = args

        self.user_integration = database.get_user_integration(self.yellowant_integration_id)
        self.command = commands_by_invoke_name.get(self.command_name)
    
    def parse(self):
        message = MessageClass()
        
        if self.yellowant_integration_id is None:
            message.message_text = "Sorry! I could not find your integration."
        
        elif self.command is None:
            message.message_text = "Sorry! I could not find that command."
        
        return self.command(self.args, self.user_integration)


### Sample commands ###
commands_by_invoke_name = {
    "createitem": create_item,
    "getlist": get_list,
    "getitem": get_item,
    "updateitem": update_item,
    "deleteitem": delete_item,
}


todo_list = [
    {
        "id": 0,
        "title": "Setup a YellowAnt account",
        "description": "Sign up on YellowAnt with Slack or Microsoft."
    },
    {
        "id": 1,
        "title": "Integrate an app from the marketplace",
        "description": "Head over to https://www.yellowant.com/marketplace/ to integrate your favorite app."
    },
    {
        "id": 2,
        "title": "Issue a basic command",
        "description": "Type `help` in your chat application to start using your integration."
    },
    {
        "id": 3,
        "title": "Create a YellowAnt application",
        "description": "Register your application on https://www.yellowant.com/developers/. Setup a server with the appropriate URL endpoints and application logic."
    },
    {
        "id": 4,
        "title": "Use your integrations in automated workflows",
        "description": "Automate your routine by heading over to https://www.yellowant.com/workflows/ and start connecting multiple apps to build powerful workflows."
    },
]
todo_id_counter = 4

def create_item(args, user_integration, message=None):
    message = message or MessageClass()

    # verify arguments
    title = args.get("title")
    description = args.get("description")
    if title is None or description is None or len(title) == 0 or len(description) == 0:
        # inform the user that they have not provided valid arguments
        message.message_text = "You need to provide values for both `title` and `description` as arguments."
        return message
    
    # create an item in the todo list
    todo_id_counter += 1
    new_item = {
        "id": todo_id_counter,
        "title": title,
        "description": description,
    }
    todo_list.append(new_item)

    # build return message for the user
    message.message_text = "You have created a new item:"
    message.attach(item_attachment(new_item, user_integration))

    return message

def get_list(args, user_integration, message=None):
    message = message or MessageClass()

    # inform the user if the todo list is empty
    if len(todo_list) == 0:
        message.message_text = "Your todo list is empty"
        return message
    
    # create message with the list of todos
    message.message_text = "Here are your todo items:"
    for item in todo_list: # a message can have multiple attachments
        message.attach(item_attachment(item, user_integration))
    return message

def get_item(args, user_integration, message=None):
    message = message or MessageClass()

    # verify args
    try:
        # since an item's id is supposed to be an integer, we will try casting the argument `id` to an int
        item_id = int(args.get("id"))
    except:
        # inform the user that they need to provide a valid integer id
        message.message_text = "You need to provide an integer value for the argument `id`."
        return message
    
    # inform the user if the item was not found by the id
    item_search = filter(lambda item: item.get("id") == item_id, todo_list)
    if len(item_search) == 0:
        message.message_text = "Could not find todo item with the id: {}".format(item_id)
        return message
    
    # create message for the found item
    message.message_text = "Here are the item details:"
    message.attach(item_attachment(item_search[0], user_integration))
    
    return message


def update_item(args, user_integration, message=None):
    message = message or MessageClass()

    # helper method
    def item_updater(old_item, updated_item):
        if updated_item.get("id") == old_item.get("id"):
            old_item["title"] = updated_item.get("title", old_item["title"])
            old_item["description"] = updated_item.get("description", old_item["description"])
        
        return old_item

    # verify args
    title = args.get("title")
    description = args.get("description")
    try:
        # since an item's id is supposed to be an integer, we will try casting the argument `id` to an int
        item_id = int(args.get("id"))
    except:
        # inform the user that they need to provide a valid integer id
        message.message_text = "You need to provide an integer value for the argument `id`."
        return message
    
    # dummy updated item
    updated_item = {
        "id": item_id,
        "title": title,
        "description": description
    }

    # inform the user if the item was not found by the id
    item_search = filter(lambda item: item.get("id") == item_id, todo_list)
    if len(item_search) == 0:
        message.message_text = "Could not find todo item with the id: {}".format(item_id)
        return message
    
    # update todo list
    todo_list = map(lambda item: item_updater(item, updated_item), todo_list)

    # create message with the updated item
    message.message_text = "Here are the updated item details:"
    message.attach(item_attachment(updated_item, user_integration))

    return message


def delete_item(args, user_integration, message=None):
    message = message or MessageClass()

    # verify args
    try:
        # since an item's id is supposed to be an integer, we will try casting the argument `id` to an int
        item_id = int(args.get("id"))
    except:
        # inform the user that they need to provide a valid integer id
        message.message_text = "You need to provide an integer value for the argument `id`."
        return message

    # inform the user if the item was not found by the id
    item_search = filter(lambda item: item.get("id") == item_id, todo_list)
    if len(item_search) == 0:
        message.message_text = "Could not find todo item with the id: {}".format(item_id)
        return message
    
    # remove item from the todo list
    todo_list = filter(lambda item: item.get("id") != item_id, todo_list)

    # create message with the list of todos
    if len(todo_list) == 0:
        message.message_text = "Your todo list is empty."
    else:
        message.message_text = "Here are your todo items:"
        for item in todo_list: # a message can have multiple attachments
            message.attach(item_attachment(item, user_integration))
    return message    


### YA Message Attachment Builders ###
def item_attachment(item, user_integration, attachment=None):
    attachment = attachment or MessageAttachmentsClass()
    attachment.title = item.get("title")
    attachment.text = item.get("description")

    attachment.attach_field(AttachmentFieldsClass("ID", 1, item.get("id")))

    attachment.attach_button(update_item_button(item, user_integration))

    return attachment


### YA Message Button Builders ###
def update_item_button(item, user_integration, text="Update", value=0, name=0):
    button = MessageButtonsClass()
    button.text = text
    button.value = value
    button.name = name
    
    button.command = {
        "function_name": "updateitem",
        "service_application": user_integration.yellowant_integration_id,
        "data": {
            "id": item.get("id")
        },
        "inputs": [
            "title",
            "description"
        ]
    }

    return button