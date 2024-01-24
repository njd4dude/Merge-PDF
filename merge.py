from PyPDF2 import PdfMerger
import os


def merge_pdfs(input_folder, output_folder, output_file):
    try:
        merger = PdfMerger()

        # Ensure the output folder exists, create it if necessary
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Get a list of all PDF files in the input folder
        input_files = [file for file in os.listdir(
            input_folder) if file.endswith('.pdf')]

        for pdf in input_files:
            pdf_path = os.path.join(input_folder, pdf)
            print(f"Attaching file: {pdf}")
            merger.append(pdf_path)

        # Concatenate the output folder and file name
        output_path = os.path.join(output_folder, output_file)

        merger.write(output_path)
        merger.close()

        print(f"Merged PDFs saved to: {output_path}")

    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    # Specify the input folder, output folder, and file name
    input_folder = "input"
    output_folder = "output"
    output_file = "combined_output.pdf"

    merge_pdfs(input_folder, output_folder, output_file)
