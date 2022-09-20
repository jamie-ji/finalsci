# PDF转成word包
# 基于Adobe Developer API

# 1.提取PDF转化为zip
# 2.解压zip，得到json文件
# 3.解析json文件，得到每段正文，根据段落数或字数来确定摘要，把摘要那个生成一个可调用的类

import zipfile
import logging
from msilib.schema import Class
import os.path

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from numpy import save



    
#zipo
def zipcreate(pdfpath,savepath):

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    try:
        # get base path.
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # Initial setup, create credentials instance.
        credentials = Credentials.service_account_credentials_builder() \
            .from_file('D:\discourse_code\code\preprocess\pdf2json\pdfservices-api-credentials.json') \
            .build()

        # Create an ExecutionContext using credentials and create a new operation instance.
        execution_context = ExecutionContext.create(credentials)
        extract_pdf_operation = ExtractPDFOperation.create_new()

        # Set operation input from a source file.
        source = FileRef.create_from_local_file(pdfpath)
        extract_pdf_operation.set_input(source)

        # Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        # Execute the operation.
        result: FileRef = extract_pdf_operation.execute(execution_context)

        # Save the result to the specified location.
        result.save_as(savepath)

        print("转换成功！！！")
    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation")
        print("转换失败！！！请检查网络")
