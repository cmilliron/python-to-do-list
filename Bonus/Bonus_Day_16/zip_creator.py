import zipfile
from pathlib import Path
import datetime


def make_archive(filepaths, dest_dir):
    now = datetime.datetime.now()

    output_file = Path(dest_dir, f"compressed-{now.isoformat()}.zip")
    with zipfile.ZipFile(output_file, "w") as archive:
        for filepath in filepaths:
            filepath = Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    test_data = ['/Users/codymilliron/Downloads/21500343-avada-responsive-multipurpose-theme-license.txt',
                 '/Users/codymilliron/Downloads/bundle.js',
                 '/Users/codymilliron/Downloads/Cody Milliron.hazellicense',
                 '/Users/codymilliron/Downloads/G3Y1QoZp',
                 '/Users/codymilliron/Downloads/House Marketplace.html',
                 '/Users/codymilliron/Downloads/HSTTestResultsReportPDF.pdf',
                 '/Users/codymilliron/Downloads/IBG-log-retina.png']

    make_archive(test_data, '/Users/codymilliron/Downloads')