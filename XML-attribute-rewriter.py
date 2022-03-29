import sys
import getopt
import xml.etree.ElementTree as ET


class XmlAttributeRewriter:
    def __init__(self, file_path) -> None:
        self._file_path: str = file_path
        self._tree: ET.ElementTree = ET.parse(file_path)
        self._root: ET.Element = self._tree.getroot()
        self._ENCODING: str = 'utf-16'

    def rewrite_attribute(self, node_path, attribute_path, value) -> None:
        self._root.find(f'./{node_path}').set(attribute_path, value)
        self._tree.write(
            self._file_path,
            encoding=self._ENCODING, xml_declaration=True)


if(__name__ == '__main__'):
    FILE_COMMAND_KEY, NODE_KEY, ATTRIBUTE_KEY, VALUE_KEY = '-f', '-n', '-a', '-v'

    command_dictionary = dict()

    arguments = getopt.getopt(sys.argv[1:], 'f:n:a:v:')[0]

    for tupple in arguments:
        key = tupple[0]
        command = tupple[1]
        command_dictionary[key] = command

    rewriter: XmlAttributeRewriter = XmlAttributeRewriter(
        command_dictionary[FILE_COMMAND_KEY])

    rewriter.rewrite_attribute(
        command_dictionary[NODE_KEY], command_dictionary[ATTRIBUTE_KEY], command_dictionary[VALUE_KEY])
