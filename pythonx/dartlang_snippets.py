def ensure_import(path, snip):
    """Adds missing imports to the top of the file."""
    if ":" not in path:
        path = "package:%s.dart" % path
    full_line = "import '%s';" % path
    if full_line not in snip.buffer:
        snip.buffer.append(full_line, 0)
