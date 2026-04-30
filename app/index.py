import sys
import slint

sys.path.append("ui")

class App(slint.loader.window.AppWindow):
    @slint.callback
    def request_increase_value(self):
        self.counter = self.counter + 1

app = App()
app.run()