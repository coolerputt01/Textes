import flet as ft


def index_view():
    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Image(
                        src="img/illustrations/blink.gif",
                        width=200,
                        filter_quality=ft.FilterQuality.HIGH,
                        border_radius=10
                    ),
                    ft.Text(
                        "Textes",
                        font_family="Pixel",
                        size=48,
                        weight=ft.FontWeight.BOLD
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
    )

def signup_view():
    return ft.View(
        route="/signup",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Enter Username",font_family="Pixel",size=10,text_align=ft.TextAlign.LEFT,color=ft.Colors.GREY_700),
                    ft.TextField(
                        value="",
                        text_align=ft.TextAlign.LEFT,
                        width=350,
                        autocorrect=False,
                        hint_text="Type something...",
                        text_style=ft.TextStyle(
                            font_family="Pixel",
                            size=14
                        ),
                    ),
                    ft.Button(
                        content="Okay!",
                        width=360,
                        margin=ft.margin.only(top=10),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=20),
                            bgcolor={
                                ft.ControlState.DEFAULT: ft.Colors.GREEN_200,
                                ft.ControlState.HOVERED: ft.Colors.GREEN_400,
                                ft.ControlState.PRESSED: ft.Colors.GREEN_600,
                            },
                            color=ft.Colors.WHITE,
                            padding=ft.Padding(20, 10, 20, 10),
                            text_style=ft.TextStyle(
                                font_family="Pixel",
                                size=12
                            ),
                        ),
                    )
                ]
            )
        ]
    )