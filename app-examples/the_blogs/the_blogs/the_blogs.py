"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
from xtconfig import config

import nextpy as xt


filename = f"{config.app_name}/{config.app_name}.py"


class State(xt.State):
    """The app state."""

    pass


# Assuming all necessary Nextpy components are correctly imported
import nextpy as xt


def Navbar() -> xt.Component:
    return xt.box(
        xt.hstack(
            xt.link(
                xt.image(src="/logo_darkmode.svg", width="120px"),
                href="/",
            ),
            xt.box(
                xt.link(
                    "Manifesto",
                    href="/manifesto",
                    font_size="14px",
                    color="white",
                    _hover={"text_decoration": "none"},
                    class_name="py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]",
                ),
                xt.link(
                    "Documentation",
                    href="https://github.com/dot-agent/nextpy/tree/main/docs",
                    color="white",
                    font_size="14px",
                    # bg="#EDEEF0",
                    _hover={"text_decoration": "none"},
                    class_name="py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]",
                ),
                xt.link(
                    "Hackathon",
                    color="white",
                    href="https://discord.gg/w7fNkUsaWf",
                    font_size="14px",
                    _hover={"text_decoration": "none"},
                    class_name="py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]",
                ),
                xt.link(
                    "App Templates",
                    color="white",
                    href="https://github.com/dot-agent/nextpy/tree/main/app-examples",
                    font_size="14px",
                    _hover={"text_decoration": "none"},
                    class_name="py-1 px-2  rounded-md text-white hover:text-[#111113] hover:bg-[#EDEEF0]",
                ),
                class_name="gap-6 items-center text-sm lg:flex hidden",
            ),
            xt.box(
                xt.link(
                    "Support",
                    href="https://github.com/dot-agent/nextpy",
                    color="#D0D1D3",
                    font_size="14px",
                    _hover={"text_decoration": "none"},
                ),
                xt.link(
                    xt.image(src="/discord.svg", width="1.2rem"),
                    href="https://discord.gg/g9PFpVztZg",
                    is_external=True,
                ),
                xt.link(
                    xt.image(src="/github-mark.svg", width="1.2rem"),
                    href="https://github.com/dot-agent/nextpy",
                    is_external=True,
                ),
                # xt.link(
                #     xt.image(src="/colormode.svg", width="1.2rem"),
                #     is_external=True,
                # ),
                class_name="flex items-center flex-row gap-6",
            ),
            justify_content="space-between",
            align_items="center",
        ),
        height="55px",
        class_name="py-2 sm:px-8 px-4 ",
        width="100%",
    )


# Other parts of your code remain the same


def Heading():
    return xt.box(
        xt.box(
            xt.divider(border_color="white"),
            xt.text(
                "THE BLOG",
                class_name="lg:text-9xl text-6xl md:text-[150px] font-bold pb-4 ",
            ),
            xt.divider(border_color="white"),
            # width="80%",
            class_name="w-full lg:w-4/5 ",
        ),
        class_name="flex justify-center text-center pb-10 ",
    )


def RecentBlogs():
    return xt.box(
        xt.box(
            xt.image(
                src="Image.svg",
                # width="592px",
                # height="228px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-3 pt-6",
            ),
            xt.text(
                "UX review presentations",
                class_name="text-xl pb-3",
            ),
            xt.text(
                "How do you create compelling presentations that wow your colleagues and impress your managers?",
                class_name="text-sm pb-6",
            ),
            xt.hstack(
                xt.text(
                    "Design",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full px-4 py-2 items-center",
                ),
                xt.text(
                    "Research",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full px-4 py-2 text-center",
                ),
                xt.text(
                    "Presentation",
                    class_name="text-sm text-[#C11574] bg-white rounded-full px-4 py-2 text-center ",
                ),
            ),
        ),
    )


def MirgartingCard():
    return xt.box(
        xt.box(
            # Box for the image
            xt.box(
                xt.image(
                    src="Image (1).svg",
                    # width="320px",
                    # height="200px",
                    class_name="w-full h-full",
                ),
                class_name="flex-1",  # Adjust as needed for desired sizing
            ),
            # Box for all text components
            xt.box(
                xt.flex(
                    xt.text(
                        "Sunday, 1 Jan 2023",
                        class_name="text-sm text-[#6941C6] pb-3 ",
                    ),
                    xt.text(
                        "Migrating to Linear 101",
                        class_name="text-xl pb-3",
                    ),
                    xt.text(
                        "Linear helps streamline software projects, sprints, tasks, and bug tracking. Here's how to get...",
                        class_name="text-sm pb-6",
                    ),
                    xt.hstack(
                        xt.text(
                            "Design",
                            class_name="text-sm text-[#027A48] bg-white rounded-full px-4 py-2 items-center",
                        ),
                        xt.text(
                            "Research",
                            class_name="text-sm text-[#C11574] bg-white rounded-full px-4 py-2 text-center",
                        ),
                    ),
                    class_name="flex flex-col items-start justify-start",
                ),
                class_name="flex-1",
            ),
            class_name="gap-4 flex flex-col md:justify-center md:flex-row justify-start items-start",
        ),
    )


