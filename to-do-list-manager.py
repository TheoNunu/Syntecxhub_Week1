list = input('Enter your to-do list items separated by commas: ').split(',')
array = [item.strip() for item in list]
print("Your to-do list:")
for i, item in enumerate(array, start=1):
    print(f"{i}. {item}")

add_items = input("Enter items to add separated by commas (or press Enter to skip): ")
if add_items != "":
    new_items = [item.strip() for item in add_items.split(",") if item.strip()]
    array.extend(new_items)
    if new_items:
        print(f"Added {len(new_items)} item(s) to your to-do list.")

if len(array) > 0:
    remove_item = input("Enter the number of the item you want to remove (or press Enter to skip): ")
    if remove_item.isdigit():
        index_to_remove = int(remove_item) - 1
        if 0 <= index_to_remove < len(array):
            removed_item = array.pop(index_to_remove)
            print(f"Removed '{removed_item}' from your to-do list.")
        else:
            print("Invalid item number.")
    elif remove_item != "":
        print("Please enter a valid number.")

if len(array) > 0:
    print("Updated to-do list:")
    for i, item in enumerate(array, start=1):
        print(f"{i}. {item}")


if len(array) == 0: 
    print("Your to-do list is empty.") 


