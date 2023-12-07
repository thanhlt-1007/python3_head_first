import html

print("Escape: " + html.escape("This HTML fragment contains a <script>script</script> tag."))
print("Unescape: " + html.unescape("I &hearts; Python's &lt;standard library&gt;."))