def BuildingCard():
    return xt.box(
        xt.box(
            # Box for the image
            xt.box(
                xt.image(
                    src="Image (2).svg",  # Ensure this path is correct
                    # width="320px",
                    # height="200px",
                    class_name="w-full h-full",
                ),
                class_name="flex-1",  # Ensure Tailwind CSS is properly configured
            ),
            # Box for all text components
            xt.box(
                xt.flex(
                    xt.text(
                        "Sunday, 1 Jan 2023",
                        class_name="text-sm text-[#6941C6] pb-4 pt-4",
                    ),
                    xt.text(
                        "Building your API Stack",
                        class_name="text-xl pb-3",
                    ),
                    xt.text(
                        "The rise of RESTful APIs has been met by a rise in tools for creating, testing, and managing them.",
                        class_name="text-sm pb-4",
                    ),
                    xt.hstack(
                        xt.text(
                            "Design",
                            class_name="text-sm text-[#6941C6] bg-white rounded-full px-4 py-2 items-center",
                        ),
                        xt.text(
                            "Research",
                            class_name="text-sm text-[#3538CD] bg-white rounded-full px-4 py-2 text-center",
                        ),
                    ),
                    class_name="flex flex-col items-start justify-start ",
                ),
                class_name="flex-1",
            ),
            class_name="gap-4 flex flex-col md:justify-center md:flex-row justify-start items-start",
        ),
    )


def GridSystemCard():
    return xt.flex(
        # Box for the image
        xt.box(
            xt.image(
                src="Image (3).svg",  # Ensure this path is correct
                width="592px",
                height="246px",
            ),
            class_name="flex-1",  # Adjust as needed for desired sizing
        ),
        # Box for all text components
        xt.box(
            xt.flex(
                xt.text(
                    "Sunday, 1 Jan 2023",
                    class_name="text-sm text-[#6941C6] pb-4 pt-4",
                ),
                xt.text(
                    "Grid system for better Design User Interface",
                    class_name="text-xl pb-4",
                ),
                xt.text(
                    "A grid system is a design tool used to arrange content on a webpage. It is a series of vertical and horizontal lines that create a matrix of intersecting points, which can be used to align and organize page elements. Grid systems are used to create a consistent look and feel across a website, and can help to make the layout more visually appealing and easier to navigate.",
                    class_name="text-sm pb-4",
                ),
                xt.hstack(
                    xt.text(
                        "Design",
                        class_name="text-sm text-[#027A48] bg-white rounded-full px-4 py-2",
                    ),
                    xt.text(
                        "Interface",
                        class_name="text-sm text-[#C11574] bg-white rounded-full px-4 py-2 ",
                    ),
                ),
                class_name="flex flex-col items-start justify-start",
            ),
            class_name="flex-1",  # Adjust as needed for desired sizing
        ),
        class_name="flex items-center justify-center flex-col md:flex-row  h-[306] gap-6 ",  # This ensures that the hstack behaves like a flex container
    )


def BillCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (4).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "Bill Walsh leadership lessons",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "Like to know the secrets of transforming a 2-14 team into a 3x Super Bowl winning Dynasty?",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Leadership",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Management",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "Presentation",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def PMCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (5).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "PM mental models",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "Mental models are simple expressions of complex processes or relationships.",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Prodct",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Reseach",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "Framework",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def WireframingCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (6).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "What is Wireframing?",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "Introduction to Wireframing and its Principles. Learn from the best in the industry.",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Design",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Reseach",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "Presentation",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def ColborationCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (7).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "How collaboration makes us better designers",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "Collaboration can make our teams stronger, and our individual designs better.",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Design",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Reseach",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "Presentation",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def JavascriptCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (8).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "Our top Ten Javascript frameworks  to use",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "JavaScript frameworks make development easy with extensive features and functionalities.",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Software Development",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Tools",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "SaaS",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def PodcastCard():
    return xt.box(
        xt.box(
            xt.image(
                src="Image (9).svg",
                width="384px",
                height="240px",
            ),
            xt.text(
                "Sunday, 1 Jan 2023",
                class_name="text-sm text-[#6941C6] pb-4 pt-4",
            ),
            xt.text(
                "Podcast: Creating a better CX Community",
                class_name="text-xl pb-4",
            ),
            xt.text(
                "Starting a community doesn’t need to be complicated, but how do you get started?",
                class_name="text-sm pb-4",
            ),
            xt.hstack(
                xt.text(
                    "Podcast",
                    class_name="text-sm text-[#6941C6] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 items-center",
                ),
                xt.text(
                    "Customer Success",
                    class_name="text-sm text-[#3538CD] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center",
                ),
                xt.text(
                    "Presentation",
                    class_name="text-sm text-[#C11574] bg-white rounded-full xl:px-4  xl:py-2 px-2 py-1 text-center ",
                ),
            ),
        ),
    )


def index() -> xt.Component:
    return xt.fragment(
        Navbar(),
        Heading(),
        xt.box(
            xt.box(
                xt.box(
                    RecentBlogs(),
                ),
                xt.box(
                    MirgartingCard(),
                    BuildingCard(),
                    class_name="grid grid-rows-2 gap-6",
                ),
                class_name="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-6",
            ),
            GridSystemCard(),
            xt.box(
                BillCard(),
                PMCard(),
                WireframingCard(),
                ColborationCard(),
                JavascriptCard(),
                PodcastCard(),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
            class_name="flex flex-col gap-6 py-6 px-4 xl:px-48",
        ),
    )


# Add state and page to the app.
app = xt.App()
app.add_page(index)
app.compile()
