from conlltoken import *
class ConLLUTokenBuilder(object):
    def buildToken(self, line):
        self.array = []
        line = line.strip()
        if line == "": 
            pass
        else:
            self.array = line.split()
        return ConLLToken(self.array[1], self.array[2], self.array[3], self.array[5])


builder = ConLLUTokenBuilder()
line = "1 The the DET _ Definite=Def|PronType=Art _ _ _ _"
tok = builder.buildToken(line)
print("Token:", str(tok))
print("Type:", type(tok))
class ConLL09TokenBuilder(object):
    def buildToken(self, line):
        self.array = []
        line = line.strip()
        if line == "":
            pass
        else:
            self.array = line.split()

        return ConLLToken(self.array[1], self.array[2], self.array[4], self.array[6])


builder = ConLL09TokenBuilder()
line = "6   zujda   gzwiq   _       DET     _       Mood=Sub|Number=Plur|Person=3   _       4       _       obj     _       _       _       _"
tok = builder.buildToken(line)
print("Token:", str(tok))
print("Type:", type(tok))
