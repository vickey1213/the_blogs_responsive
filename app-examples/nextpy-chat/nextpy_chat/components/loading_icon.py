import nextpy as xt

class LoadingIcon(xt.Component):
    """A custom loading icon component."""

    library = "react-loading-icons"
    tag = "SpinningCircles"
    stroke: xt.Var[str]
    stroke_opacity: xt.Var[str]
    fill: xt.Var[str]
    fill_opacity: xt.Var[str]
    stroke_width: xt.Var[str]
    speed: xt.Var[str]
    height: xt.Var[str]

    def get_event_triggers(self) -> dict:
        return {"on_change": lambda status: [status]}


loading_icon = LoadingIcon.create