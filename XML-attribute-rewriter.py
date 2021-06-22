import sys
import getopt
import xml.etree.ElementTree as ET


class XmlAttributeRewriter:
    def __init__(self, file_path) -> None:
        self.__file_path__: str = file_path
        self.__tree__: ET.ElementTree = ET.parse(file_path)
        self.__root__: ET.Element = self.__tree__.getroot()
        self.__encoding__: str = 'utf-16'

    def rewrite_attribute(self, node_path, attribute_path, value) -> None:
        self.__root__.find(f'./{node_path}').set(attribute_path, value)
        self.__tree__.write(
            self.__file_path__,
            encoding=self.__encoding__, xml_declaration=True)


if(__name__ == '__main__'):
    must_have_commands = ['-f', '-n', '-a', '-v']
    command_dictionary = dict()

    opts = getopt.getopt(sys.argv[1:], 'f:n:a:v:')[0]

    for tupple in opts:
        key = tupple[0]
        command = tupple[1]
        command_dictionary[key] = command

    rewriter: XmlAttributeRewriter = XmlAttributeRewriter(
        command_dictionary['-f'])

    rewriter.rewrite_attribute(
        command_dictionary['-n'], command_dictionary['-a'], command_dictionary['-v'])
