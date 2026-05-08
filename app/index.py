import flet as ft
import asyncio

from ui.views.index_view import index_view
from ui.views.signup_view import signup_view
from services.main import main

storage = None

async def run(page: ft.Page):
    page.fonts = {
        "Pixel": "fonts/pixel.ttf"
    }
    async def load_app():
        await page.push_route("/signup")
        storage = services.dbInit("./db.sqlite")
        page.update()
    
    async def route_change():
        if page.route == '/':
            page.views.clear()
            page.views.append(index_view())
            await asyncio.sleep(2)

            await load_app()
        
        elif page.route == "/signup":
            page.views.clear()
            if storage != None:
                page.views.append(signup_view(storage=storage))
            page.update()
    
        page.update()
    
    page.on_route_change = route_change
    page.push_route('/')
    

    await route_change()

if __name__ =="__main__":
    main()
    ft.run(run,assets_dir="assets")