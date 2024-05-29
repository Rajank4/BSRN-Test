from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.widgets import Welcome


class TestButton(Static):

    def compose(self):
        yield Button("Button 1")


class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static("Buzzword Bingo")
        yield self.widget

    # def for schleife für bestimmung der laenge
    def Spalten(self):
        for i in range(0,5):
            yield TestButton() #("Button " + str(i))
        #def for schleife für bestimmung der breite
    def Zeilen(self): #addet Zeilen
        for i in range(0,5):
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
