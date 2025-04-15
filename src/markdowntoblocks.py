def markdown_to_blocks(markdown):
    md_split=markdown.split("\n\n")

    for i in range(len(md_split)):
        md_split[i]=md_split[i].strip()
    
    md_split=list(filter(None, md_split))

    return md_split

