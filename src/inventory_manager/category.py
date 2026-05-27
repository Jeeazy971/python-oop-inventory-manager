class Category:
    DEFAULT_DESCRIPTION = "Aucune description"

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def has_description(self):
        return self.description != "" and self.description != self.DEFAULT_DESCRIPTION

    def get_info(self):
        if self.description == "":
            return f"Catégorie: {self.name} - {self.DEFAULT_DESCRIPTION}"
        else:
            return f"Catégorie: {self.name} - {self.description}"
