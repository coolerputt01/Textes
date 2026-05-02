import flet as ft
from modules.services import services

def signup_view(storage):
    return ft.View(
        route="/signup",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Enter Username",font_family="Pixel",size=10,text_align=ft.TextAlign.LEFT,color=ft.Colors.GREY_700),
                    username := ft.TextField(
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
                        on_click=lambda _: services.createUser(storage, username.value, ""),
                        margin=ft.Margin.only(top=10),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=20),
                            bgcolor={
                                ft.ControlState.DEFAULT: ft.Colors.GREEN_300,
                                ft.ControlState.HOVERED: ft.Colors.GREEN_500,
                                ft.ControlState.PRESSED: ft.Colors.GREEN_700,
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