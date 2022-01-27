def finding_parents(input):
    # maak een lege lijst
    output = []
    # get parent of input
    while input != None:
        input = input.getparent()
        # wanneer input geen parent heeft (root bereikt bij parent=None)
        if input != None:
            output.append(input)
    return output