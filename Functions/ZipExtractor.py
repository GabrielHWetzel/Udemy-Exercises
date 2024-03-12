import zipfile


def extract_archive(archivepath, destination):
    try:
        with zipfile.ZipFile(archivepath, 'r') as archive:
            archive.extractall(destination)
        return "File Extracted"
    except FileNotFoundError:
        return "File Not Found"
    except zipfile.BadZipfile:
        return "Not A Zip File"


if __name__ == "__main__":
    try :
        extract_archive(
            r"C:\Users\dwolf\Desktop\Documents\Code\Coding Excercises\Test\compressed.zip",
            r"C:\Users\dwolf\Desktop\Documents\Code\Coding Excercises\Test")
    except FileNotFoundError:
        print("File not Found")