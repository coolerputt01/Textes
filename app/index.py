from ui.views import index_view,signup_view
import flet as ft
import asyncio

async def main(page: ft.Page):
    page.fonts = {
        "Pixel": "fonts/pixel.ttf"
    }
    async def load_app():
        await page.push_route("/signup")
        page.update()
    
    async def route_change():
        if page.route == '/':
            page.views.clear()
            page.views.append(index_view())
            await asyncio.sleep(2)

            await load_app()
        
        elif page.route == "/signup":
            page.views.clear()
            page.views.append(signup_view())
            page.update()
    
        page.update()
    
    page.on_route_change = route_change
    page.push_route('/')
    

    await route_change()

ft.run(main,assets_dir="assets")