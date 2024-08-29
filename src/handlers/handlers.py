from .error import handler as error
from . import debug
from . import info
from . import upload

# TODO: import your handlers here

# Debug handlers
debug_handlers = []
for module in [debug, info, upload]:
    debug_handlers.extend(module.create_handlers())
# Business logic handlers
logic_handlers = []
for module in []: # TODO: insert your handlers here
    logic_handlers.extend(module.create_handlers())
# All handlers (debug + logic)
all = debug_handlers + logic_handlers
