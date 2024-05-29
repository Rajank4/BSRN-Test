from textual.app import App, ComposeResult
from textual.widgets import Static


class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static("Buzzword Bingo")

        yield self.widget

    def on_mount(self) -> None:
        self.widget.styles.background = "aquamarine"
        self.widget.styles.color = "black"
        self.widget.styles.border = ("heavy", "black")

if __name__ == "__main__":
    app = WidgetApp()
    app.run()