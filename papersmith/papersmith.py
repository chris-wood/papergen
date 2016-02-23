import os
import pymarkdown
import yaml

class DocumentCongiguration(object):
    pass

class Document(object):
    pass

class FileReader(object):
    def __init__(self, fname):
        self.fname = fname
        self.fhandle = open(fname, "r")

    def next_line(self):
        return self.fhandle.readline()

class ContentParser(object):
    def __init__(self, reader):
        pass
    pass

class ConfigParser(object):
    def __init__(self, reader):
        self.reader = reader

    def is_config_boundary(self, line):
        return line.startswith("---")
    
    def parse(self):
        line = self.reader.next_line()
        while not self.is_config_boundary(line):
            line = self.reader.next_line()

        line = self.reader.next_line()
        config_lines = [line]
        while not self.is_config_boundary(line):
            config_lines.append(line)
            line = self.reader.next_line()

        self.config_data = yaml.load("\n".join(config_lines))

class DocumentReader(object):
    def __init__(self, fname):
        self.fname = fname
        self.reader = FileReader(fname)

    def parse(self):
        self.config = ConfigParser(self.reader).parse()
        self.content = ContentParser(self.reader).parse()

def main(args):
    # TODO
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
