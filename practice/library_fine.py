def fine(date_book_return, supposed_return_date):
    d1, m1, y1 = date_book_return
    d2, m2, y2 = supposed_return_date
    hackos = 0

    if y1 <= y2 and m1 <= m2 and d1 <= d2:
        return hackos

    if y1 < y2:
        return hackos

    if m1 < m2 and y1 <= y2:
        return hackos

    if y1 > y2:
        hackos += 10000
        return hackos

    if m1 > m2:
        hackos = 500 * (m1 - m2)
        return hackos

    if d1 > d2:
        hackos = 15 * (d1 - d2)
        return hackos


date_returned = list(map(int, input().split()))
date_to_return = list(map(int, input().split()))
print(fine(date_returned, date_to_return))
