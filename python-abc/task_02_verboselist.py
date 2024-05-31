#!/usr/bin/python3

""" Extending the Python List with Notifications """

class VerboseList(list):
    """
    Custom list class that prints notifications when items are added or removed.
    """

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with {len(x)} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=None):
        if index is None:
            index = -1
        else:
            item = super().pop(index)
            print(f"Popped {item} from the list.")
