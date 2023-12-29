"""A heading component."""


from nextpy.frontend.components.libs.chakra import ChakraComponent, LiteralHeadingSize
from nextpy.backend.vars import Var


class Heading(ChakraComponent):
    """A page heading."""

    tag = "Heading"

    # Override the tag. The default tag is `<h2>`.
    as_: Var[str]

    # "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs"
    size: Var[LiteralHeadingSize]
