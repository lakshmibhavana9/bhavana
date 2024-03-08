from typing import AnyStr
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *
from pydantic import Field

class ReadPDFArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file")

class ReadPDF(BaseTool):
    """Tool that adds the capability to read text from a PDF file."""

    name = "pdf_read"
    description = "A tool to read text content from a PDF file."
    
    args_schema: Optional[Type[BaseModel]] = ReadPDFArgs

    def _run(self, file_path: AnyStr) -> str:
        # Open the PDF file
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PdfReader(file)

            # Read text from each page
            text_content = ""
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text_content += page.extract_text()

        return text_content

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "_main_":
    # Replace 'your_pdf_file.pdf' with the actual path to your PDF file
    pdf_file_path = 'Resume_Bhavana.pdf'
    
    ans = ReadPDF()._run(pdf_file_path)
    print(ans)