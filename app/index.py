from ui.views import index_view
import flet as ft

def main(page: ft.Page):
    page.fonts = {
        "Pixel": "fonts/pixel.ttf"
    }
    def route_change():
        if page.route == '/':
            page.views.append(index_view)
    
        page.update()
    
    page.on_route_change = route_change
    page.push_route('/')

    route_change()

ft.run(main,assets_dir="assets")