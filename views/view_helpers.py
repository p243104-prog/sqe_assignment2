"""Reusable helpers for Tkinter views."""


def clear_tree(tree):
    """Remove all items from a Tkinter Treeview."""
    for item in tree.get_children():
        tree.delete(item)
