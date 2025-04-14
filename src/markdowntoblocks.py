def markdown_to_blocks(markdown):
    md_split=markdown.split("\n\n")

    for i in range(len(md_split)):
        md_split[i]=md_split[i].strip()
    
    md_split=list(filter(None, md_split))

    return md_split

markdown_to_blocks("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")