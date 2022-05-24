square_length = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())
time_for_one_tile = 0.2

square_area = square_length * square_length
bench_area = bench_width * bench_length
area_for_covering = square_area - bench_area
tile_area = tile_width * tile_length
needed_tiles = area_for_covering / tile_area
time = needed_tiles * time_for_one_tile

print(needed_tiles)
print(f"{time}")
