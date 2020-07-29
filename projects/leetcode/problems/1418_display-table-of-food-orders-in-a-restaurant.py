class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        food = {}
        table = {}
        for order in orders:
            if(food.has_key(order[2])):
                food[order[2]].append(order[1])
            else:
                food[order[2]] = [order[1]]
            if(table.has_key(int(order[1]))):
                table[int(order[1])].append(order[2])
            else:
                table[int(order[1])] = [order[2]]
        foodCol = {}
        result = [['Table']]
        foodItems = len(food.keys())
        foodIndex = 1
        for key in sorted(food):
            print(key)
            result[0].append(key)
            foodCol[key] = foodIndex
            foodIndex += 1
        for key in sorted(table):
            t = ['0']*(foodItems + 1)
            t[0] = str(key)
            for f in table[key]:
                t[foodCol[f]] = str(int(t[foodCol[f]]) + 1)
            result.append(t)
        return(result)
