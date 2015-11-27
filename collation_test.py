from collatex import *

# try with resources
with open("text_file_tsa", "r") as data_input:
    witness_a = data_input.read()

with open("text_file_tsb", "r") as data_input:
    witness_b = data_input.read()

# import witnesses in collateX
collation = Collation()
collation.add_plain_witness("liefde-tsa", witness_a)
collation.add_plain_witness("liefde-tsb", witness_b)

alignment_table = collate(collation, layout="vertical")

print(alignment_table)