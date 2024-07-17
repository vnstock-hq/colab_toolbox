# a function to run ocrmypdf command line tool
import os
import subprocess
from typing import Union

class OCR:
    def __init__(self, input_dir:str, output_dir:Union[str, None]=None):
        """
        Initialize the OCR class with input and output directories.
        
        Args:
            input_dir (str): Path to the input directory containing the files to be processed.
            output_dir (str, optional): Path to the output directory where the processed files will be stored. If not provided, the input directory will be used.
        """
        self.input_dir = input_dir
        if output_dir is None:
            self.output_dir = input_dir
        else:
            self.output_dir = output_dir

    def to_pdfa (self, file_name:str, lang='vie+eng'):
        """
        Converts the given file to PDF/A format using ocrmypdf command line tool.
        Args:
            - file_name (str): Name of the file to be converted.
            - lang (str, optional): Language(s) to be used for conversion. Defaults to 'vie+eng'.
        Raises:
            - ValueError: If the input file is not in PDF format.
        """
        # validation, file_name should be in pdf format
        file_extension = os.path.splitext(file_name, '.')[-1]
        
        if file_extension != "pdf":
            raise ValueError("Input file should be in PDF format.")

        input_file = os.path.join(self.input_dir, file_name)
        output_file = os.path.join(self.output_dir, os.path.splitext(file_name)[0] + ".pdf")

        # run command and show stdout: ocrmypdf -l {lang} {input_file} {output_file}
        subprocess.run(["ocrmypdf", "-l", lang, input_file, output_file], stdout=subprocess.PIPE, check=True)
        print(f"Converted {input_file} to {output_file}")

    def to_text (self, file_name:str, lang='vie+eng'):
        """
        Converts the given file to text format using ocrmypdf command line tool.
        Args:
            - file_name (str): Name of the file to be converted.
            - lang (str, optional): Language(s) to be used for conversion. Defaults to 'vie+eng'.
        Raises:
            - ValueError: If the input file is not in PDF format.
        """
        # validation, file_name should be in pdf format
        file_extension = file_name.split('.')[-1]

        if file_extension != "pdf":
            raise ValueError("Input file should be in PDF format.")

        input_file = os.path.join(self.input_dir, file_name)
        output_txt = os.path.join(self.output_dir, os.path.splitext(file_name)[0] + ".txt")
        output_pdf = os.path.join(self.output_dir, os.path.splitext(file_name)[0] + ".pdf")

        # run command and show stdout: ocrmypdf -l {lang} --deskew {input_file} {output_file}
        subprocess.run(["ocrmypdf", "--sidecar", output_txt, input_file, output_pdf, '-l', lang, "--force-ocr"], stdout=subprocess.PIPE, check=True)
        print(f"Converted {input_file} to {output_txt} and {output_pdf}")

    def image_to_pdf (self, file_name:str, lang:str='vie+eng'):
        """
        Performs OCR on the given image file using tesseract command line tool.
        Args:
            - file_name (str): Name of the image file to be processed.
            - lang (str, optional): Language to be used for OCR. Defaults to 'vi' for Vietnamese. For multiple languages, using plus sign (+) to join. For instance, "vie+eng" for Vietnamese and English.
        """
        # validation, file_name should be in image format
        file_extension = file_name.split('.')[-1].lower()

        if file_extension not in ["jpg", "jpeg", "png", "gif", 'webp', 'bmp', 'pnm']:
            raise ValueError("Input file should be in supported image formats: jpg, jpeg, png, gif, webp, bmp, pnm.")

        input_file = os.path.join(self.input_dir, file_name)
        output_name = file_name.split('.')[0]

        # run command and show stdout: tesseract {input_file} {output_file} -l {lang}
        subprocess.run(["tesseract", input_file, output_name, "pdf", "-l", lang], stdout=subprocess.PIPE, check=True)
        print(f"Converted {input_file} to pdf file")

    def image_to_text (self, file_name:str, lang:str='vie+eng'):
        """
        Performs OCR on the given image file using tesseract command line tool.
        Args:
            - file_name (str): Name of the image file to be processed.
            - lang (str, optional): Language to be used for OCR. Defaults to 'vi' for Vietnamese. For multiple languages, using plus sign (+) to join. For instance, "vie+eng" for Vietnamese and English.
        """
        # validation, file_name should be in image format
        file_extension = file_name.split('.')[-1].lower()

        if file_extension not in ["jpg", "jpeg", "png", "gif", 'webp', 'bmp', 'pnm']:
            raise ValueError("Input file should be in supported image formats: jpg, jpeg, png, gif, webp, bmp, pnm.")

        input_file = os.path.join(self.input_dir, file_name)

        # run command and show stdout: tesseract {input_file} stdout -l {lang}
        subprocess.run(["tesseract", input_file, "-", "-l", lang], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
        # print(f"Converted {input_file} succeed!")