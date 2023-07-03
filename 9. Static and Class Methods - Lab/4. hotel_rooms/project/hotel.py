class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))

            if not room.is_taken and room.capacity >= people:
                room.is_taken = True
                room.guests += people
                self.guests += people

        except StopIteration:
            return f"Room number {room_number} cannot be taken"

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))

            self.guests -= room.guests
            room.is_taken = False
            room.guests = 0

        except StopIteration:
            return f"Room number {room_number} is not taken"

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests" + \
               "\n" + \
               f"Free rooms: {', '.join(free_rooms)}" + \
               "\n" + \
               f"Taken rooms: {', '.join(taken_rooms)}"

from room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
