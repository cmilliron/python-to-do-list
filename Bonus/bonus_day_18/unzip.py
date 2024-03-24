import zipfile

def extract_archive(file_path, dest_path):
    with zipfile.ZipFile(file_path, mode='r') as archive:
        archive.extractall(dest_path)

if __name__ == '__main__':
    extract_archive('/Users/codymilliron/Downloads/randomideas-theme.zip',
                    '/Users/codymilliron/Downloads')