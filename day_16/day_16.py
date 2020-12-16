def GetFields(filename):
    # There is an easier way to do all this, a much easier way if I finally get to grips with regex
    
    field_keys = [] # the order is important, so keep the field keys in a list
    field_valid_ranges = [] # store the pair of pair of numbers that describe the valid range for each field
    personal_ticket = None
    nearby_tickets = []

    # read field and its valid range
    with open(filename, "r") as f:
        fields_mode = True
        personal_ticket_mode = False
        nearby_tickets_mode = False

        for line in f:
            if line == '\n':
                if fields_mode:
                    fields_mode = False
                    personal_ticket_mode = True
                elif personal_ticket_mode:
                    personal_ticket_mode = False
                    nearby_tickets_mode = True
                continue
            
            elif line[-1] == '\n':
                line = line[:-1]
            
            if fields_mode:
                field_valid_range = []
                line = line.split(": ")

                field_keys.append(line[0]) 
                
                valid_ranges_raw = line[1].split(" or ")

                for raw_range in valid_ranges_raw:
                    valid_range = raw_range.split("-")
                    valid_range[0] = int(valid_range[0])
                    valid_range[1] = int(valid_range[1])

                    field_valid_range.append(tuple(valid_range))
                
                field_valid_ranges.append(tuple(field_valid_range))
                
            elif personal_ticket_mode:
                if line[0] == 'y':
                    continue
                else:
                    personal_ticket = line.split(',')

                    for i in range(len(personal_ticket)):
                        personal_ticket[i] = int(personal_ticket[i])

            elif nearby_tickets_mode:
                if line[0] == 'n':
                    continue
                else:
                    nearby_ticket = line.split(',')

                    for i in range(len(nearby_ticket)):
                        nearby_ticket[i] = int(nearby_ticket[i])

                    nearby_tickets.append(nearby_ticket)

    
    return field_keys, field_valid_ranges, personal_ticket, nearby_tickets
    
def IsInRange(number, r):
    return number >= r[0] and number <= r[1]
    
def ScanErrorRate(tickets, field_valid_ranges):
    error_rate = 0
    invalid_tickets = []
    for ticket in tickets:
        for i in range(len(ticket)):
            is_valid = False
            for valid_range in field_valid_ranges:
                if IsInRange(ticket[i], valid_range[0]) or IsInRange(ticket[i], valid_range[1]):
                    is_valid = True
                    break
            
            if not is_valid:
                error_rate += ticket[i]
                
            
    return error_rate

if __name__=="__main__":
    filename = "input.txt"
    field_keys, field_valid_ranges, personal_ticket, nearby_tickets = GetFields(filename)
    error_rate = ScanErrorRate(nearby_tickets, field_valid_ranges)
    print(f"Part 1: Error Rate = {error_rate}")