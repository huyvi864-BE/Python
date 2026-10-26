class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        go = set()
        go.add(0)
        stack = [0]

        while stack:
            current_room = stack.pop()

            for key in rooms[current_room]:
                if key not in go:
                    go.add(key)
                    stack.append(key)
        return len(go) == len(rooms)