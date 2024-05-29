from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Column

class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static("Buzzword Bingo")

        # Erstelle eine Column mit 5 Spalten
        self.column = Column()
        for i in range(5):
            row = []
            for j in range(5):
                button = Button(f"Button {i+1}-{j+1}")
                row.append(button)
            self.column.add_child(*row)

        yield self.widget
        yield self.column

    def on_mount(self) -> None:
        self.widget.styles.background = "aquamarine"
        self.widget.styles.color = "black"
        self.widget.styles.border = ("heavy", "black")
        self.widget.styles.width = 17

if __name__ == "__main__":
    app = WidgetApp()
    app.run()