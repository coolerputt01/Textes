import flet as ft
import asyncio

from ui.views.index_view import index_view
from ui.views.signup_view import signup_view
from services.db_handler import db_init

app_state = {"storage": None}

async def run(page: ft.Page):
    page.fonts = {
        "Pixel": "fonts/pixel.ttf"
    }
    async def load_app():
        await page.push_route("/signup")
        app_state["storage"] = db_init("./db.sqlite")
        page.update()
    
    async def route_change():
        if page.route == '/':
            page.views.clear()
            page.views.append(index_view())
            await asyncio.sleep(2)

            await load_app()
        
        elif page.route == "/signup":
            page.views.clear()
            page.views.append(signup_view(storage=app_state["storage"]))
            page.update()
    
        page.update()
    
    page.on_route_change = route_change
    await page.push_route('/')
    

    await route_change()

if __name__ =="__main__":
    ft.run(run,assets_dir="assets",port=8080,web_renderer=ft.WebRenderer.CANVAS_KIT)