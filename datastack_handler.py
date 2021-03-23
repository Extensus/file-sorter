import os


class databaseApi:

    def file_maintainance(self):
        isfile = os.path.isfile("./file_sort_var_db.txt") and os.access("./file_sort_var_db.txt", os.R_OK)
        if not isfile:      # checks if the file exists and if it is accessible
            with open("./file_sort_var_db.txt", "w+") as f:     # creates template file if isfile == False
                f.write("<=#=#=#=> SETTINGS <=#=#=#=>"

                        "\n\n#> EXTENSION LIST (ADD IF YOU NEED MORE, KEEP EXISTING FORMAT) <#"
                        "\n\nAudio Extensions=['mp3', 'wav', 'raw', 'mid', 'midi', 'wma']"
                        "\nVideo Extensions=['mp4', 'mpg', 'mpeg', 'avi', 'flv', 'mov', 'mkv', 'mwv', 'h264', 'm4v']"
                        "\nImage Extensions=['png', 'jpeg', 'jpg', 'gif', 'svg', 'bmp', 'psd', 'tiff', 'tif']"
                        "\nDocument Extensions=['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'tex', "
                        "'odt', 'ppt', 'pptx', 'log', 'mobi', 'html', 'epub'] "
                        "\nCompressed File Extensions=['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']"
                        "\nExecutable Extensions=['dmg', 'iso', 'exe']"
                        "\nWord Extensions=['doc', 'docx']"
                        "\nPower Point Extensions=['ppt', 'pptx', 'pptm', 'ppsx']"

                        "\n\n#> SUPPORTED DIRECTORIES TO SORT TO <#"
                        "\n\nDownloads Directory=C:\\Users\\eric\\Downloads"
                        "\nDocuments Directory=C:\\Users\\usr\\Documents"
                        "\nDesktop Directory=C:\\Users\\usr\\Desktop"
                        "\nMusic Directory=C:\\Users\\usr\\Music"
                        "\nVideo Directory=C:\\Users\\usr\\Video"
                        "\n\Pictures Directory=C:\\Users\\usr\\Pictures"
                        "\nZip File Directory=C:\\Users\\usr\\Desktop"
                        "\nExecutable Directory=C:\\Users\\usr\\Desktop"

                        "\n\n#> MONITORED DIRECTORIES THAT ARE SUPPORTED BY THE SYSTEM (Please provide Directories "
                        "above) <# "
                        "\n\nSort Downloads=False"
                        "\nSort Documents=False"
                        "\nSort Desktop=False"
                        "\nSort Audio=False"
                        "\nSort Video=False"
                        )

    def __init__(self):     # assigns class variables
        self.content = None
        self.fetchedVars = {}
        self.vars = []
        self.conts = []

        self.file_maintainance()

    def variable_fetching(self, item):      # assigns the variables and contents from settings db file (fetching)
        try:
            var = None
            cont = None
            var = item[0]
            cont = item[1]
            self.vars.append(var)
            self.conts.append(cont)
        except IndexError:
            pass
        return var, cont

    def get_from_base(self):
        self.file_maintainance()    # checks if the file has been corrupted or deleted
        # gets file contents with previously created variable_fetching function
        with open('./file_sort_var_db.txt', 'r+') as f:
            self.content = f.read().splitlines()
            for item in self.content:
                list_item = item.split("=", 1)
                var, cont = self.variable_fetching(list_item)
                self.fetchedVars[var] = cont

            return self.fetchedVars

    def change_var(self, var):      # placeholder for changing variables dynamically

        pass

    def write_to_base(self):
        with open('./file_sort_var_db.txt', 'w') as f:      # updates database through overwriting everything
            try:
                if self.content is not None:
                    for x in self.fetchedVars:
                        f.write(f"{x}\n")
                else:
                    pass
            except TypeError:
                pass


if __name__ == '__main__':
    api = databaseApi()
    api.get_from_base()
    print(api.fetchedVars)

