from __future__ import annotations
from typing import TYPE_CHECKING
import astroid
from astroid import nodes
import difflib
from pylint.checkers import BaseChecker
from pylint.typing import MessageDefinitionTuple

if TYPE_CHECKING:
    from pylint.lint import PyLinter

# Define valid parameters for each xt method
VALID_PARAMETERS = {
    'text': {"font_size"},
    'vstack': {"spacing", "align_items", "justify_content", "height"},
    'button': {"on_click"},
    # Add other methods and their valid parameters here
}

MSGS: dict[str, MessageDefinitionTuple] = {
    "E9009": (
        "Invalid parameter '%s' in function 'xt.%s'. Did you mean '%s'?",
        "invalid-parameter-in-xt-function",
        "Used when an invalid parameter is used in an xt function."
    ),
}

class InvalidParameterChecker(BaseChecker):
    name = "invalid-parameter"
    msgs = MSGS

    def visit_call(self, node: nodes.Call) -> None:
        if isinstance(node.func, nodes.Attribute) and node.func.attrname in VALID_PARAMETERS:
            module = node.func.expr
            if isinstance(module, nodes.Name) and module.name == 'xt':
                valid_params = VALID_PARAMETERS[node.func.attrname]
                for keyword in node.keywords:
                    if keyword.arg not in valid_params:
                        closest_match = self.find_closest_attribute(keyword.arg, valid_params)
                        self.add_message(
                            'invalid-parameter-in-xt-function', 
                            node=keyword, 
                            args=(keyword.arg, node.func.attrname, closest_match)
                        )

    def find_closest_attribute(self, attr_name: str, valid_attrs: set[str]) -> str:
        closest_matches = difflib.get_close_matches(attr_name, valid_attrs, n=1)
        return closest_matches[0] if closest_matches else "no similar attribute found"

def register(linter: PyLinter) -> None:
    linter.register_checker(InvalidParameterChecker(linter))
