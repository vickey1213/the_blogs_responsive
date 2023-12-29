"""Declarative layout and common spacing props."""
from __future__ import annotations

from typing import Literal

from nextpy.frontend import dom
from nextpy.backend.vars import Var

from .base import LayoutComponent

LiteralContainerSize = Literal["1", "2", "3", "4"]


class Container(dom.Div, LayoutComponent):
    """Constrains the maximum width of page content.

    See https://www.radix-ui.com/themes/docs/components/container
    """

    tag = "Container"

    # The size of the container: "1" - "4" (default "4")
    size: Var[LiteralContainerSize]
