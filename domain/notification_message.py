class NotificationMessage:
    title: str
    description: str
    color: int
    footer_text: str

    # ベースの色は16進数65280(Green)
    def __init__(
        self,
        title: str,
        description: str = "",
        color: int = 65280,
        footer_text: str = "",
    ):
        self.title = title
        self.description = description
        self.color = color
        self.footer_text = footer_text
