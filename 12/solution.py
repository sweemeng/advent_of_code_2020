class Ship:
    def __init__(self, waypoint_mode=False):
        self.heading = (0,1)
        self.headings = [(1,0), (0,1), (-1,0), (0,-1)]
        self.headings_waypoint = [(1,1), (-1,1), (-1,-1),(1,-1)]
        self.pos = (0,0)
        self.waypoint_mode = waypoint_mode
        self.waypoint = (1,1)

    def move(self, command):
        cmd, amount = command[0], int(command[1:])
        
        if cmd in ["N","E","W","S"]:
            if self.waypoint_mode:
                self.waypoint = self.move_news(cmd, amount)
            else:
                self.pos = self.move_news(cmd, amount)
        elif cmd == "F":
            self.pos = self.move_forward(cmd, amount)
     
        elif cmd in ["L","R"]:
            if self.waypoint_mode:
                self.waypoint = self.move_left_right_waypoint(cmd, amount)
            else:
                self.heading = self.move_left_right(cmd, amount)

    def move_left_right_waypoint(self, command, amount):
        amount = amount / 90
        amount = int(amount)
        x, y = self.waypoint
        direction = self.headings_waypoint
        # We don't care we always start at top left whenever we turn
        idx = 0
        
        while amount > 0:
            x,y = y,x
            if command == "R":
                idx = (idx+1) % len(direction)
            else:
                 idx -= 1
            amount = amount - 1
        dx,dy = direction[idx]
        return x*dx, y*dy
            
    
    def move_left_right(self, command, amount):
        amount = amount / 90
        amount = int(amount)
        if command == "R":
            idx = self.headings.index(self.heading)
            idx = (idx + amount) % len(self.headings)
            return self.headings[idx]
        else:
            idx = self.headings.index(self.heading)
            idx -= amount
            return self.headings[idx]

    def move_forward(self, command, amount):
        if self.waypoint_mode:
            dx, dy = self.waypoint
        else:
            dx, dy = self.heading
        dx *= amount
        dy *= amount
        x, y = self.pos
        return x+dx, y+dy

    def move_news(self, command, amount):
        directions = {
            "N": (1,0),
            "E": (0,1),
            "W": (0,-1),
            "S": (-1,0),
        }
        dx, dy = directions[command]
        dx = dx * amount
        dy = dy * amount
        if self.waypoint_mode:
            x, y = self.waypoint
        else:
            x, y = self.pos
        return x + dx, y + dy




def main():
    with open("input") as f:
        data=f.readlines()
    ship = Ship()
    for cmd in data:
        ship.move(cmd)
    x, y = ship.pos
    result = abs(x) + abs(y)
    print(f"Result 1: {result}")


    ship = Ship(waypoint_mode=True)
    ship.waypoint = (1,10)
    for cmd in data:
        ship.move(cmd)
    x,y = ship.pos
    result = abs(x) + abs(y)
    print(f"Result 2: {result}")


if __name__ == "__main__":
    main()
