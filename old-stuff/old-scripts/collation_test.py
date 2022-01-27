from collatex import *

# try with resources
with open("xml/plain-text-ts-fol.txt", "r") as data_input:
    witness_a = data_input.read()

with open("xml/plain-text-tsq.txt", "r") as data_input:
    witness_b = data_input.read()

# import witnesses in collateX
collation = Collation()
collation.add_plain_witness("liefde-tsq", witness_a)
collation.add_plain_witness("liefde-ts-fol", witness_b)

alignment_table = collate(collation, layout="vertical")

print(alignment_table)