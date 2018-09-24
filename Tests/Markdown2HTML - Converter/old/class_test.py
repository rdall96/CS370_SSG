import markdown2html as Converter

input = raw_input("select file: ")
output = Converter.markdown2html(input)
#print(output)