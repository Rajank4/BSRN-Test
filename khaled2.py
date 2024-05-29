from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.widgets import Welcome

class TestButton(Static):
    def compose(self):
    #def for schleife für bestimmung der breite
        yield Button("Welcome")
        yield Button("Word")
        yield Button("tete")
        yield Button("tutu")
        yield Button("haloo")

class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static("Buzzword Bingo")
        yield self.widget
    # def for schleife für bestimmung der laenge

        yield TestButton()
        yield TestButton()
        yield TestButton()
        yield TestButton()
        yield TestButton()
    CSS = """
    TestButton {
        layout: horizontal;
    }
    """
    def on_mount(self) -> None:
        self.widget.styles.background = "aquamarine"
        self.widget.styles.color = "black"
        self.widget.styles.border = ("heavy", "black")
        self.widget.styles.width = 17

if __name__ == "__main__":
    app = WidgetApp()
    app.run()