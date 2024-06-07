def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    stripped_blocks = [line.strip() for line in lines]
    return list(filter(None, stripped_blocks))