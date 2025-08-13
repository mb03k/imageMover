
class GlobalVariables:
    paths = ["", ""]
    selected_language = "de"    

    def __init__(self, imageInputPath, imageOutputPath, selectedLanguage):
        self.paths = [imageInputPath, imageOutputPath]
        self.selected_language = selectedLanguage

    def setSelectedLanguage(self, selectedLanguage):
        self.selected_language = selectedLanguage

    def setPaths(self, paths):
        self.paths = paths
