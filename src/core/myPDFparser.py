import os
import re
from magic_pdf.data.data_reader_writer import FileBasedDataWriter, FileBasedDataReader
from magic_pdf.data.dataset import PymuDocDataset
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.config.enums import SupportedPdfParseMethod
from core.utils import encode_image_to_base64
from core.myImageParser import ParserImage

class PDF2MarkdownConverter:
    def __init__(self, pdf_root_dir: str, output_dir: str):
        self.pdf_root_dir = pdf_root_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def convert(self):
        for file in os.listdir(self.pdf_root_dir):
            if not file.endswith(".pdf"):
                continue

            pdf_path = os.path.join(self.pdf_root_dir, file)
            base_name = os.path.splitext(file)[0]

            # 设置输出路径
            local_output_dir = os.path.join(self.output_dir, "output_" + base_name)
            local_image_dir = os.path.join(local_output_dir, "images")
            local_md_dir = local_output_dir
            parsed_md_dir = os.path.join(self.output_dir, "parsed")
            os.makedirs(parsed_md_dir, exist_ok=True)
            os.makedirs(local_image_dir, exist_ok=True)

            # 初始化 Reader 和 Writer
            image_writer = FileBasedDataWriter(local_image_dir)
            md_writer = FileBasedDataWriter(local_md_dir)
            reader = FileBasedDataReader("")
            pdf_bytes = reader.read(pdf_path)

            # 解析 PDF
            ds = PymuDocDataset(pdf_bytes)
            if ds.classify() == SupportedPdfParseMethod.OCR:
                infer_result = ds.apply(doc_analyze, ocr=True)
                pipe_result = infer_result.pipe_ocr_mode(image_writer)
            else:
                infer_result = ds.apply(doc_analyze, ocr=False)
                pipe_result = infer_result.pipe_txt_mode(image_writer)

            # 输出 Markdown
            md_filename = f"{base_name}.md"
            pipe_result.dump_md(md_writer, md_filename, local_image_dir)

            # 加载并处理 Markdown
            md_path = os.path.join(local_md_dir, md_filename)
            with open(md_path, "r", encoding="utf-8") as f:
                md_lines = f.readlines()

            new_md_lines = []
            for line in md_lines:
                new_md_lines.append(line)
                match = re.search(r'!\[\]\((.*?)\)', line)
                if match:
                    image_rel_path = match.group(1)
                    image_abs_path = os.path.join(local_output_dir, image_rel_path)
                    if os.path.exists(image_abs_path):
                        convert_image = ParserImage()
                        image_base64 = encode_image_to_base64(image_abs_path)
                        description = convert_image.convert_image_to_md(image_base64)
                        new_md_lines.append(f"> Image Description: \n{description}\n")

            # 保存新 Markdown 到 parsed 目录
            parsed_md_path = os.path.join(parsed_md_dir, md_filename)
            with open(parsed_md_path, "w", encoding="utf-8") as f:
                f.writelines(new_md_lines)

            print(f"✅ Already Done: {file}")