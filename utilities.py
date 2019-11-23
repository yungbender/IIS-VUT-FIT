def format_date(ticket):
    if not ticket:
        return None

    ticket.creation_date = str(ticket.creation_date.day) + "." + str(ticket.creation_date.month) + "." + str(ticket.creation_date.year)
