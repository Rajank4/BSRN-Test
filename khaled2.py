from textual.app import App, ComposeResult
from textual.widgets import Static, Button

class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static("Buzzword Bingo")

        # Erstelle ein 5x5 Raster mit Buttons
        for i in range(5):
            for j in range(5):
                button = Button(f"Button {i+1}-{j+1}")
                yield button

        yield self.widget

    def on_mount(self) -> None:
        self.widget.styles.background = "aquamarine"
        self.widget.styles.color = "black"
        self.widget.styles.border = ("heavy", "black")
        self.widget.styles.width = 17

if __name__ == "__main__":
    app = WidgetApp()
    app.run()
