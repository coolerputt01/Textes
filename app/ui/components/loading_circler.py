import flet as ft

def LoadingButton(content, on_click, width=360):
    loader = ft.ProgressRing(width=20, height=20, stroke_width=2, color=ft.Colors.WHITE)

    def button_click_wrapper(e):
        btn.content = loader
        btn.disabled = True
        btn.update()

        try:
            on_click(e)
        finally:
            btn.content = content
            btn.disabled = False
            btn.update()

    
    btn = ft.Button(
        content=ft.Text(content, font_family="Pixel", size=12),
        width=width,
        on_click=button_click_wrapper,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.GREEN_300,
                ft.ControlState.HOVERED: ft.Colors.GREEN_500,
                ft.ControlState.PRESSED: ft.Colors.GREEN_700,
            },
            color=ft.Colors.WHITE,
            padding=ft.Padding(20, 10, 20, 10),
        ),
    )
    return btn
