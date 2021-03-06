"""
    pyexcel.source.file_source_input
    ~~~~~~~~~~~~~~~~~~~

    Representation of input file sources

    :copyright: (c) 2015-2017 by Onni Software Ltd.
    :license: New BSD License
"""
import pyexcel.constants as constants
import pyexcel.internal.parser_meta as parsers
from . import params
from .file_sources import InputSource


class ReadExcelFileMemory(InputSource):
    """Pick up 'file_type' and read a sheet from memory"""
    fields = [params.FILE_TYPE]
    targets = (constants.SHEET, constants.BOOK)
    actions = (constants.READ_ACTION,)
    attributes = parsers.get_all_file_types()
    key = params.FILE_TYPE

    def __init__(self,
                 file_content=None,
                 file_type=None,
                 file_stream=None,
                 **keywords):
        self.__file_type = file_type
        self.__file_stream = file_stream
        self.__file_content = file_content
        self.__keywords = keywords
        self.__parser = parsers.get_parser(file_type)

    def get_data(self):
        if self.__file_stream is not None:
            sheets = self.__parser.parse_file_stream(
                self.__file_stream,
                **self.__keywords)
        else:
            sheets = self.__parser.parse_file_content(
                self.__file_content,
                **self.__keywords)
        return sheets

    def get_source_info(self):
        return params.MEMORY, None
