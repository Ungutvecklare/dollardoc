# Language: English
# Creation Date: 2023-06-02
# File description: Contains all the error constants used in Dollar.
# This was done to make it easier to modify/remove/add error messages without having to search through the codebase.

# Category: DollarObject - General
INVALID_DOLLAR_OBJECT = "Object is not a valid DollarObject"
DOLLAR_OBJECT_IS_WRONG_TYPE = "Dollar object is of wrong type"

# Category: DollarObject - Creation
DOLLAR_OBJECT_ID_EXISTS = "DollarObject with id {0} already exists"  # format: id <string>
DOLLAR_OBJECT_ID_DOES_NOT_EXIST = "DollarObject with id {0} does not exist"  # format: id <string>

# Category: Config
KEY_NOT_PROVIDED_IN_CONFIG = "Key {0} was not provided in the config"  # format: key <string>
KEY_MUST_BE_PROVIDED_IN_CONFIG = "Key {0} must be provided in the config"  # format: key <string>
KEY_NOT_LIST_OR_STRING = "Key {0} was not a list or string as expected"  # format: key <list/string>
REQUIRED_CONFIG_NOT_PRESENT = "Required config {0} not present in the config"  # format: config name <string>

# Category: File operations
FAILED_TO_OPEN_FILE = "Failed to open file {0}"  # format: file name <string>
FAILED_TO_READ_FILE = "Failed to read file {0}"  # format: file name <string>
FILE_NOT_FOUND = "File not found: {0}"  # format: file name <string>
COULD_NOT_WRITE_FILE = "Could not write file {0}"  # format: file name <string>

# Category: Path/File location
INVALID_PATH_STRING = "Path passed to DollarFile must be valid string"
INVALID_FILE_TYPE = "File Ending passed to DollarFile must be valid string"

# Category: Plugin loading and execution
BLOCK_PLUGIN_NOT_FOUND = "Block plugin with name {0}, cannot be found"  # format: block name <string>
BLOCK_PLUGIN_WRONG_TYPE = "Block plugin is of wrong type"
EXTENSION_PLUGIN_NOT_FOUND = "Extension plugin with name {0}, cannot be found"  # format: extension name <string>
FUNCTION_PLUGIN_NOT_FOUND = "Function plugin with name {0}, cannot be found"  # format: function name <string>
FUNCTION_PLUGIN_WRONG_TYPE = "Function plugin is of wrong type"
NO_EXTENSION_HANDLER = "No extension plugin with handler for secondary key {0}"  # format: secondary key <string>
UNSUPPORTED_PLUGIN_TYPE = "Plugin with type {0} is not supported"  # format: plugin type <string>

# Category: Blank checks
BLOCK_NAME_NOT_BLANK = "Block name can not be blank"
FUNCTION_NAME_NOT_BLANK = "Function name can not be blank"
PARAMETER_CANNOT_BE_EMPTY = "Parameter {0} cannot be empty"  # format: parameter name <string>
TARGET_TEXT_NOT_BLANK = "Target text can not be blank"
TEXT_NOT_BLANK = "Text can not be blank"

# Category: Parsing
ALREADY_PARSING_DOLLAR = "Already parsing dollar"

# Category: Formatting
DOLLAR_FUNCTION_NOT_FORMATED_CORRECTLY = "Dollar Function is not formatted properly"
ERR_LIST_FIRST_ITEM = "List can not be the first item inside a List"
ERR_UNSUPPORTED_LIST_FORMAT = "Format {0} is not supported on List"  # format: format <string>
INVALID_FORMAT = "Format {0} is not supported"  # format: format <string>
INVALID_ID_STRING = "Id must be a valid string"
INVALID_STRING = "String must be a valid string"
UNION_CONTAINS_UNION = "Union can not contain another union"

# Category: Scope Restriction
DOLLAR_REFERENCE_SCOPE_RESTRICTION = "Dollar reference can only be used locally"