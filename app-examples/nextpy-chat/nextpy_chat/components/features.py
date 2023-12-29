import nextpy as xt

from nextpy_chat import styles

def features() -> xt.Component:
    """Various features for menu"""
    return (
        xt.menu(
            xt.menu_button(
                xt.image(src="/Vector.svg", width="1.2em", height="auto"),
                class_name = 'min-w-[1.2em]'
            ),
            xt.menu_list(
                xt.menu_item(
                    xt.link(
                        xt.hstack(
                            xt.image(
                                src='/logo.png' , width = '25px', height = '25px', mx='4px'
                            ),
                            xt.text(
                                "NEXTPY GPT",
                                color = '#071952',
                                font_weight = 'bold'
                            ),
                        ),
                        href="http://localhost:3000",
                    ),
                    bg = '#00ADB5'
                ),
                xt.menu_divider(),
                xt.menu_item(
                    xt.link(
                        xt.hstack(
                            xt.image(
                                src='/interview_prep.png' , width = '25px', height = '25px', mx='4px'
                            ),
                            xt.text(
                                "Interview Preparation Helper",
                                color = '#ffffff',
                                font_weight = 'bold',
                            )
                        ),
                        href="http://localhost:3000/interview_prep",
                    ),
                    py = '1em',
                    bg = '#00ADB5'
                ),
                xt.menu_item(
                    xt.link(
                        xt.hstack(
                            xt.image(
                                src='/interview_prep.png' , width = '25px', height = '25px', mx='4px'
                            ),
                            xt.text(
                                "Example",
                                color = '#ffffff',
                                font_weight = 'bold'
                            ),               
                        ),
                        href="http://localhost:3000/interview_prep",
                    ),
                    py = '1em',
                    bg = '#00ADB5'
                ),
                my = '1em',
                bg = '#00ADB5'
            ),
            bg = '#00ADB5'
        )
    )

