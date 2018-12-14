def part_1():
    def power_level(x_cord, y_cord, serial):
        #print(f"x cord: {x_cord}, y cord: {y_cord}, serial: {serial}")
        rack_id = x_cord + 10
        #print(f"rack id: {rack_id}")
        power = rack_id * y_cord
        #print(f"power :{power}")
        power += serial
        #print(f"power :{power}")
        power = power * rack_id
        #print(f"power :{power}")
        power = str(power)
        #print(f"power :{power}")
        power = int(power[-3])
        #print(f"power :{power}")
        power -= 5
        #print(f"power :{power}")
        return power

    #print(power_level(3,5,8))
    #print(power_level(122,79,57))
    serial = 5468
    grid_size = 3
    grid_range = range(1,300 - grid_size + 2)
    max_coord = (0,0,0)
    cache = {}

    for y in grid_range:
        for x in grid_range:
            local_sum = 0
            print(f"eval at x:{x}, y:{y}")
            for y1 in range(0, grid_size):
                for x1 in range(0, grid_size):
                    print(x+x1,y+y1)
                    if (x+x1,y+y1) in cache:
                        local_sum += cache[(x+x1, y+y1)]
                    else:
                        pl = power_level(x+x1, y+y1, serial)
                        local_sum += pl
                        cache[(x+x1,y+y1)] = pl
            print(x,y,local_sum)
            if local_sum > max_coord[2]:
                max_coord = (x,y,local_sum)
    print("final: ",max_coord)


def part_2():
    def power_level(x_cord, y_cord, serial):
        #print(f"x cord: {x_cord}, y cord: {y_cord}, serial: {serial}")
        rack_id = x_cord + 10
        #print(f"rack id: {rack_id}")
        power = rack_id * y_cord
        #print(f"power :{power}")
        power += serial
        #print(f"power :{power}")
        power = power * rack_id
        #print(f"power :{power}")
        power = str(power)
        #print(f"power :{power}")
        power = int(power[-3])
        #print(f"power :{power}")
        power -= 5
        #print(f"power :{power}")
        return power

    #print(power_level(3,5,8))
    #print(power_level(122,79,57))
    cache = {}
    max_coord = (0,0,0,0)
    serial = 5468
    for x in range(1,301):
        for y in range(1,301):
            max_grid_size = 0
            local_sum = 0
            #print(x,y)
            if x > y:
                max_grid_size = x
            else:
                max_grid_size = y
            for grid_range in range(0,301-max_grid_size+1):
                for x1 in range(x,x+grid_range+1):
                    #print("eval: ", x1, y+grid_range)
                    local_sum += power_level(x1, y+grid_range, serial)

                for y1 in range(y,y+grid_range+1):
                    #print("eval: ", x+grid_range, y1)
                    local_sum += power_level(x1, y+grid_range, serial)
                #print(x,x+grid_range+1, y,y+grid_range+1)
                local_sum -= power_level(x+grid_range,y+grid_range, serial)
                if local_sum > max_coord[3]:
                    max_coord = (x,y,grid_range,local_sum)
                    print("new max: ", max_coord)
            print(x,y,301-max_grid_size)

    print(max_coord)

part_2()
