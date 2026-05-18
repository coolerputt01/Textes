import flet as ft

import sys, os
from ..components.loading_circler import LoadingButton
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../..")
from services.auth.auth import create_user

def signup_view(storage):
    def handle_signup(e):
        result = create_user(
            username=username.value.encode("utf-8")
            )
        if result == 0:
            print("User created")
        else:
            print("Username taken or invalid")

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
                    LoadingButton(
                        content="Okay!",
                        width=360,
                        on_click=handle_signup
                    )
                ]
            )
        ]
    )