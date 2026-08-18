def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item

order_list = ['Pizza', 'Burger', 'Sandwich']

removed = remove_last_item(order_list)

print("Removed item:", removed)
print("Updated order list:", order_list)