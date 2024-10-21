pages = 100
lines = 50
symbols_line = 25
bytes_symbol = 4

disk_capacity_mb = 1.44

disk_capacity_bytes = int(disk_capacity_mb * 1024 * 1024)

total_characters = pages * lines * symbols_line

book_size_bytes = total_characters * bytes_symbol

number_of_books = disk_capacity_bytes // book_size_bytes


print("Количество книг, помещающихся на дискету:",number_of_books)
