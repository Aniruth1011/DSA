class Solution:
    def maximumTime(self, time: str) -> str:
        hours = time[:2]
        minutes = time[3:]
        res = []
        if hours == "??":
            res.append("23")
        elif hours[0] == "?" and hours[1]!="?":
            if int(hours[1])<4:
                res.append("2")
                res.append(hours[1])
            else:
                res.append("1")
                res.append(hours[1])
        elif hours[0]!="?" and hours[1]=="?":
            if int(hours[0]) <2:
                res.append(hours[0])
                res.append("9")
            else:
                res.append(hours[0])
                res.append("3")
        else:
            res.append(hours)
        res.append(":")
        if minutes == "??":
            res.append("59")
        elif minutes[0] == "?" and minutes[1]!="?":
            res.append("5")
            res.append(minutes[1])
        elif minutes[0] != "?" and minutes[1]=="?":
            res.append(minutes[0])
            res.append("9")
        else:
            res.append(minutes)

        return "".join(res)
