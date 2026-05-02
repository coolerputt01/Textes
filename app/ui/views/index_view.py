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