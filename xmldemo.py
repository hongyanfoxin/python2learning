import xml.etree.ElementTree as ET

write_dic = {}
key = "the Text message"
value = "the Parse message"
write_dic[key] = value

# a = ET.Element('a')
# b = ET.SubElement(a, 'b')
# c = ET.SubElement(a, 'c')
# d = ET.SubElement(c, 'd')
# ET.dump(a)

sentences = ET.Element('Sentences')
sent = ET.SubElement(sentences, 'Sentence')
text = ET.SubElement(sent, 'Text')
parse = ET.SubElement(sent, 'Parse')
text.text = "the Text message"
parse.text = "the Parse message"
ET.dump(sentences)
#<Sentences><Sentence><Text>the Text message</Text><Parse>the Parse message</Parse></Sentence></Sentences>
