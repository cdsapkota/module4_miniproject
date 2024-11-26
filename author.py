class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_details(self):
        details = (
        f"\nName: {self.__name}\n"
        f"Biography: {self.__biography}"
        )
        return details
