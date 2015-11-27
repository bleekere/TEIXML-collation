from collatex import *

# try with resources
with open("text_file_tsa", "r") as data_input:
    witness_a = data_input.read()

with open("text_file_tsb", "r") as data_input:
    witness_b = data_input.read()

# import witnesses in collateX
collation = Collation()
collation.add_plain_witness("liefde-tsa", witness_a) # p[2] in div n=01r
collation.add_plain_witness("liefde-tsb", witness_b) # p[2] in div n=01r

alignment_table = collate(collation, layout="vertical")

print(alignment_table)